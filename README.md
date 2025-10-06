# 📱 PhoneBookLOCA

<div align="center">

```ascii
╔═══════════════════════════════════════════════════════╗
║     PhoneBookLOCA v1.1 - OSINT Phone Lookup Tool      ║
║              Phone Number Intelligence                ║
╚═══════════════════════════════════════════════════════╝
```

**🔍 OSINT Tool for Phone Number Intelligence Gathering**

[![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-active-success.svg)]()

*For educational and authorized security research only*

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Examples](#-examples)

</div>

---

## 🎯 What is PhoneBookLOCA?

PhoneBookLOCA is a phone number OSINT tool built for security researchers and penetration testers. It helps you gather intelligence on phone numbers quickly and efficiently, whether you're working on a single target or processing hundreds of numbers from a breach dataset.

### What It Does

- **Validates** phone numbers and tells you if they're legit
- **Locates** where the number is registered (country, region, city)
- **Identifies** the carrier/network provider
- **Detects** number type (mobile, landline, VoIP, toll-free, etc.)
- **Generates** OSINT queries and search URLs automatically
- **Checks** reputation against spam/scam databases
- **Detects** VoIP and disposable numbers
- **Extracts** phone numbers from text files, logs, or leaked documents
- **Processes** bulk lists of numbers for large-scale reconnaissance
- **Exports** results in multiple formats for your reports
- **Integrates** with external APIs (NumVerify, Twilio)

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 🎯 Core Capabilities
- ✅ Single number lookups
- ✅ Batch file processing
- ✅ Interactive mode with commands
- ✅ Text scanning & extraction
- ✅ Multiple export formats
- ✅ Session statistics tracking
- ✅ VoIP/disposable detection
- ✅ API configuration system

</td>
<td width="50%">

### 📊 Intelligence Gathered
- 🌍 Geographic location
- 📱 Carrier/provider info
- 🔢 Number type detection
- 🕐 Timezone mapping
- 🌐 Country & region codes
- 📝 Format variants
- 🔍 OSINT query generation
- ⚠️ Reputation checking

</td>
</tr>
</table>

### 🆕 New in v1.1

- **OSINT Query Generator** - Auto-generate Google dorks and search queries
- **Lookup URL Generator** - Direct links to TrueCaller, Whitepages, etc.
- **Go-Powered Web Scanner** 🚀 - Concurrent web scraping for real OSINT results
- **VoIP Detection** - Identify virtual and disposable numbers
- **Reputation Checking** - Check against spam/scam databases
- **API Integration** - Support for NumVerify (free) and Twilio (paid)
- **Prompt-Based Configuration** - Easy API key setup through interactive prompts
- **Pattern Analysis** - Detect patterns in batch lookups

---

## 🚀 Installation

### Automated Installation (Recommended)

The installer supports **all Linux distros**, macOS, and Windows with automatic package manager detection.

```bash
# Clone the repo
git clone https://github.com/DezTheJackal/PhoneBookLOCA.git
cd PhoneBookLOCA

# Run the installer
chmod +x install.sh
./install.sh
```

**Choose your installation type:**
1. **Local installation** - Installs in current directory only
2. **System-wide installation** - Available globally from anywhere (`sudo` required)

The installer will:
- ✅ Auto-detect your OS and package manager
- ✅ Install Python/pip if missing (with permission)
- ✅ Install dependencies using global `requirements.txt`
- ✅ Automatically use `--break-system-packages` when needed
- ✅ Build the Go scraper (if Go is installed)
- ✅ Optionally install system-wide to `/usr/local/bin`
- ✅ Make everything executable and test it

**Supported Package Managers:**
- 📦 Arch Linux: `pacman`
- 📦 Ubuntu/Debian: `apt`
- 📦 Fedora: `dnf`
- 📦 RHEL/CentOS: `yum`
- 📦 OpenSUSE: `zypper`
- 📦 Alpine: `apk`
- 🍎 macOS: `brew` (for Go only, Python via system)
- 🪟 Windows: Git Bash/WSL

### System-Wide Installation

```bash
# Install globally (requires root)
sudo ./install.sh
# Choose option 2 when prompted

# Now use from anywhere
phonebookloca +14155552671
phonebookloca --osint +442071838750
```

Installs to:
- `/usr/local/bin/phonebookloca` - Main script
- `/usr/local/share/phonebookloca/` - Data directory (scraper binary)

### Manual Installation

If you prefer manual control:

```bash
# Clone the repo
git clone https://github.com/DezTheJackal/PhoneBookLOCA.git
cd PhoneBookLOCA

# Install Python dependencies (uses global requirements.txt)
pip3 install -r requirements.txt --break-system-packages

# Build Go scraper (optional but recommended)
go build -o scraper scraper.go

# Make executable
chmod +x PhoneBookLOCA

# Run locally
./PhoneBookLOCA

# OR install system-wide manually
sudo cp PhoneBookLOCA /usr/local/bin/phonebookloca
sudo mkdir -p /usr/local/share/phonebookloca
sudo cp scraper /usr/local/share/phonebookloca/
```

### Requirements

**Python (Required):**
- Python 3.6 or higher
- `phonenumbers` library
- `requests` library

**Go (Optional - for web scanner):**
- Go 1.16 or higher
- Required only for `--web-scan` feature

### Package Manager Auto-Install

The installer can automatically install missing dependencies on these distros:

| Distro | Package Manager | Auto-Install |
|--------|----------------|--------------|
| Arch Linux | pacman | ✅ |
| Ubuntu/Debian | apt | ✅ |
| Fedora | dnf | ✅ |
| RHEL/CentOS | yum | ✅ |
| OpenSUSE | zypper | ✅ |
| Alpine | apk | ✅ |
| macOS | - | Manual |
| Windows | - | Manual |

### Global requirements.txt

All dependencies are managed through the global `requirements.txt` in the root directory:
```
phonenumbers>=8.12.0
requests>=2.25.0
```

The installer automatically uses this file and handles `--break-system-packages` for you.

### Virtual Environment (Alternative)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
./PhoneBookLOCA
```

### Optional API Configuration

For additional features, you can configure API keys:

**Free APIs:**
- **NumVerify** - Get free API key at https://numverify.com/

**Paid APIs:**
- **Twilio Lookup** - Get credentials at https://www.twilio.com/

Configure via interactive prompt:
```bash
./PhoneBookLOCA --config
```

Or in interactive mode, type `config`.

---

## 💡 Usage

### Local Installation

If installed locally (in the git directory):

```bash
./PhoneBookLOCA +14155552671
```

### System-Wide Installation

If installed system-wide:

```bash
phonebookloca +14155552671
```

**All examples below work with both:**
- Local: `./PhoneBookLOCA [options]`
- System-wide: `phonebookloca [options]`

---

### Basic Lookup

The simplest way to use it:

```bash
phonebookloca +14155552671
```

**Output:**
```
[*] Target: +14155552671
[*] Initiating trace...

[+] Results:
    Country Code: +1
    Country: United States
    Region: US
    Location: San Francisco, CA
    Carrier: Verizon Wireless
    Type: Mobile
    Timezone(s): America/Los_Angeles
    Valid: Yes

[+] Trace Complete
```

### OSINT Mode

Generate reconnaissance queries and lookup URLs:

```bash
./PhoneBookLOCA +14155552671 --osint
```

**With Go-powered web scanning (FAST! 🚀):**
```bash
./PhoneBookLOCA +14155552671 --osint --web-scan
```

This launches concurrent checks across multiple platforms:
- Google (via dorks)
- Facebook
- LinkedIn  
- Twitter
- Instagram
- TrueCaller
- Pastebin dumps
- GitHub code search

**Output example:**
```
[*] Launching concurrent web scan (Go-powered)...
[*] This will check multiple sources simultaneously...

[✓] TrueCaller (0.85s)
[✓] Pastebin (1.23s)
[✗] Facebook (0.92s)
[✓] GitHub (1.45s)
[✗] LinkedIn (1.02s)
[✗] Twitter/X (0.78s)
[✗] Instagram (1.15s)
[✓] Google (0.65s)

[+] Scan complete: Found in 4/8 sources

[*] OSINT Web Scan Results:
    Scanned: 8 sources
    Found in: 4 platforms
    Failed: 4 sources

  Platforms where number was found:
    ✓ TrueCaller
    ✓ Pastebin
    ✓ GitHub
    ✓ Google
```

The Go scraper uses goroutines for concurrent execution - all 8 sources are checked simultaneously, completing in ~1-2 seconds total instead of 8-10 seconds sequentially! SpyDialer: https://www.spydialer.com/
```

Copy-paste these queries directly into Google or visit the URLs for more intel.

### Reputation Check

Check if a number is flagged as spam/scam:

```bash
./PhoneBookLOCA +14155552671 --reputation
```

### Interactive Mode

Just run it without arguments for an interactive session:

```bash
./PhoneBookLOCA
```

**Interactive Commands:**
```
PhoneBook> +14155552671              # Look up a number
PhoneBook> osint +14155552671        # OSINT mode for this number
PhoneBook> reputation +14155552671   # Check reputation
PhoneBook> stats                     # Show session statistics
PhoneBook> export                    # Export session results
PhoneBook> config                    # Configure API keys
PhoneBook> clear                     # Clear session cache
PhoneBook> help                      # Show all commands
PhoneBook> quit                      # Exit
```

### Batch Processing

Got a list of numbers? Process them all at once:

```bash
# Create a file with numbers (one per line)
cat > targets.txt << EOF
+14155552671
+442071838750
+33142869000
# Comments are supported
+81312345678
EOF

# Process the batch
./PhoneBookLOCA -b targets.txt

# With OSINT queries
./PhoneBookLOCA -b targets.txt --osint

# With reputation checking
./PhoneBookLOCA -b targets.txt --reputation
```

Want the results in a file?

```bash
# Save as JSON
./PhoneBookLOCA -b targets.txt -o results.json

# Save as CSV (great for Excel)
./PhoneBookLOCA -b targets.txt -o results.csv -f csv

# Save as plain text
./PhoneBookLOCA -b targets.txt -o results.txt -f txt
```

### Text Scanning

Found a leak with phone numbers scattered throughout? Extract them all:

```bash
# Scan any text file
./PhoneBookLOCA --scan leaked_data.txt

# Save the extracted numbers
./PhoneBookLOCA --scan leaked_data.txt -o extracted.txt
```

This will find every phone number in the file, no matter how it's formatted.

### Verbose Mode

Want more details?

```bash
./PhoneBookLOCA +14155552671 -v
```

This shows you all the different format variations of the number (E164, International, National, RFC3966).

### Format Variants

Need to see how else a number might be written?

```bash
./PhoneBookLOCA +14155552671 --variants
```

Shows you common ways that number might appear:
- `+14155552671`
- `14155552671`
- `(415) 555-2671`
- `415-555-2671`
- And more...

Useful for enumeration or finding alternate formats in data.

---

## 📖 Examples

### Scenario 1: Quick Single Lookup

```bash
./PhoneBookLOCA +14155552671
```
*Perfect for quickly checking one number during recon*

### Scenario 2: Full OSINT Reconnaissance

```bash
./PhoneBookLOCA +14155552671 --osint -v
```
*Get everything: location, carrier, OSINT queries, lookup URLs, format variants*

### Scenario 3: Processing a Target List

```bash
./PhoneBookLOCA -b company_phones.txt -o intel.csv -f csv --reputation
```
*Process employee numbers and check reputation*

### Scenario 4: Mining Leaked Data

```bash
./PhoneBookLOCA --scan database_leak.sql -o found_numbers.txt
./PhoneBookLOCA -b found_numbers.txt -o analyzed.json --osint
```
*Extract numbers from a breach, then do full OSINT on all of them*

### Scenario 5: Interactive Research Session

```bash
./PhoneBookLOCA
PhoneBook> config                    # Set up APIs
PhoneBook> osint +14155552671       # Look up with OSINT
PhoneBook> reputation +442071838750  # Check reputation
PhoneBook> stats                     # See patterns
PhoneBook> export                    # Save everything
```
*Good for exploratory research where you're following leads*

### Scenario 6: Automated Pipeline

```bash
# Extract, analyze, export in one go
./PhoneBookLOCA --scan dump.txt -o numbers.txt && \
./PhoneBookLOCA -b numbers.txt -o results.csv -f csv --osint --quiet
```
*Silent automation for scripts*

---

## 🎨 Command Reference

```bash
# Basic usage
./PhoneBookLOCA <number>                    # Look up one number
./PhoneBookLOCA                             # Interactive mode

# Lookup options
-v, --verbose                               # Show more details
-j, --json                                  # Output raw JSON
--variants                                  # Show format variants
--osint                                     # Generate OSINT queries
--reputation                                # Check reputation

# Batch processing  
-b FILE, --batch FILE                       # Process file of numbers
-o FILE, --output FILE                      # Save results
-f FORMAT, --format FORMAT                  # Output format (json/csv/txt)
--quiet                                     # No progress messages

# Text scanning
--scan FILE                                 # Extract numbers from text
-o FILE                                     # Save extracted numbers

# Configuration
--config                                    # Configure API keys
```

---

## 📊 What You Get

Every lookup gives you:

| Field | Description | Example |
|-------|-------------|---------|
| **Country Code** | International dialing code | +1, +44, +33 |
| **Country Name** | Full country name | United States |
| **Region Code** | ISO region code | US, GB, FR |
| **Location** | City/state/province | San Francisco, CA |
| **Carrier** | Network provider | Verizon Wireless |
| **Type** | Number classification | Mobile, Landline, VoIP |
| **Timezone(s)** | Associated time zones | America/Los_Angeles |
| **Valid** | Whether the number is real | Yes/No |
| **VoIP Status** | Virtual/disposable detection | Yes/No |

### OSINT Mode Output

When using `--osint`, you also get:

**Google Dorks** - Ready-to-search queries for:
- Social media platforms (Facebook, LinkedIn, Twitter, Instagram)
- Paste sites (Pastebin, Ghostbin)
- General web mentions
- Email associations

**Lookup URLs** - Direct links to:
- TrueCaller
- Whitepages
- WhoCalledMe
- SpyDialer
- NumLookup
- Sync.me

### API Integration Results

With configured APIs, you get additional data:

**NumVerify (Free)**
- Enhanced carrier information
- Line type details
- Country validation

**Twilio (Paid)**
- Carrier name and type
- National format
- Enhanced validation

### Export Formats

**JSON** - Machine-readable, perfect for automation
```json
{
  "timestamp": "2025-10-06T14:30:00",
  "input": "+14155552671",
  "valid": true,
  "country_name": "United States",
  "carrier": "Verizon Wireless",
  "type": "Mobile",
  "voip_check": {
    "is_voip": false,
    "likely_disposable": false
  },
  "osint_queries": {
    "google_dorks": ["..."],
    "lookup_urls": {"..."}
  }
}
```

**CSV** - Spreadsheet-ready, great for analysis
```csv
timestamp,input,country_name,carrier,type,is_voip
2025-10-06T14:30:00,+14155552671,United States,Verizon,Mobile,False
```

**TXT** - Human-readable reports
```
Target: +14155552671
Country: United States (+1)
Location: San Francisco, CA
Carrier: Verizon Wireless
Type: Mobile
VoIP: No
```

---

## 🛠️ Use Cases

### Security Research
- Reconnaissance during penetration tests
- OSINT gathering on targets
- Validating contact information
- Geographic profiling
- VoIP/disposable number detection

### Incident Response  
- Analyzing phone numbers from breach data
- Correlating numbers with threat intel
- Identifying attacker infrastructure
- Checking reputation of suspicious numbers

### Data Analysis
- Processing large contact databases
- Normalizing phone number formats
- Extracting numbers from unstructured data
- Pattern detection in number lists

### Social Engineering
- Carrier identification for SMS attacks
- Geographic context for pretexting
- Format variants for enumeration
- OSINT query generation for profile building

---

## 🎓 Tips & Tricks

### Batch File Tips

```bash
# Use comments to organize your targets
cat > targets.txt << EOF
# Sales Team
+14155551234
+14155555678

# Support Team  
+14155559876

# Executives
+14155550001
EOF
```

### OSINT Workflow

```bash
# Full recon on a number
./PhoneBookLOCA +14155552671 --osint -v > recon.txt

# Then use the generated queries in your browser
# Copy-paste the Google dorks
# Visit the lookup URLs
```

### Quiet Mode for Scripts

```bash
# Run silently for automation
./PhoneBookLOCA -b huge_list.txt -o results.json --quiet
```

### Chain Commands

```bash
# Extract, then analyze
./PhoneBookLOCA --scan dump.txt -o numbers.txt && \
./PhoneBookLOCA -b numbers.txt -o results.csv -f csv --osint
```

### Interactive Mode Productivity

```bash
# Set up once, use throughout session
PhoneBook> config                    # Configure APIs first
PhoneBook> osint +1234567890        # Quick OSINT
PhoneBook> reputation +9876543210   # Quick reputation check
PhoneBook> stats                     # See what you've found
PhoneBook> export                    # Save before quitting
```

### API Key Storage

API keys are stored in `~/.phonebookloca_config.json`. They persist across sessions, so you only need to configure once.

---

## 🔌 API Integration

### NumVerify (Free Tier)

1. Sign up at https://numverify.com/
2. Get your free API key (100 requests/month)
3. Configure in PhoneBookLOCA:
```bash
./PhoneBookLOCA --config
# Choose option 1, enter your key
```

### Twilio Lookup (Paid)

1. Sign up at https://www.twilio.com/
2. Get your Account SID and Auth Token
3. Configure in PhoneBookLOCA:
```bash
./PhoneBookLOCA --config
# Choose option 2, enter your credentials
```

**Pricing:** ~$0.005 per lookup (very cheap for professional use)

---

## 📁 Project Structure

```
PhoneBookLOCA/
├── PhoneBookLOCA           # Main Python script (DezTheJackal + 0xb0rn3)
├── scraper.go              # Go web scraper (maintained by 0xb0rn3 | oxbv1)
├── scraper                 # Compiled Go binary (created by install.sh)
├── install.sh              # Multi-platform installer (maintained by 0xb0rn3 | oxbv1)
├── requirements.txt        # Python dependencies
├── README.md               # This file
├── CONTRIBUTORS.md         # Credits and contributions
├── LICENSE                 # MIT License (DezTheJackal)
└── .phonebookloca_config.json  # API config (created at runtime)
```

---

## ⚠️ Important Notes

- **Country codes are required** - Use +1 for US, +44 for UK, etc.
- **International format works best** - E.164 format (+1234567890)
- **Rate limiting** - Be respectful, don't hammer the lookups
- **API limits** - Free tiers have request limits
- **Legal use only** - This is for authorized security research and education
- **Config file** - API keys stored in `~/.phonebookloca_config.json`

---

## 🤝 Contributing

Got ideas? Found a bug? Want to add features?

1. Fork the repo
2. Create your branch (`git checkout -b cool-feature`)
3. Make your changes
4. Test everything
5. Submit a pull request

All contributions welcome!

---

## 📜 License

MIT License - See [LICENSE](LICENSE) file for details

---

## 👤 Author

**DezTheJackal**

Original creator and maintainer of PhoneBookLOCA.

If this tool helped you out, give it a ⭐ on GitHub!

---

## 🙏 Contributors

Special thanks to the following contributors who have added features to make this tool more powerful for the community:

- **0xb0rn3 (0xbv1)** - v1.1 OSINT features, Go-powered web scanner, API integrations, batch processing enhancements

Want to contribute? Check out the [Contributing](#-contributing) section!

---

<div align="center">

**🔒 Remember: Only use this for legal and authorized security research 🔒**

Made with 💀 by DezTheJackal for the security community

</div>
