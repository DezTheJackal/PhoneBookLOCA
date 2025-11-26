# 📱 PhoneBookLOCA v2.1

<div align="center">

```ascii
╔═══════════════════════════════════════════════════════════════╗
║     PhoneBookLOCA v2.1 - Professional OSINT Platform          ║
║     Law Enforcement Edition with Enhanced Geolocation         ║
╚═══════════════════════════════════════════════════════════════╝
```

**🔍 Professional-Grade OSINT Intelligence Platform**

[![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-active-success.svg)]()

*For educational, authorized security research, and law enforcement use only*

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Law Enforcement](#-law-enforcement-mode)

</div>

---

## 🎯 What is PhoneBookLOCA v2.1?

PhoneBookLOCA v2.1 is a **professional-grade OSINT intelligence platform** for phone number reconnaissance with **enhanced geolocation capabilities** designed for law enforcement and missing persons investigations. Created by DezTheJackal, with continuous enhancements from the community.

### Version History

| Version | Features | Developed By |
|---------|----------|--------------|
| **v1.0** | Basic phone lookup, validation, carrier info | **DezTheJackal** |
| **v1.1** | OSINT queries, web scanning, API integration | 0xb0rn3 \| oxbv1 |
| **v2.0** | SQLite caching, reputation engine, ML classification | 0xb0rn3 \| oxbv1 |
| **v2.1** | 🚨 **Enhanced geolocation, LE tools, missing persons features** | **DezTheJackal** |

---

## ✨ What's New in v2.1

### 🚨 Law Enforcement Features (Added by DezTheJackal)

#### 1. **Enhanced Geolocation System**
- **Maximum legal precision** location intelligence
- **Area code + Exchange mapping** (±5-50 km accuracy)
- **Cell tower proximity analysis** with distance calculations
- **Geographic coordinate estimation** with confidence scoring
- **Multi-source data aggregation** for best accuracy

```bash
# Enhanced geolocation lookup
./PhoneBookLOCA +14155552671 --geo

# Output includes:
📍 Enhanced Geolocation
Precision: exchange (±5 km)
Confidence: 80%
Coordinates: 37.774929, -122.419418
City: San Francisco
County: San Francisco
State: CA
```

#### 2. **Law Enforcement Investigation Interface**
- **Interactive LE mode** for case management
- **Case tracking system** with SQLite database
- **Professional report generation** (JSON, CSV, HTML)
- **Carrier legal compliance contacts** built-in database
- **Investigative lead generation** with actionable recommendations

```bash
# Law enforcement mode
./PhoneBookLOCA --le-mode

🚨 LAW ENFORCEMENT MODE
Case Number: MP-2025-001
Officer Name: Det. Smith
Agency: SFPD
```

#### 3. **Professional Report Exports**
- **JSON format** - Machine-readable for systems integration
- **CSV format** - Spreadsheet import for case files
- **HTML format** - Professional formatted reports with legal disclaimers
- **Automatic timestamps** and case tracking
- **Browser integration** for HTML reports

#### 4. **Cell Tower Analysis**
- **Nearby tower identification** from public databases
- **Distance calculations** using Haversine formula
- **Technology detection** (5G, LTE, 4G, 3G)
- **Carrier infrastructure mapping**
- **Coverage area estimation**

#### 5. **Legal Compliance Framework**
- **Clear data limitations** in all reports
- **Warrant guidance** for real-time tracking
- **Carrier contact information** for legal requests
- **Emergency ping procedures** documentation
- **Legal disclaimer system** in all exports

---

## 🎨 Complete Feature Set

### Core Intelligence Capabilities

<table>
<tr>
<td width="50%">

### 🎯 Basic Intelligence
- ✅ Phone number validation
- ✅ Geographic location (country, region, city)
- ✅ Carrier/provider identification
- ✅ Number type detection (mobile, landline, VoIP)
- ✅ Timezone mapping
- ✅ Format variants generation
- ✅ Carrier intelligence
- ✅ Risk classification

</td>
<td width="50%">

### 🚨 v2.1 Law Enforcement (NEW)
- ✅ **Enhanced geolocation (±5-50 km)**
- ✅ **Case tracking & management**
- ✅ **Professional report exports**
- ✅ **Cell tower proximity analysis**
- ✅ **Carrier legal contact database**
- ✅ **Missing persons investigation tools**
- ✅ **Legal compliance framework**
- ✅ **Investigative lead generation**

</td>
</tr>
</table>

### Advanced Analysis (v2.0)

- ✅ **SQLite caching** - Instant lookups (<1s vs 5-10s)
- ✅ **Reputation scoring** - Multi-source aggregation (0-100 scale)
- ✅ **Spam/scam detection** - Community reports analysis
- ✅ **ML-powered classification** - Risk assessment algorithms
- ✅ **VoIP/disposable detection** - Service type identification
- ✅ **Rich terminal UI** - Beautiful formatting (optional)

### OSINT Capabilities (v1.1)

- ✅ **OSINT query generation** - Google dorks, social media
- ✅ **Web scanning** - Concurrent Go-powered scraper
- ✅ **Lookup URL generation** - TrueCaller, Whitepages, etc.
- ✅ **API integration** - NumVerify, Twilio support
- ✅ **Batch processing** - Multiple number analysis
- ✅ **Export formats** - JSON, CSV, TXT

---

## 🚀 Installation

### Quick Start with Installer

```bash
# Clone the repository
git clone https://github.com/DezTheJackal/PhoneBookLOCA.git
cd PhoneBookLOCA

# Run the automated installer
chmod +x install.sh
./install.sh
```

### Manual Installation

```bash
# Install dependencies
pip3 install -r requirements.txt

# Make executable
chmod +x PhoneBookLOCA

# Run
./PhoneBookLOCA
```

### Requirements

**Python Dependencies:**
```
phonenumbers>=8.12.0    # Core phone number functionality
requests>=2.25.0        # HTTP requests
rich>=13.0.0            # Optional - Enhanced terminal UI
```

**System Requirements:**
- Python 3.6+
- SQLite3 (usually pre-installed)
- Go 1.16+ (optional, for web scanner)

---

## 💡 Usage

### Basic Lookup

```bash
# Standard lookup
./PhoneBookLOCA +14155552671

# Output:
📊 Basic Intelligence
Country: United States (+1)
Carrier: Verizon Wireless
Type: Mobile
Timezone(s): America/Los_Angeles
```

### Enhanced Geolocation (v2.1)

```bash
# Maximum precision geolocation
./PhoneBookLOCA +14155552671 --geo

# Output includes:
📍 Enhanced Geolocation
Precision Level: exchange
Confidence: 80%
Accuracy Radius: ±5 km

Coordinates:
  Latitude: 37.774929
  Longitude: -122.419418

Location:
  City: San Francisco
  County: San Francisco
  State: CA
  Country: US

📡 Nearby Cell Towers: 3 found
Primary Tower:
  • ID: tower_sf_001
  • Distance: 2.3 km
  • Range: 5 km
  • Technology: 5G, LTE

⚖️ Legal Notice:
Public data only - For real-time tracking, obtain legal warrant
```

### Interactive Mode

```bash
./PhoneBookLOCA

PhoneBook> +14155552671              # Standard lookup
PhoneBook> geo +14155552671          # Enhanced geolocation
PhoneBook> le-mode                   # Law enforcement mode
PhoneBook> help                      # Show commands
PhoneBook> quit                      # Exit
```

---

## 🚨 Law Enforcement Mode

### Accessing LE Mode

```bash
# Command line
./PhoneBookLOCA --le-mode

# Or from interactive mode
PhoneBook> le-mode
```

### LE Mode Workflow

```
🚨 LAW ENFORCEMENT MODE
Enhanced Geolocation for Missing Persons Investigations

1. Enter Case Information
   ├─ Case Number: MP-2025-001
   ├─ Officer Name: Det. John Smith
   ├─ Agency: San Francisco Police Department
   ├─ Case Type: missing person
   └─ Priority: high

2. Subject Phone Number
   └─ +14155552671

3. Automated Analysis
   ├─ Enhanced geolocation lookup
   ├─ Cell tower proximity analysis
   ├─ Carrier legal contact retrieval
   └─ Investigative lead generation

4. Report Export
   ├─ JSON (machine-readable)
   ├─ CSV (spreadsheet)
   └─ HTML (formatted report)
```

### Case Tracking

All LE cases are tracked in the database:

```
~/.phonebookloca/intel.db
  └─ le_cases table
     ├─ case_id
     ├─ case_number
     ├─ officer_name
     ├─ agency
     ├─ created_date
     └─ status
```

### Report Contents

#### JSON Report
```json
{
  "case_information": {
    "case_number": "MP-2025-001",
    "requesting_officer": "Det. John Smith",
    "agency": "SFPD",
    "report_generated": "2025-01-15T14:30:00"
  },
  "legal_disclaimer": {
    "notice": "Public data only",
    "limitations": [...],
    "legal_requirements": [...]
  },
  "subject_information": {
    "phone_number": "+14155552671",
    "carrier": "Verizon Wireless",
    "is_valid": true
  },
  "geolocation_intelligence": {
    "precision_level": "exchange",
    "confidence": 0.8,
    "coordinates": {
      "latitude": 37.774929,
      "longitude": -122.419418
    },
    "radius_km": 5.0,
    "address": {...}
  },
  "carrier_contacts": {
    "legal_compliance": "1-800-451-5242",
    "emergency_24_7": "1-888-483-7200",
    "email": "lawenforcement@verizonwireless.com"
  },
  "recommendations": {...}
}
```

#### HTML Report Features
- Professional formatting
- Legal disclaimers prominently displayed
- Interactive map links
- Carrier contact information
- Investigative recommendations
- Browser-ready for printing/sharing

---

## 📊 Geolocation Precision Levels

| Precision Level | Accuracy | Confidence | Use Case |
|----------------|----------|------------|----------|
| **Exchange** | ±5 km | 70-85% | Best precision without warrant |
| **Area Code** | ±50 km | 50-70% | Regional approximation |
| **Cell Tower** | ±10 km | 65-80% | When tower data available |
| **City** | ±25 km | 60-75% | General metropolitan area |

### Data Sources Used

1. **Area Code Database** - US/Canada NANP mapping
2. **Exchange Mapping** - NPA-NXX to geographic assignment
3. **Cell Tower Database** - Public infrastructure data
4. **Carrier Assignment** - MNO/MVNO identification
5. **PhoneNumbers Library** - Google's libphonenumber

---

## 🔒 Legal & Privacy

### ⚖️ Legal Notice

**PhoneBookLOCA v2.1 provides APPROXIMATE location intelligence based on PUBLIC data sources.**

#### What This Tool DOES:
✅ Estimates location based on area code/exchange  
✅ Identifies nearby cell towers (public data)  
✅ Provides carrier legal contact information  
✅ Generates investigative leads  
✅ Creates professional reports for documentation  

#### What This Tool DOES NOT Do:
❌ Provide real-time GPS tracking  
❌ Access live carrier location data  
❌ Bypass legal requirements for warrants  
❌ Guarantee precise device location  
❌ Replace proper legal channels  

### 📋 Legal Requirements for Real-Time Tracking

For **precise, real-time location** of a device, law enforcement MUST:

1. **Obtain Legal Authorization**
   - Court order / Search warrant
   - Exigent circumstances documentation
   - Emergency ping authorization (life-threatening)

2. **Contact Carrier Legal Compliance**
   - Use provided emergency numbers
   - Submit proper legal documentation
   - Request real-time location or CDR

3. **Follow Proper Procedures**
   - 18 U.S.C. § 2703 compliance
   - State-specific requirements
   - Chain of custody documentation

### 🚨 Emergency Situations

For **immediate life-threatening situations**:

1. Contact carrier emergency line (24/7)
2. Provide case details and authorization
3. Request emergency ping
4. Follow up with legal documentation

**Emergency Contact Numbers (Built-in):**
- **Verizon:** 1-888-483-7200
- **AT&T:** 1-800-635-6840
- **T-Mobile:** 1-888-987-4500

### 📁 Data Storage

PhoneBookLOCA stores data locally:

```
~/.phonebookloca/
├── intel.db              # Main cache database
│   ├── lookups           # Lookup history
│   ├── area_code_mapping # Geographic data
│   ├── cell_towers       # Public tower data
│   └── le_cases          # LE case tracking
└── reports/              # Exported reports
    ├── LE_Report_*.json
    ├── LE_Report_*.csv
    └── LE_Report_*.html
```

**Privacy:**
- All data stored locally (no cloud sync)
- No telemetry or analytics
- Database encrypted at OS level
- Case data confidential

---

## 📖 Command Reference

### Command Line Options

```bash
# Standard lookup
./PhoneBookLOCA +14155552671

# Enhanced geolocation
./PhoneBookLOCA +14155552671 --geo

# Law enforcement mode
./PhoneBookLOCA --le-mode

# Disable cache (force fresh lookup)
./PhoneBookLOCA +14155552671 --no-cache

# Cache management
./PhoneBookLOCA --cache-stats
./PhoneBookLOCA --clear-cache [days]

# Interactive mode (default)
./PhoneBookLOCA
```

### Interactive Commands

```
PhoneBook> <number>           # Standard lookup
PhoneBook> geo <number>       # Enhanced geolocation
PhoneBook> le-mode            # Law enforcement mode
PhoneBook> cache              # Show cache stats
PhoneBook> clear-cache [days] # Clear old cache
PhoneBook> help               # Show help
PhoneBook> quit               # Exit
```

### LE Mode Commands

```
Within LE Mode:
1. Enter case information
2. Provide subject phone number
3. Automatic enhanced lookup
4. Choose export format:
   - 1) JSON
   - 2) CSV
   - 3) HTML
   - 4) All formats
   - 5) Skip export
```

---

## 🎯 Use Cases

### 🚨 Law Enforcement (v2.1 Primary Focus)

#### Missing Persons Investigations
- **Initial location approximation** for deployment planning
- **Case documentation** with professional reports
- **Legal contact information** for carrier requests
- **Search area estimation** based on precision/confidence
- **Investigative lead generation** for follow-up actions

#### Cold Case Review
- **Historical number analysis** with caching
- **Carrier change tracking** (porting history)
- **Geographic pattern analysis** across multiple numbers
- **Report generation** for case files

#### Emergency Response
- **Quick approximation** while warrant processes
- **Carrier emergency contacts** readily available
- **Search radius calculation** for resource deployment
- **Documentation** for legal proceedings

### 🔍 Security Research

#### OSINT Gathering
- **Target reconnaissance** during penetration tests
- **Social engineering** assessment
- **Attack surface** mapping
- **Threat intelligence** correlation

#### Fraud Investigation
- **Disposable number detection**
- **VoIP identification**
- **Carrier reputation analysis**
- **Pattern detection** across datasets

### 📊 Data Analysis

#### Large-Scale Processing
- **Batch analysis** with caching (10x faster)
- **Risk scoring** for contact lists
- **Geographic distribution** analysis
- **Carrier assignment** patterns

---

## 🛠️ Advanced Configuration

### Area Code Database Expansion

Add custom area codes to improve precision:

```python
# In the EnhancedGeolocation class, add to area_codes list:
area_codes = [
    ('XXX', 'YYY', 'City', 'State', 'County', lat, lon, pop, 'Timezone'),
    # Add your entries here
]
```

### Cell Tower Database

Add local cell towers for better accuracy:

```python
# Add to towers list:
towers = [
    ('tower_id', 'Carrier', lat, lon, range_km, 'Technology', 'Area', 'City', 'State'),
    # Add your towers here
]
```

### Custom Carrier Contacts

Add additional carriers:

```python
# In _get_carrier_contacts():
contacts = {
    'Your Carrier': {
        'legal_compliance': '1-800-XXX-XXXX',
        'emergency_24_7': '1-888-XXX-XXXX',
        'email': 'legal@carrier.com'
    }
}
```

---

## 📈 Performance

### Lookup Speed

| Operation | v1.1 | v2.0 | v2.1 |
|-----------|------|------|------|
| Standard lookup | 5-10s | <1s (cached) | <1s (cached) |
| Enhanced geo | N/A | N/A | 1-3s (first) / <1s (cached) |
| LE report generation | N/A | N/A | 2-5s |
| 100 lookups | 8-16min | 1-2min | 1-2min |

### Cache Performance

- **Hit rate:** 60-95% (depending on use case)
- **Storage:** ~1-5 MB per 1000 entries
- **Freshness:** Configurable (default: 7 days for geo)

---

## 🔧 Troubleshooting

### Common Issues

#### "Module not found" Error

```bash
# Install missing dependencies
pip3 install phonenumbers requests rich
```

#### Cache Not Working

```bash
# Check cache database
ls -la ~/.phonebookloca/intel.db

# Fix permissions
chmod 755 ~/.phonebookloca
chmod 644 ~/.phonebookloca/intel.db

# Clear and rebuild
rm ~/.phonebookloca/intel.db
./PhoneBookLOCA +14155552671
```

#### Poor Geolocation Accuracy

**Possible causes:**
- Number ported from different area
- VoIP number (no geographic tie)
- Limited area code data
- International number (US data focused)

**Solutions:**
- Use `--no-cache` for fresh lookup
- Contact carrier for accurate data
- Obtain warrant for real-time location

#### LE Reports Not Generating

```bash
# Check reports directory
mkdir -p ~/.phonebookloca/reports
chmod 755 ~/.phonebookloca/reports

# Verify write permissions
touch ~/.phonebookloca/reports/test.txt
```

---

## 🤝 Contributing

Want to improve PhoneBookLOCA?

1. **Fork** the repository
2. **Create** feature branch: `git checkout -b feature-name`
3. **Make** your changes
4. **Credit** original authors in file headers
5. **Update** CONTRIBUTORS.md
6. **Submit** pull request

### Contribution Guidelines

- Maintain backwards compatibility
- Follow existing code style
- Test on multiple platforms
- Update documentation
- Add yourself to contributors list

### Areas for Contribution

- Additional area code mappings
- International carrier databases
- Enhanced cell tower data
- Additional export formats
- UI/UX improvements
- Performance optimizations

---

## 📜 License

MIT License - See [LICENSE](LICENSE) file

**Summary:** Free to use, modify, and distribute with attribution.

---

## 👥 Credits & Attribution

### Original Creator
**DezTheJackal** - Creator and maintainer of PhoneBookLOCA
- Original concept and v1.0 implementation
- v2.1 Law Enforcement Geolocation features
- Enhanced geolocation system
- LE investigation interface
- Professional report generation
- Case tracking system
- Cell tower analysis
- Missing persons investigation tools

### Major Contributors

**0xb0rn3 | oxbv1** - v1.1 & v2.0 Enhancements
- Go-powered web scanner (v1.1)
- OSINT query generation (v1.1)
- API integration framework (v1.1)
- Multi-platform installer (v1.1)
- SQLite caching system (v2.0)
- Reputation engine (v2.0)
- ML-powered classification (v2.0)
- Rich terminal UI (v2.0)
- Performance optimizations (v2.0)

---

## 🔗 Links

- **GitHub Repository:** https://github.com/DezTheJackal/PhoneBookLOCA
- **Report Issues:** https://github.com/DezTheJackal/PhoneBookLOCA/issues
- **Documentation:** This README + inline code comments

---

## ⚠️ Important Disclaimers

### For Law Enforcement

This tool provides **investigative leads** and **approximate location intelligence**. It:
- Uses publicly available data sources
- Provides geographic approximations (not GPS)
- Requires legal authorization for real-time tracking
- Should supplement, not replace, proper legal procedures

**Always follow proper legal channels for accurate location data.**

### For Security Researchers

This tool is for:
- ✅ Authorized security research
- ✅ Penetration testing with permission
- ✅ Educational purposes
- ✅ OSINT gathering on public information

This tool is NOT for:
- ❌ Illegal tracking or stalking
- ❌ Privacy violations
- ❌ Harassment
- ❌ Unauthorized surveillance

### For General Users

- This tool respects privacy and legal boundaries
- Enhanced geolocation uses only public data
- Real-time tracking requires legal authorization
- Use responsibly and ethically

---

## 📞 Support

### Getting Help

1. **Read the documentation** (this README)
2. **Check issues** for similar problems
3. **Create issue** with details:
   - PhoneBookLOCA version
   - Operating system
   - Error message
   - Steps to reproduce

### Feature Requests

We welcome feature requests! Please:
1. Search existing issues first
2. Describe the use case
3. Explain expected behavior
4. Consider contributing the feature

---

<div align="center">

## 🚨 For Law Enforcement & Missing Persons Investigations 🚨

**PhoneBookLOCA v2.1 - Professional OSINT Intelligence Platform**

*Enhanced Geolocation | Case Tracking | Professional Reports*

**Created by: DezTheJackal**

v1.0: DezTheJAckal | v1.1-v2.0: 0xb0rn3 | oxbv1 | v2.1 LE Features: DezTheJackal

⚖️ **Use responsibly. Follow legal procedures. Respect privacy.**

</div>

---

## 📝 Version History

### v2.1 - 2025 (Current)
- 🚨 **Law enforcement investigation interface** (DezTheJackal)
- 📍 **Enhanced geolocation system** (DezTheJackal)
- 📊 **Professional report exports** (DezTheJackal)
- 📡 **Cell tower proximity analysis** (DezTheJackal)
- 📞 **Carrier legal contact database** (DezTheJackal)
- 🗂️ **Case tracking and management** (DezTheJackal)

### v2.0 - 2025
- SQLite caching for 10x performance (0xb0rn3)
- Reputation engine with multi-source aggregation (0xb0rn3)
- ML-powered risk classification (0xb0rn3)
- Enhanced carrier intelligence (0xb0rn3)
- Rich terminal UI (0xb0rn3)

### v1.1 - 2025
- Go-powered web scanner (0xb0rn3)
- OSINT query generation (0xb0rn3)
- API integration (NumVerify, Twilio) (0xb0rn3)
- Multi-platform installer (0xb0rn3)
- VoIP/disposable detection (0xb0rn3)

### v1.0 - 2025
- Initial release (DezTheJackal)
- Core phone lookup functionality (DezTheJackal)
- Carrier and location identification (DezTheJackal)
- Number type detection (DezTheJackal)

---

<div align="center">

**⭐ Star this repo if you find it useful!**

**Made with 💙 for the OSINT and Law Enforcement communities**

</div>
