#!/usr/bin/env python3
"""
PhoneBookLOCA - free API setup wizard
Created by: DezTheJackal

Walks you through getting the FREE API keys PhoneBookLOCA can use, shows the exact
page to open and what to copy BEFORE asking for each key, checks every key against
the live service, and saves them where PhoneBookLOCA loads them automatically.
Every service here is free. Nothing paid is ever offered.

Usage:
    python3 setup_apis.py                  # guided setup of every free service
    python3 setup_apis.py --links          # just print the links and steps, change nothing
    python3 setup_apis.py --only gemini    # one service (gemini, groq, opencellid; comma-separate several)
    python3 setup_apis.py --status         # show what is configured and test it
    python3 setup_apis.py --reset groq     # forget one key (or: --reset all)
    python3 setup_apis.py --no-browser     # never offer to open pages
    python3 setup_apis.py --no-test        # save keys without checking them online

Requirements: Python 3.8+ standard library only. Runs on Linux, macOS and Windows.
Keys are stored in ~/.phonebookloca/config.json (owner-only permissions where the
OS supports it). Real environment variables always override the saved file.
"""

import argparse
import getpass
import json
import os
import re
import sys
import tempfile
import urllib.error
import urllib.parse
import urllib.request
import webbrowser
from pathlib import Path

VERSION = "2.4.0"
USER_AGENT = f"PhoneBookLOCA-setup/{VERSION}"
CONFIG_DIR = Path.home() / ".phonebookloca"
CONFIG_FILE = CONFIG_DIR / "config.json"

# --------------------------------------------------------------------------- UI

USE_COLOR = sys.stdout.isatty() and os.environ.get("NO_COLOR") is None
if USE_COLOR and os.name == "nt":
    os.system("")          # enables ANSI escape processing on Windows 10+ consoles


def _c(code, text):
    return f"\033[{code}m{text}\033[0m" if USE_COLOR else text


def cyan(t): return _c("96", t)
def green(t): return _c("92", t)
def yellow(t): return _c("93", t)
def red(t): return _c("91", t)
def magenta(t): return _c("95", t)
def bold(t): return _c("1", t)


# ------------------------------------------------------------------- services

SERVICES = {
    "gemini": {
        "name": "Google Gemini",
        "purpose": "AI briefings (--ai, 'ai <number>' and LE-list briefings)",
        "env": "GEMINI_API_KEY",
        "url": "https://aistudio.google.com/apikey",
        "prefix": "AIza",
        "default_yes": True,
        "steps": [
            "Open the page below and sign in with any Google account.",
            "Click \"Create API key\" (accept the terms if asked - no credit card needed).",
            "Copy the key shown (it starts with \"AIza\").",
        ],
        "free": "Free tier, no credit card. Limits are per project and shown at "
                "https://aistudio.google.com/rate-limit",
        "warning": "On Google's free tier, prompts and responses MAY be used to improve Google products. "
                   "PhoneBookLOCA never sends the phone number, case number, officer, agency or file "
                   "names - only non-identifying metadata (carrier, line type, country, scores). "
                   "Every briefing file lists exactly what was sent.",
    },
    "groq": {
        "name": "Groq",
        "purpose": "AI briefings (alternative / automatic fallback to Gemini)",
        "env": "GROQ_API_KEY",
        "url": "https://console.groq.com/keys",
        "prefix": "gsk_",
        "default_yes": True,
        "steps": [
            "Open the page below and sign in (Google, GitHub or email - no credit card).",
            "Click \"Create API Key\" and give it a name such as phonebookloca.",
            "Copy the key IMMEDIATELY - it is shown only once (it starts with \"gsk_\").",
        ],
        "free": "Free tier with rate limits (see https://console.groq.com/docs/rate-limits).",
        "warning": "Same privacy rule as Gemini: only non-identifying metadata is ever sent. "
                   "Check Groq's terms if your agency has data-handling rules.",
    },
    "opencellid": {
        "name": "OpenCellID",
        "purpose": "Cell-tower lookup near the area-code location (OPTIONAL)",
        "env": "OPENCELLID_API_KEY",
        "url": "https://opencellid.org/",
        "prefix": None,
        "default_yes": False,
        "steps": [
            "Open the page below and sign up for a free account (confirm the e-mail).",
            "Log in and open your Dashboard.",
            "Copy your API access token (it is also called the API key).",
        ],
        "free": "Free key, 1,000 requests per day.",
        "warning": "The tower lookup PhoneBookLOCA uses is only served to whitelisted keys (free for apps "
                   "that contribute data). A normal key gets HTTP 403 and PhoneBookLOCA simply skips tower "
                   "data. Everything else works without this key - skipping it is fine.",
    },
}
ORDER = ["gemini", "groq", "opencellid"]
AI_SERVICES = ("gemini", "groq")


# ------------------------------------------------------------ model selection
# (same logic as PhoneBookLOCA itself, so the wizard and the tool always agree)

def pick_gemini_model(models):
    """Newest stable Gemini Flash model that supports generateContent."""
    best = None
    for m in models or []:
        name = (m.get("name") or "").replace("models/", "")
        if "generateContent" not in (m.get("supportedGenerationMethods") or []):
            continue
        mt = re.fullmatch(r"gemini-(\d+(?:\.\d+)?)-flash(-lite)?(-preview(?:-[\w.-]+)?)?", name)
        if not mt:
            continue
        score = (0 if mt.group(3) else 1, float(mt.group(1)), 0 if mt.group(2) else 1)
        if best is None or score > best[0]:
            best = (score, name)
    return best[1] if best else None


def pick_groq_model(ids):
    """A general chat model from Groq's model list."""
    ids = list(ids or [])
    for want in ("llama-3.3-70b-versatile", "llama-3.1-8b-instant",
                 "openai/gpt-oss-20b", "openai/gpt-oss-120b"):
        if want in ids:
            return want
    skip = re.compile(r"whisper|guard|tts|playai|embed|distil|safeguard|orpheus", re.I)
    for i in ids:
        if not skip.search(i):
            return i
    return None


# ----------------------------------------------------------------- networking

def http(method, url, headers=None, timeout=15):
    """Tiny stdlib HTTP helper. Returns (status, body); status is None on network failure."""
    req = urllib.request.Request(url, method=method,
                                 headers={"User-Agent": USER_AGENT, **(headers or {})})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, resp.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        try:
            body = e.read().decode("utf-8", "replace")
        except Exception:                                  # noqa: BLE001
            body = ""
        return e.code, body
    except (urllib.error.URLError, OSError, ValueError) as e:
        return None, re.sub(r"(?i)\b(key|token)=[^&\s]+", r"\1=***", str(e))


def _json(body):
    try:
        return json.loads(body)
    except ValueError:
        return {}


def test_gemini(key):
    """Returns (state, message, extra). state: ok | invalid | warn | network."""
    status, body = http("GET", "https://generativelanguage.googleapis.com/v1beta/models?pageSize=200",
                        {"x-goog-api-key": key})
    if status is None:
        return "network", f"could not reach Google ({body[:80]})", {}
    if status == 200:
        model = pick_gemini_model(_json(body).get("models", []))
        extra = {"GEMINI_MODEL": model} if model else {}
        return "ok", f"key accepted; model: {model or 'none auto-detected (tool will auto-detect later)'}", extra
    if status in (400, 401, 403):
        return "invalid", "Google rejected this key", {}
    if status == 429:
        return "warn", "key looks valid but the free-tier rate limit was hit just now", {}
    return "warn", f"unexpected response (HTTP {status})", {}


def test_groq(key):
    status, body = http("GET", "https://api.groq.com/openai/v1/models",
                        {"Authorization": f"Bearer {key}"})
    if status is None:
        return "network", f"could not reach Groq ({body[:80]})", {}
    if status == 200:
        ids = [m.get("id") for m in _json(body).get("data", []) if m.get("id")]
        model = pick_groq_model(ids)
        extra = {"GROQ_MODEL": model} if model else {}
        return "ok", f"key accepted; model: {model or 'none auto-detected (tool will auto-detect later)'}", extra
    if status == 401:
        return "invalid", "Groq rejected this key", {}
    if status == 403 and "1010" in body:
        return "warn", "request blocked by Groq's firewall (try another network); key not verified", {}
    if status == 429:
        return "warn", "key looks valid but the free-tier rate limit was hit just now", {}
    return "warn", f"unexpected response (HTTP {status})", {}


def test_opencellid(key):
    # getInAreaSize counts 2 of your 1,000 daily credits.
    url = ("https://opencellid.org/cell/getInAreaSize?key=" + urllib.parse.quote(key, safe="")
           + "&BBOX=-26.21,28.03,-26.20,28.04&format=json")
    status, body = http("GET", url)
    if status is None:
        return "network", f"could not reach OpenCellID ({body[:80]})", {}
    if status == 200:
        return "ok", "key accepted", {}
    if status == 401:
        return "invalid", "OpenCellID rejected this key", {}
    if status == 403:
        return "warn", "key is valid but not whitelisted for tower lookups (HTTP 403) - tower data will be skipped", {}
    if status == 429:
        return "ok", "key accepted (daily limit already used up)", {}
    return "warn", f"unexpected response (HTTP {status})", {}


TESTERS = {"gemini": test_gemini, "groq": test_groq, "opencellid": test_opencellid}


# --------------------------------------------------------------------- config

def load_config():
    try:
        with open(CONFIG_FILE, encoding="utf-8") as f:
            cfg = json.load(f)
        return cfg if isinstance(cfg, dict) else {}
    except FileNotFoundError:
        return {}
    except (OSError, ValueError) as e:
        print(yellow(f"[!] Could not read {CONFIG_FILE} ({e}) - starting with an empty config."))
        return {}


def save_config(cfg):
    """Atomic write; owner-only permissions where the OS supports them."""
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=str(CONFIG_DIR), prefix=".config-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(cfg, f, indent=2)
        try:
            os.chmod(tmp, 0o600)
        except OSError:
            pass
        os.replace(tmp, CONFIG_FILE)
    except Exception:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


def mask(key):
    if not key:
        return "(not set)"
    return f"{key[:4]}...{key[-4:]}" if len(key) >= 12 else "****"


def clean_key(raw, env):
    key = (raw or "").strip().strip("'\"").strip()
    key = re.sub(r"^(export\s+)?" + re.escape(env) + r"\s*=\s*", "", key).strip().strip("'\"")
    return key


def update_provider(cfg):
    """Keep AI_PROVIDER pointing at a provider that actually has a key."""
    have = [s for s in AI_SERVICES if cfg.get(SERVICES[s]["env"])]
    if not have:
        cfg.pop("AI_PROVIDER", None)
    elif cfg.get("AI_PROVIDER") not in have:
        cfg["AI_PROVIDER"] = have[0]


# ----------------------------------------------------------------------- flow

def ask_yes_no(prompt, default):
    hint = "[Y/n]" if default else "[y/N]"
    try:
        ans = input(f"{prompt} {hint} ").strip().lower()
    except EOFError:
        return default
    if not ans:
        return default
    return ans.startswith("y")


def print_service(svc, index=None, total=None):
    tag = f"[{index}/{total}] " if index else ""
    print("\n" + cyan("=" * 66))
    print(bold(f"{tag}{svc['name']}") + f" - {svc['purpose']}")
    print(green("COST: ") + svc["free"])
    print(bold("\nHow to get the key:"))
    for n, step in enumerate(svc["steps"], 1):
        print(f"  {n}. {step}")
    print(magenta("\n  >>> OPEN THIS PAGE: ") + bold(svc["url"]))
    print(yellow("\nNote: ") + svc["warning"])


def setup_service(sid, cfg, args, index, total):
    """Guide the user through one service. Returns True if the config changed."""
    svc = SERVICES[sid]
    env = svc["env"]
    print_service(svc, index, total)
    print()

    if cfg.get(env):
        if not ask_yes_no(f"{svc['name']} is already set up ({mask(cfg[env])}). Replace it?", False):
            return False
    elif not ask_yes_no(f"Set up {svc['name']} now?", svc["default_yes"]):
        print(yellow("  Skipped.") + f" Run 'python3 setup_apis.py --only {sid}' any time.")
        return False

    if not args.no_browser and ask_yes_no("Open that page in your browser now?", True):
        try:
            webbrowser.open(svc["url"])
        except Exception:                                  # noqa: BLE001
            print(yellow("  Could not open a browser - open the link above manually."))

    for attempt in range(1, 4):
        try:
            raw = getpass.getpass(f"Paste your {svc['name']} key (hidden; press Enter to skip): ")
        except EOFError:
            raw = ""
        key = clean_key(raw, env)
        if not key:
            print(yellow("  Skipped."))
            return False
        if re.search(r"\s", key):
            print(red("  That does not look like a single key (it contains spaces). Try again."))
            continue
        if svc["prefix"] and not key.startswith(svc["prefix"]):
            print(yellow(f"  Heads-up: {svc['name']} keys normally start with \"{svc['prefix']}\"."))

        extra = {}
        if not args.no_test:
            print("  Checking the key online...")
            state, msg, extra = TESTERS[sid](key)
            if state == "ok":
                print(green(f"  [OK] {msg}"))
            elif state == "warn":
                print(yellow(f"  [!] {msg}"))
            elif state == "network":
                print(yellow(f"  [!] {msg}. Saving it unverified."))
            else:
                print(red(f"  [X] {msg}."))
                choice = ""
                try:
                    choice = input("  [R]etry, [S]ave anyway, or [K]skip? [R] ").strip().lower()
                except EOFError:
                    pass
                if choice.startswith("k"):
                    return False
                if not choice.startswith("s"):
                    continue

        cfg[env] = key
        cfg.update(extra)
        update_provider(cfg)
        save_config(cfg)
        print(green(f"  Saved {svc['name']} key ({mask(key)}) to {CONFIG_FILE}"))
        return True

    print(yellow("  Too many attempts - skipped."))
    return False


def cmd_links():
    for i, sid in enumerate(ORDER, 1):
        print_service(SERVICES[sid], i, len(ORDER))
    print("\nNothing was changed. Run 'python3 setup_apis.py' to enter the keys.\n")


def cmd_status(args):
    cfg = load_config()
    print(bold("\nPhoneBookLOCA API status"))
    print(f"Config file: {CONFIG_FILE}\n")
    for sid in ORDER:
        svc = SERVICES[sid]
        env = svc["env"]
        if os.environ.get(env):
            key, source = os.environ[env], "environment variable"
        elif cfg.get(env):
            key, source = cfg[env], "saved config"
        else:
            print(f"  {svc['name']:<14} {red('not set')}   -> python3 setup_apis.py --only {sid}")
            continue
        line = f"  {svc['name']:<14} {green('set')}  {mask(key)}  ({source})"
        if not args.no_test:
            state, msg, _ = TESTERS[sid](key)
            colour = {"ok": green, "warn": yellow, "network": yellow, "invalid": red}[state]
            line += "  " + colour(f"{state.upper()}: {msg}")
        print(line)
    if cfg.get("AI_PROVIDER"):
        print(f"\n  Preferred AI provider: {cfg['AI_PROVIDER']}")
    print()


def cmd_reset(target):
    cfg = load_config()
    names = ORDER if target == "all" else [target]
    removed = []
    for sid in names:
        env = SERVICES[sid]["env"]
        if env in cfg:
            removed.append(SERVICES[sid]["name"])
    if not removed:
        print(yellow("Nothing to reset - no saved keys for that selection.\n"))
        return
    if not ask_yes_no(f"Forget the saved key(s) for: {', '.join(removed)}?", False):
        print("Cancelled.\n")
        return
    for sid in names:
        env = SERVICES[sid]["env"]
        cfg.pop(env, None)
        cfg.pop(env.replace("_API_KEY", "_MODEL"), None)
    update_provider(cfg)
    save_config(cfg)
    print(green("Done.") + " Remember to also delete/regenerate the key on the provider's page if it was exposed.\n")


def build_parser():
    p = argparse.ArgumentParser(description="PhoneBookLOCA free API setup wizard")
    p.add_argument("--links", action="store_true", help="print the links and steps only; change nothing")
    p.add_argument("--only", metavar="LIST", help="comma-separated: gemini, groq, opencellid")
    p.add_argument("--status", action="store_true", help="show what is configured (and test it)")
    p.add_argument("--reset", nargs="?", const="all", metavar="SERVICE",
                   help="forget a saved key: gemini, groq, opencellid or all")
    p.add_argument("--no-browser", action="store_true", help="never offer to open pages")
    p.add_argument("--no-test", action="store_true", help="do not check keys online")
    p.add_argument("--version", action="version", version=f"setup_apis {VERSION}")
    return p


def main(argv=None):
    args = build_parser().parse_args(argv)

    if args.links:
        cmd_links()
        return 0
    if args.status:
        cmd_status(args)
        return 0
    if args.reset is not None:
        if args.reset not in ORDER + ["all"]:
            print(red(f"Unknown service '{args.reset}'. Choose: {', '.join(ORDER)}, all"))
            return 2
        cmd_reset(args.reset)
        return 0

    chosen = ORDER
    if args.only:
        chosen = [s.strip().lower() for s in args.only.split(",") if s.strip()]
        bad = [s for s in chosen if s not in SERVICES]
        if bad:
            print(red(f"Unknown service(s): {', '.join(bad)}. Choose from: {', '.join(ORDER)}"))
            return 2

    print(cyan("\n" + "=" * 66))
    print(bold(f"  PhoneBookLOCA v{VERSION} - free API setup"))
    print(cyan("=" * 66))
    print("Every service below is FREE. For each one this wizard shows the exact page to")
    print("open and what to copy, then checks your key and saves it. Press Enter at any")
    print("key prompt to skip that service. Keys are typed hidden.")

    cfg = load_config()
    changed = []
    try:
        for i, sid in enumerate(chosen, 1):
            if setup_service(sid, cfg, args, i, len(chosen)):
                changed.append(SERVICES[sid]["name"])
    except KeyboardInterrupt:
        print(yellow("\n\nInterrupted - anything already saved is kept."))

    print("\n" + cyan("=" * 66))
    print(bold("Summary"))
    for sid in ORDER:
        env = SERVICES[sid]["env"]
        state = green("configured") if cfg.get(env) else yellow("not set")
        print(f"  {SERVICES[sid]['name']:<14} {state:<22} {mask(cfg.get(env)) if cfg.get(env) else ''}")
    if cfg.get("AI_PROVIDER"):
        print(f"  AI provider in use: {cfg['AI_PROVIDER']}")
    print(f"\nConfig file: {CONFIG_FILE}")
    print("Keys are stored as plain text there - never commit or share that file. If a key is")
    print("ever exposed, delete it on the provider's page (links above) and run this again.")
    if any(cfg.get(SERVICES[s]["env"]) for s in AI_SERVICES):
        print(green("\nTry it:  ./PhoneBookLOCA +27821234567 --ai"))
    print("Check anytime:  python3 setup_apis.py --status\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
