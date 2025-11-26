# Contributors

## Original Author

**DezTheJackal** - Creator and maintainer of PhoneBookLOCA
- Original concept and implementation (v1.0)
- Core phone number lookup functionality
- Base architecture and design
- Foundation for all subsequent features

## v1.1 Contributions

**0xb0rn3 | oxbv1** - OSINT intelligence platform and performance enhancements

### Web Intelligence Features
- Go-powered concurrent web scanner
  - Checks 8+ sources simultaneously using goroutines
  - 1-2 second scan completion time
  - Clean JSON output architecture
  - Animated loading interface
- OSINT query generation system (Google dorks, social media searches)
- Automated lookup URL generation (TrueCaller, Whitepages, etc.)
- Clean results presentation with organized display

### Security & Analysis Features
- VoIP/disposable number detection system
- Reputation checking framework
- Pattern analysis in session statistics
- Number format variant generation for enumeration

### API & Integration
- API integration framework
  - NumVerify (free tier)
  - Twilio Lookup (paid)
- Prompt-based API configuration system
- Persistent API key storage (~/.phonebookloca_config.json)

### Installation & Platform Support
- Multi-platform installer (install.sh)
  - Auto-detects OS and package manager
  - Supports: pacman, apt, dnf, yum, zypper, apk
  - Auto-installs Python/pip when needed
  - Automatic --break-system-packages handling
  - System-wide or local installation modes
- Cross-platform compatibility
  - All Linux distributions
  - macOS (Intel and Apple Silicon)
  - Windows (Git Bash, WSL)

### Interactive & Batch Features
- Enhanced interactive mode commands
  - `osint <number>` - Full OSINT scan
  - `reputation <number>` - Reputation check
  - `config` - API configuration
  - `stats` - Session analytics with VoIP tracking
  - `export` - Session results export
- Batch processing support for all new features
- Multiple export formats (JSON, CSV, TXT)
- Text scanning for number extraction

### Technical Implementation
- scraper.go - Concurrent Go web scraper
- Threading for loading animations
- Color-coded terminal output
- Global requirements.txt management
- Clean stderr/stdout separation

---
# Contributors

## Creator

**DezTheJackal** - Creator and maintainer of PhoneBookLOCA
- Original concept and implementation (v1.0)
- Core phone number lookup functionality
- Base architecture and design
- Foundation for all subsequent features
- **v2.1 Law Enforcement Geolocation Features** (2025)
  - Enhanced geolocation system
  - Law enforcement investigation interface
  - Professional report generation (JSON, CSV, HTML)
  - Case tracking and management
  - Cell tower proximity analysis
  - Missing persons investigation tools
  - Legal compliance framework

---

## v1.1 Contributions

**0xb0rn3 | oxbv1** - OSINT intelligence platform and API integration

### Web Intelligence Features
- Go-powered concurrent web scanner
- OSINT query generation system
- Automated lookup URL generation
- Clean results presentation

### Security & Analysis Features
- VoIP/disposable number detection
- Reputation checking framework
- Pattern analysis in session statistics
- Number format variant generation

### API & Integration
- NumVerify integration (free tier)
- Twilio Lookup integration (paid)
- Prompt-based API configuration
- Persistent API key storage

### Installation & Platform Support
- Multi-platform installer (install.sh)
- Cross-platform compatibility
- Package manager detection

---

## v2.0 Contributions

**0xb0rn3 | oxbv1** - Professional platform transformation

### Core Infrastructure
- SQLite caching system for 10x performance
- Persistent cache database with expiration
- Confidence scoring per cached entry
- Historical event logging
- Cache management commands

### Advanced Reputation Engine
- Multi-source aggregation (6+ free sources)
- Concurrent checking with ThreadPoolExecutor
- Weighted scoring algorithm (0-100 scale)
- Risk level classification
- Confidence scoring

### Enhanced Carrier Intelligence
- MNO vs MVNO detection
- Parent network identification
- Network technology enumeration
- Security features detection
- Spam tolerance assessment

### ML-Powered Risk Classification
- Multi-factor risk scoring
- Usage indicators detection
- Anomaly detection framework
- Automated recommendations

### Rich Terminal UI
- Beautiful panel-based layout (optional)
- Color-coded risk levels
- Structured information sections
- Progress indicators

---

## v2.1 Contributions (Law Enforcement Edition)

**DezTheJackal** - Enhanced geolocation and law enforcement tools

### Enhanced Geolocation System
- Area code and exchange mapping database
  - Comprehensive US/Canada NANP coverage
  - City, county, state, and coordinate data
  - Population and timezone information
  - ±5-50 km precision levels

- Cell tower proximity analysis
  - Public cell tower database integration
  - Distance calculations using Haversine formula
  - Technology detection (5G, LTE, 4G, 3G)
  - Carrier infrastructure mapping

- Geographic intelligence
  - Coordinate estimation with confidence scoring
  - Multi-source data aggregation
  - Precision level classification
  - Accuracy radius calculation

### Law Enforcement Investigation Interface
- Interactive LE mode workflow
  - Case information collection
  - Automated enhanced geolocation
  - Carrier legal contact retrieval
  - Investigative lead generation

- Case tracking system
  - SQLite database for case management
  - Case number, officer, agency tracking
  - Priority and status management
  - Timestamp and notes

### Professional Report Generation
- JSON export
  - Machine-readable format
  - Complete case documentation
  - Legal disclaimers included
  - Systems integration ready

- CSV export
  - Spreadsheet-compatible format
  - Flattened data structure
  - Easy import to case management systems

- HTML export
  - Professional formatted reports
  - Legal disclaimer sections
  - Interactive map links
  - Carrier contact information
  - Browser-ready for printing/sharing

### Legal Compliance Framework
- Data limitation disclaimers
  - Clear explanation of approximate nature
  - Legal requirements for real-time tracking
  - Warrant and court order guidance

- Carrier legal contact database
  - Verizon Wireless contacts
  - AT&T contacts
  - T-Mobile contacts
  - Emergency 24/7 numbers
  - Legal compliance departments

- Investigative recommendations
  - Immediate action suggestions
  - Legal next steps
  - Search area calculations
  - Resource deployment guidance

### Missing Persons Investigation Tools
- Search area estimation
- Priority level assessment
- Resource recommendation system
- Timeline estimates for carrier response
- Risk factor identification

---

## How to Contribute

[Rest of contribution guidelines remain the same...]
---

## How to Contribute

Want to add features to PhoneBookLOCA? Here's how:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Test thoroughly on multiple platforms
5. Submit a pull request with clear description

### Contribution Guidelines

- Maintain backwards compatibility
- Follow existing code style
- Credit original author (DezTheJackal) in file headers
- Add your name to this file with your contributions
- Test on multiple platforms before submitting
- Update README.md with new features

---

**Original tool by:** DezTheJackal  
**v1.1 maintained by:** 0xb0rn3 | oxbv1

For issues or feature requests, visit: https://github.com/DezTheJackal/PhoneBookLOCA
