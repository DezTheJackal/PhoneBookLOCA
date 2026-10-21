# 📱 PhoneBookLOCA v2.3.1

<div align="center">

<img src="assets/logo.svg" alt="PhoneBookLOCA" width="600">

**Phone Number OSINT & Geolocation Intelligence Platform**

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![Platforms](https://img.shields.io/badge/platforms-Linux%20%7C%20macOS%20%7C%20Windows-brightgreen.svg)]()

*For educational, authorized security research, and law enforcement use only*

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [What's New](#-whats-new-in-v231)

</div>

-----

## 🎯 What is PhoneBookLOCA?

PhoneBookLOCA is a phone-number OSINT and geolocation-intelligence CLI. It resolves a number to carrier,
line type, and an approximate area-code-level location; layers on porting-likelihood scoring, historical
tracking, batch pattern analysis, and passive OSINT lead generation; and produces exportable reports for
investigative use. Everything is built on **public data** (libphonenumber, an optional free OpenCellID
key, and public web lookups) — it does not access carrier networks or provide real GPS tracking.

### Evolution Timeline

| Version | Key Features | Developer |
|---------|---------------|-----------|
| **v1.0** | Basic phone lookup, validation, carrier info | **DezTheJackal** |
| **v1.1** | OSINT web scanner (Go), API integration | 0xb0rn3 \| oxbv1 |
| **v2.0** | SQLite caching, batch analysis foundation | 0xb0rn3 \| oxbv1 |
| **v2.1** | Enhanced geolocation, LE case tracking | **DezTheJackal** |
| **v2.2** | Worldwide area-code database, porting detection | **DezTheJackal** |
| **v2.3** | Confidence/risk scoring, OSINT command wired to the Go scraper, CSV/HTML export, cross-platform (Windows/macOS), bug fixes | **DezTheJackal** |
| **v2.3.1** | OSINT upgrade: corrected lookup links, messaging-app checks, data-breach check with its own report files | **DezTheJackal** |

-----

## ✨ What's New in v2.3.1

Only the OSINT section changed — every command and flag works exactly as before (`--osint`, the
`osint <number>` command, and `--le-mode` all pick up the new behavior automatically).

- **More accurate links** — Truecaller now uses the ISO region (`/search/za/...`) instead of the calling
  code, Whitepages uses its dashed US format (and only appears for `+1` numbers), and dorks search the
  number in E.164, international *and* local formats at once. Each dork also gets a clickable Google link.
- **Messaging-app checks** — direct `wa.me`, `t.me` and `signal.me` links for the number.
- **Data-breach check — works with no API at all.** It runs inside OSINT and has two layers:
  1. **Offline (no API, no network):** searches breach files you already hold, in
     `~/.phonebookloca/breach_data/` (see below).
  2. **Online (optional):** with keys set it also queries
     [Have I Been Pwned](https://haveibeenpwned.com/API/v3) and
     [LeakCheck](https://wiki.leakcheck.io/en/api/api-v2-pro). Manual-lookup links (including an
     [Intelligence X](https://intelx.io/) deep link) are always shown.
- **Own output files** — if a breach is found (offline or online), `BREACH_<number>_<timestamp>.json` and
  `.html` are written to `~/.phonebookloca/reports/breach/`. Nothing is written when no breach is found.
  Only the source/file name, line number, date and the *names* of exposed fields are saved — never leaked
  passwords or other raw values.
- **Fix:** a cached plain lookup no longer hides `--geo` / `--osint` sections requested afterwards, and
  OSINT/breach results are always fetched live rather than served from cache.

### Offline breach check (no API needed)

Put breach/leak datasets you are authorised to hold into the breach folder — it is created automatically on
the first `--osint` run:

| OS | Default folder |
|---|---|
| Linux / macOS | `~/.phonebookloca/breach_data/` |
| Windows | `C:\Users\<you>\.phonebookloca\breach_data\` |

Override it with `PHONEBOOKLOCA_BREACH_DIR`. Supported: `.csv .tsv .txt .json .jsonl .sql .log` and
gzip-compressed versions (`.csv.gz`, …), including subfolders (up to 500 files).

- Every field of every line is reduced to its digits and compared with each common storage form of the
  number, so `+27 82 123 4567`, `082 123 4567`, `0027821234567` and `27821234567` all match, while a longer
  number that merely contains those digits does not.
- Result per file: **breached** (match found), **clean** (files scanned, no match) or **skipped** (folder
  empty — the output tells you where to put files).
- Hits are capped at 25 per file / 100 total (flagged "list truncated"). Very large datasets are scanned
  line by line, so multi-GB files take a while.
- The matching line is **never stored** — only file name, line number and CSV column names.
- Keep the folder outside the git repo (the repo's `.gitignore` also excludes `breach_data/` and `reports/`).

### Online breach check (optional, needs API keys)

```bash
# Linux/macOS
export HIBP_API_KEY="your_hibp_key"          # https://haveibeenpwned.com/API/Key (paid)
export LEAKCHECK_API_KEY="your_leakcheck_key" # LeakCheck account settings (paid)

# Windows (PowerShell)
$env:HIBP_API_KEY = "your_hibp_key"
$env:LEAKCHECK_API_KEY = "your_leakcheck_key"
```

Coverage notes: the offline check is only as good as the datasets you give it. HIBP only indexes phone numbers for a few breaches (notably the 2021 Facebook leak), so a
"clean" HIBP result is not proof a number was never exposed. A breach hit shows the number appeared in
leaked data — it does not by itself identify who uses the number.

### Earlier: v2.3.0

This release focuses on finishing features that were documented but never fully wired up, fixing real
bugs, and making the tool run cleanly on Windows and macOS, not just Linux.

### 🐛 Bug fixes
- Fixed a crash in `--le-mode` caused by a stray `returnPhoneBookLOCA` token (invalid Python).
- Fixed area-code geolocation silently failing for countries whose area codes aren't 3 digits (e.g. UK
  `020`) — it now tries the longest-to-shortest prefix match instead of assuming a fixed length.
- Fixed a first-run crash when `~/.phonebookloca` couldn't be created because its parent didn't exist yet.
- Replaced bare `except:` blocks with specific exception handling so real errors surface with `--verbose`
  instead of being silently swallowed.
- Removed the leftover duplicate "Quote Fix/Fixer" utility files (a workaround for a stale editing bug
  that no longer applies to this codebase).

### 🖥️ Cross-platform
- Colour output now renders correctly on legacy Windows consoles via `colorama` (previously ANSI codes
  only worked properly on Linux/macOS terminals).
- Added `install.ps1`, a native PowerShell installer for Windows (the existing `install.sh` only runs
  under WSL/Git Bash/Cygwin, not `cmd.exe`/native PowerShell).
- The Go scraper is now invoked cross-platform (`scraper` on Linux/macOS, `scraper.exe` on Windows) and is
  entirely optional — the tool works fully without it.

### 🔌 Previously-dormant features, now implemented
- **Confidence-scored porting detection** — VoIP type, MVNO carrier match, and historical carrier changes
  each contribute to a 0-100% confidence score with named indicators, instead of a bare true/false.
- **Confidence-scored geolocation precision** (`country` 30% / `area_code` 70% / `cell_tower` 90%), plus a
  generated Google Maps link when coordinates are available.
- **Risk-scored batch analysis** — clustering, same-carrier percentage, and VoIP ratio roll up into a
  0-100 risk score and Low/Medium/High rating, and the full report is now actually saved to disk
  (`batch_analysis_<timestamp>.json` or `--output <path>`), which the old batch command described but
  never wrote.
- **`osint` command / `--osint` flag** — generates Google dorks, public lookup-service URLs, and a breach
  reminder, and calls the previously-unused `scraper.go` binary automatically if it's been built.
- **Historical tracking surfaced in reports** — first/last seen, total lookups, and carrier-change
  detection, pulled from the `history` table that v2.2 populated but never displayed.
- **CSV and HTML export** alongside JSON for LE-mode reports (previously JSON-only despite being
  documented).
- **LE case metadata** — case type and priority are now captured and stored, not just case number/officer/
  agency.
- Area-code data moved out of the script and into `data/area_codes.json` so coverage can be extended
  without touching code — includes South African cities (Johannesburg, Cape Town, Durban, Pretoria, Port
  Elizabeth, Bloemfontein), which were missing entirely.

### 🎨 New
- Cyberpunk logo/wordmark (`assets/logo.svg`) and a square icon variant (`assets/icon.svg`) for use as a
  GitHub social-preview image or avatar.
- `push.sh` / `push.ps1` — commit-and-push helper scripts for maintaining the repo (see
  [Maintainer scripts](#-maintainer-scripts)).

-----

## 🎨 Features

| Category | Capabilities |
|---|---|
| **Core lookup** | Carrier, line type (mobile/VoIP/toll-free/etc.), timezone, validity — via Google's `libphonenumber` |
| **Geolocation** | Area-code-level location with confidence score; optional OpenCellID integration for real cell-tower data (±5km vs ±50km) |
| **Porting analysis** | Weighted confidence score from VoIP type, MVNO carrier match, and historical carrier changes |
| **Batch analysis** | Geographic clustering, carrier concentration, VoIP ratio, 0-100 risk score, auto-saved JSON report |
| **OSINT leads** | Multi-format Google dorks + links, lookup services, WhatsApp/Telegram/Signal links, data-breach check with report files, optional Go-based web scraper |
| **LE case mode** | Case tracking (number, officer, agency, type, priority), JSON/CSV/HTML report export |
| **History** | Every lookup is tracked; first/last seen and carrier-change detection surface automatically |
| **Caching** | SQLite-backed cache so repeat lookups are instant and offline-capable |

-----

## 🚀 Installation

### Linux / macOS

```bash
git clone https://github.com/DezTheJackal/PhoneBookLOCA.git
cd PhoneBookLOCA
pip3 install -r requirements.txt
chmod +x PhoneBookLOCA
./PhoneBookLOCA +14155552671
```

Or for a system-wide `phonebookloca` command:

```bash
sudo ./install.sh    # choose option 2
phonebookloca +14155552671
```

### Windows

```powershell
git clone https://github.com/DezTheJackal/PhoneBookLOCA.git
cd PhoneBookLOCA
powershell -ExecutionPolicy Bypass -File install.ps1
```

This installs dependencies, optionally builds the Go scraper if Go is present, and can add a
`phonebookloca` command to your PATH. Without the installer, run it directly:

```powershell
python PhoneBookLOCA +14155552671
```

### Requirements

```
phonenumbers>=8.12.0    # Core phone number parsing/geocoding/carrier lookup
requests>=2.25.0        # HTTP requests (OpenCellID)
rich>=13.0.0            # Enhanced terminal UI (optional, recommended)
colorama>=0.4.6         # Windows-only, for correct ANSI colors
```

### Optional: OpenCellID setup

Free registration at https://opencellid.org/ gives 1,000 requests/day of real cell-tower data:

```bash
# Linux/macOS
export OPENCELLID_API_KEY="your_key_here"

# Windows (PowerShell)
$env:OPENCELLID_API_KEY = "your_key_here"
```

### Optional: build the Go OSINT scraper

```bash
go build -o scraper scraper.go          # Linux/macOS
go build -o scraper.exe scraper.go      # Windows
```

Place the resulting binary next to `PhoneBookLOCA` (or on your `PATH`) and `--osint` / the `osint` command
will use it automatically. Without it, `--osint` still returns dorks and lookup URLs — you just don't get
the live web-scraper results.

-----

## 💡 Usage

```bash
# Basic lookup
./PhoneBookLOCA +14155552671

# Enhanced geolocation, porting, and history
./PhoneBookLOCA +14155552671 --geo

# Passive OSINT leads
./PhoneBookLOCA +14155552671 --osint

# Combine flags
./PhoneBookLOCA +14155552671 --geo --osint

# Batch analysis (writes a risk-scored JSON report)
./PhoneBookLOCA --batch numbers.txt

# Law enforcement case mode (prompts for case info, exports JSON/CSV/HTML)
./PhoneBookLOCA --le-mode

# Interactive mode
./PhoneBookLOCA
PhoneBook> +14155552671
PhoneBook> geo +14155552671
PhoneBook> osint +14155552671
PhoneBook> batch numbers.txt
PhoneBook> le-mode
PhoneBook> help
PhoneBook> quit
```

### Command-line options

| Flag | Description |
|---|---|
| `number` | Phone number in E.164 format, e.g. `+14155552671` |
| `--geo` | Enhanced geolocation, porting analysis, and history |
| `--osint` | Passive OSINT lead generation |
| `--le-mode` | Law enforcement case mode |
| `--batch FILE` | Batch-analyze numbers from a file (one per line) |
| `--no-cache` | Skip the local cache |
| `--output`, `-o FILE` | Save the result/report to this path |
| `--verbose`, `-v` | Verbose diagnostic logging (shows full tracebacks) |
| `--version` | Print the version and exit |

-----

## 🔧 Maintainer scripts

`push.sh` (Linux/macOS) and `push.ps1` (Windows) stage, commit, tag, and push a release to GitHub. They
run **your** git commands with **your** credentials — nothing in this repo can push on its own.

```bash
./push.sh "v2.3.0: dormant features, cross-platform, bug fixes"
```

```powershell
.\push.ps1 -Message "v2.3.0: dormant features, cross-platform, bug fixes"
```

Both scripts: confirm you're in a git repo, show `git status` before doing anything, stage all changes,
commit, offer to tag the release, and push. See the top of each file for details.

-----

## 🔒 Legal & Privacy

### ⚖️ What this tool does
- Estimates location from public area-code data
- Identifies likely VoIP/MVNO numbers and porting patterns
- Surfaces publicly documented carrier legal-compliance contacts
- Generates investigative leads and passive OSINT starting points

### ❌ What this tool does NOT do
- Provide real-time GPS tracking
- Access live carrier network/location data
- Bypass legal warrant/subpoena requirements
- Guarantee precise device location

### 📋 For real-time tracking or subscriber records

Law enforcement must go through proper legal process: obtain a court order/warrant or subpoena, contact
the carrier's legal compliance department, and request an emergency ping (life-threatening situations) or
CDR through that channel — see `data/carrier_contacts.json` for a starting list of public compliance
portals. This tool does not substitute for that process.

-----

## 🛠️ Troubleshooting

**Poor geolocation accuracy** — area-code data only maps to the location the number *block* was
originally assigned to, which is wrong if the number has been ported. Check `--geo`'s porting-confidence
score, and add missing coverage to `data/area_codes.json` (no code changes needed).

**OpenCellID not returning towers** — confirm `OPENCELLID_API_KEY` is set (`echo $OPENCELLID_API_KEY` /
`echo $env:OPENCELLID_API_KEY`) and that you have quota remaining (1,000/day on the free tier).

**Batch analysis shows no patterns** — pattern detection needs more than 5 valid numbers to trigger; with
fewer, an absence of flagged patterns is expected, not a bug.

**Database errors** — the cache is disposable:
```bash
rm ~/.phonebookloca/intel.db     # Linux/macOS
del %USERPROFILE%\.phonebookloca\intel.db   # Windows
./PhoneBookLOCA +14155552671     # rebuilds it
```

**Something crashed with a short error message** — re-run with `--verbose` for the full traceback before
filing an issue.

-----

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Update documentation (including this README if behavior changes)
5. Submit a pull request

Credit yourself in `CONTRIBUTORS.md`.

-----

## 📜 License

MIT License — see [LICENSE](LICENSE). Free to use, modify, and distribute with attribution.

-----

## 👥 Credits & Attribution

**DezTheJackal** — original concept (v1.0), LE geolocation (v2.1), worldwide database (v2.2), and the
v2.3 update (bug fixes, cross-platform support, dormant-feature implementation).

**0xb0rn3 | oxbv1** — v1.1 OSINT Go scanner and API integration, v2.0 caching/batch-analysis foundation.

-----

## 🔗 Links

- **Repository:** https://github.com/DezTheJackal/PhoneBookLOCA
- **Issues:** https://github.com/DezTheJackal/PhoneBookLOCA/issues
- **Releases:** https://github.com/DezTheJackal/PhoneBookLOCA/releases

-----

## ⚠️ Important Disclaimers

**Law enforcement:** this tool provides investigative leads from public data — geographic approximations,
not GPS. Real-time tracking or subscriber records require proper legal authorization.

**Security researchers:** authorized use only — penetration testing with permission, OSINT on public
information, and education are fine; unauthorized tracking, stalking, or harassment are not, and are
illegal in most jurisdictions.

-----

<div align="center">

**Created by DezTheJackal** · v1.1–v2.0 contributions by 0xb0rn3 | oxbv1

⚖️ Use responsibly. Follow legal procedures. Respect privacy.

**⭐ Star this repo if you find it useful ⭐**

</div>
