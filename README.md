# 📱 PhoneBookLOCA

<div align="center">

```ascii
╔═══════════════════════════════════════════════════════╗
║     PhoneBookLOCA v1.0 - OSINT Phone Lookup Tool      ║
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
- **Extracts** phone numbers from text files, logs, or leaked documents
- **Processes** bulk lists of numbers for large-scale reconnaissance
- **Exports** results in multiple formats for your reports

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

</td>
<td width="50%">

### 📊 Intelligence Gathered
- 🌍 Geographic location
- 📱 Carrier/provider info
- 🔢 Number type detection
- 🕐 Timezone mapping
- 🌐 Country & region codes
- 📝 Format variants

</td>
</tr>
</table>

---

## 🚀 Installation

### Quick Start

```bash
# Clone the repo
git clone https://github.com/DezTheJackal/PhoneBookLOCA.git
cd PhoneBookLOCA

# Install dependency
pip3 install phonenumbers

# Make it executable
chmod +x PhoneBookLOCA

# Run it
./PhoneBookLOCA
```

### Requirements

- Python 3.6 or higher
- `phonenumbers` library

That's it. No complicated setup, no BS.

---

## 💡 Usage

### Basic Lookup

The simplest way to use it:

```bash
./PhoneBookLOCA +14155552671
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

### Interactive Mode

Just run it without arguments for an interactive session:

```bash
./PhoneBookLOCA
```

Then start typing numbers. You get these commands:
- Type a number → Look it up
- `stats` → See what you've looked up this session
- `export` → Save your results
- `clear` → Clear the cache
- `help` → Show commands
- `quit` → Exit

### Batch Processing

Got a list of numbers? Process them all at once:

```bash
# Create a file with numbers (one per line)
cat > targets.txt << EOF
+14155552671
+442071838750
+33142869000
# You can add comments like this
+81312345678
EOF

# Process the batch
./PhoneBookLOCA -b targets.txt
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

### Scenario 2: Processing a Target List

```bash
./PhoneBookLOCA -b company_phones.txt -o intel.csv -f csv
```
*Great for when you have a list of employee numbers*

### Scenario 3: Mining Leaked Data

```bash
./PhoneBookLOCA --scan database_leak.sql -o found_numbers.txt
./PhoneBookLOCA -b found_numbers.txt -o analyzed.json
```
*Extract numbers from a breach, then analyze them all*

### Scenario 4: Session-Based Research

```bash
./PhoneBookLOCA
# Look up multiple numbers interactively
# Type 'stats' to see patterns
# Type 'export' to save everything
```
*Good for exploratory research where you're following leads*

---

## 🎨 Command Reference

```bash
# Basic usage
./PhoneBookLOCA <number>                    # Look up one number
./PhoneBookLOCA                             # Interactive mode

# Options
-v, --verbose                               # Show more details
-j, --json                                  # Output raw JSON
--variants                                  # Show format variants

# Batch processing  
-b FILE, --batch FILE                       # Process file of numbers
-o FILE, --output FILE                      # Save results
-f FORMAT, --format FORMAT                  # Output format (json/csv/txt)
--quiet                                     # No progress messages

# Text scanning
--scan FILE                                 # Extract numbers from text
-o FILE                                     # Save extracted numbers
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

### Export Formats

**JSON** - Machine-readable, perfect for automation
```json
{
  "timestamp": "2025-10-06T14:30:00",
  "input": "+14155552671",
  "valid": true,
  "country_name": "United States",
  "carrier": "Verizon Wireless",
  "type": "Mobile"
}
```

**CSV** - Spreadsheet-ready, great for analysis
```csv
timestamp,input,country_name,carrier,type
2025-10-06T14:30:00,+14155552671,United States,Verizon,Mobile
```

**TXT** - Human-readable reports
```
Target: +14155552671
Country: United States (+1)
Location: San Francisco, CA
Carrier: Verizon Wireless
Type: Mobile
```

---

## 🛠️ Use Cases

### Security Research
- Reconnaissance during penetration tests
- OSINT gathering on targets
- Validating contact information
- Geographic profiling

### Incident Response  
- Analyzing phone numbers from breach data
- Correlating numbers with threat intel
- Identifying attacker infrastructure

### Data Analysis
- Processing large contact databases
- Normalizing phone number formats
- Extracting numbers from unstructured data

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
EOF
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
./PhoneBookLOCA -b numbers.txt -o results.csv -f csv
```

---

## ⚠️ Important Notes

- **Country codes are required** - Use +1 for US, +44 for UK, etc.
- **International format works best** - E.164 format (+1234567890)
- **Rate limiting** - Be respectful, don't hammer the lookups
- **Legal use only** - This is for authorized security research and education

---

## 🤝 Contributing

Got ideas? Found a bug? Want to add features?

1. Fork the repo
2. Create your branch (`git checkout -b cool-feature`)
3. Make your changes
4. Test everything
5. Submit a pull request

I'm open to improvements!

---

## 📜 License

MIT License - See [LICENSE](LICENSE) file for details

---

## 👤 Author

**DezTheJackal**

If this tool helped you out, give it a ⭐ on GitHub!

---

<div align="center">

**🔒 Remember: Only use this for legal and authorized security research 🔒**

Made with 💀 for the security community

</div>
