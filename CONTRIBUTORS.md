# Contributors

## Creator & Primary Maintainer

**DezTheJackal** - Creator and maintainer of PhoneBookLOCA

### Original Creation (v1.0)

- Original concept and implementation
- Core phone number lookup functionality
- Base architecture and design
- Foundation for all subsequent features
- Geographic location detection
- Carrier identification
- Number type classification
- Timezone mapping

### v2.1 - Law Enforcement Edition

- Enhanced geolocation system
- Law enforcement investigation interface
- Professional report generation (JSON, CSV, HTML)
- Case tracking and management system
- Cell tower proximity analysis
- Missing persons investigation tools
- Legal compliance framework
- Carrier legal contact database

### v2.2 - Worldwide Database + Advanced Features

- **Worldwide Geographic Database (200+ countries)**
  - Comprehensive area code mapping for North America, Europe, Asia, Middle East, South America, Africa, Oceania
  - Accurate coordinates (latitude/longitude) for major cities worldwide
  - Population and timezone data integration
  - Multi-regional coverage expansion
- **OpenCellID Integration**
  - Integration with OpenCellID API (40M+ cell towers)
  - Real cell tower data vs sample data
  - Distance calculation algorithms
  - Automatic API key detection and usage
  - Free tier support (1000 requests/day)
- **Number Porting Detection System**
  - Carrier mismatch detection algorithms
  - MVNO identification logic
  - Historical porting database
  - Confidence scoring system
  - Porting indicator analysis
- **Batch Analysis & Pattern Detection**
  - Multi-number analysis engine
  - Geographic clustering algorithms
  - Burner farm detection
  - Risk scoring system (0-100 scale)
  - Suspicious pattern identification
  - VoIP concentration detection
- **Enhanced OSINT Automation**
  - Automated search query generation
  - Google dork optimization
  - Social media presence checking
  - Data breach correlation hints
  - Investigative recommendation engine
- **Historical Tracking System**
  - Comprehensive lookup logging
  - Carrier change detection over time
  - Location movement tracking
  - Agency/officer correlation
  - Case number association
- **Real-Time Carrier Integration Framework**
  - Emergency ping request structure
  - CDR request system
  - Carrier contact database
  - Legal procedure documentation

-----

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
  - Automatic –break-system-packages handling
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

-----

## v2.0 Contributions

**0xb0rn3 | oxbv1** - Professional platform transformation

### Core Infrastructure

- SQLite caching system for 10x performance
  - Persistent cache database at `~/.phonebookloca/intel.db`
  - Automatic schema creation and management
  - Configurable freshness (default: 24 hours)
  - Confidence scoring per cached entry
  - Lookup count tracking
  - Historical event logging
  - Indexed queries for optimal performance
- Cache Management Commands
  - `--cache-stats` command to view statistics
  - `--clear-cache [days]` command to manage old entries
  - `--no-cache` flag to force fresh lookups
  - Interactive commands: `cache`, `clear-cache`

### Advanced Reputation Engine

- Multi-source aggregation (6+ free sources)
- Concurrent checking with ThreadPoolExecutor
- Weighted scoring algorithm (0-100 scale)
- Risk level classification (very_low to very_high)
- Confidence scoring based on source responses
- Report categorization (spam/scam/legitimate/robocall)
- Persistent storage in reputation_intel table
- Automatic integration with `--reputation` flag
- Trend analysis (stable/increasing/decreasing)

### Enhanced Carrier Intelligence

- MNO vs MVNO detection
- Parent network identification for MVNOs
- Network technology enumeration (5G, LTE, 4G, 3G)
- Coverage area identification
- Security features detection (STIR/SHAKEN, spam blocking)
- Spam tolerance assessment
- Carrier reputation system

### ML-Powered Risk Classification

- Multi-factor risk scoring (0-100)
- Weighted algorithm considering multiple indicators
- Sub-type detection (personal, business, virtual, service)
- Usage indicators (personal, business, disposable, VoIP, burner)
- Anomaly detection framework
- Automated recommendations
- Confidence scoring per classification
- Risk level categorization (Low/Medium/High)

### Rich Terminal UI (Optional)

- Beautiful panel-based layout using Rich library
- Color-coded risk levels (green/yellow/red)
- Structured information sections
- Visual hierarchy for easy scanning
- Progress indicators and spinners
- Professional appearance
- Graceful fallback to basic ANSI colors
- Auto-detection of Rich library availability

### Technical Implementation

- Database schema design and optimization
- Threading and concurrent processing
- Caching algorithms and expiration logic
- Risk scoring mathematical models
- UI/UX design and implementation

-----

## v2.1 - Law Enforcement Edition (Detailed)

**DezTheJackal** - Enhanced geolocation and law enforcement tools

### Enhanced Geolocation System

- **Area Code and Exchange Mapping Database**
  - Comprehensive US/Canada NANP coverage
  - City, county, state, and coordinate data
  - Population and timezone information
  - ±5-50 km precision levels
  - Exchange-level precision (±5 km)
  - Area code-level precision (±50 km)
- **Cell Tower Proximity Analysis**
  - Public cell tower database integration
  - Distance calculations using Haversine formula
  - Technology detection (5G, LTE, 4G, 3G)
  - Carrier infrastructure mapping
  - Range estimation algorithms
- **Geographic Intelligence**
  - Coordinate estimation with confidence scoring
  - Multi-source data aggregation
  - Precision level classification
  - Accuracy radius calculation
  - Source tracking and validation

### Law Enforcement Investigation Interface

- **Interactive LE Mode Workflow**
  - Case information collection
  - Automated enhanced geolocation
  - Carrier legal contact retrieval
  - Investigative lead generation
  - Structured investigation process
- **Case Tracking System**
  - SQLite database for case management
  - Case number, officer, agency tracking
  - Priority and status management
  - Timestamp and notes storage
  - Historical case correlation

### Professional Report Generation

- **JSON Export**
  - Machine-readable format
  - Complete case documentation
  - Legal disclaimers included
  - Systems integration ready
  - Structured data hierarchy
- **CSV Export**
  - Spreadsheet-compatible format
  - Flattened data structure
  - Easy import to case management systems
  - Tabular data organization
- **HTML Export**
  - Professional formatted reports
  - Legal disclaimer sections
  - Interactive map links
  - Carrier contact information
  - Browser-ready for printing/sharing
  - CSS styling for professional appearance

### Legal Compliance Framework

- **Data Limitation Disclaimers**
  - Clear explanation of approximate nature
  - Legal requirements for real-time tracking
  - Warrant and court order guidance
  - Emergency ping procedures
- **Carrier Legal Contact Database**
  - Verizon Wireless: 1-800-451-5242, Emergency: 1-888-483-7200
  - AT&T: 1-800-635-6840, Emergency: 1-800-635-6840
  - T-Mobile: 1-800-937-8997, Emergency: 1-888-987-4500
  - Email addresses for legal compliance departments
  - Online portal URLs for legal requests
- **Investigative Recommendations**
  - Immediate action suggestions
  - Legal next steps documentation
  - Search area calculations
  - Resource deployment guidance
  - Priority level assessment

### Missing Persons Investigation Tools

- Search area estimation algorithms
- Priority level assessment criteria
- Resource recommendation system
- Timeline estimates for carrier response
- Risk factor identification

-----

## v2.2 - Worldwide + Advanced Features (Detailed)

**DezTheJackal** - Worldwide expansion and intelligence analytics

### Worldwide Geographic Database

- **Regional Coverage Implementation**
  - **North America (Expanded)**: All 50 US states, 13 Canadian provinces/territories, Mexico major cities
  - **Europe**: UK (England, Scotland, Wales, NI), Germany, France, Spain, Italy, Netherlands, Belgium, Switzerland, Austria, Poland, Sweden, Norway, Denmark, Finland, Ireland, Czech Republic, Hungary, Romania, Ukraine, Portugal, Greece
  - **Asia**: Japan, China, India, South Korea, Thailand, Malaysia, Singapore, Philippines, Vietnam, Indonesia, Pakistan, Bangladesh, Iran, Saudi Arabia, UAE, Israel, Turkey
  - **South America**: Brazil, Argentina, Chile, Colombia, Peru, Venezuela
  - **Africa**: South Africa, Egypt, Nigeria, Kenya, Morocco
  - **Oceania**: Australia, New Zealand
- **Database Engineering**
  - Efficient storage schema design
  - Country code + area code composite keys
  - Indexed queries for fast lookups
  - Lazy loading for memory efficiency
  - Coordinate validation and verification
- **Data Accuracy**
  - Verified coordinates from multiple sources
  - Population data from official sources
  - Timezone mapping using IANA database
  - Regular expression parsing for international formats

### OpenCellID Integration

- **API Integration Architecture**
  - RESTful API client implementation
  - JSON response parsing
  - Error handling and retry logic
  - Rate limiting compliance (1000/day free tier)
  - Timeout handling (10-15 seconds)
- **Tower Location Services**
  - Get tower by MCC/MNC/LAC/CellID
  - Search nearby towers by coordinates
  - Radius search implementation (up to 10km)
  - Distance ranking and sorting
  - Sample count reliability assessment
- **Data Processing**
  - Haversine distance calculation algorithm
  - Tower prioritization by distance
  - Technology string parsing
  - Result deduplication
  - Cache integration for API calls

### Number Porting Detection System

- **Detection Algorithms**
  - **Carrier Mismatch Analysis**: Compare expected carrier (based on area code) vs actual carrier
  - **MVNO Identification**: Database of known MVNOs and their parent networks
  - **VoIP Detection**: Number type analysis for porting indicators
  - **Historical Database**: Track known porting events over time
- **Confidence Calculation**
  - Base confidence from pattern matching
  - Weighted scoring for multiple indicators
  - Historical data boosting
  - MVNO detection adjustment
  - Final confidence normalization (0.0-1.0)
- **Porting Database Management**
  - Automatic porting event logging
  - Historical query capabilities
  - Carrier transition tracking
  - Confidence threshold filtering (≥0.6 for storage)

### Batch Analysis Engine

- **Pattern Detection Algorithms**
  - **Geographic Clustering**:
    - Location frequency analysis
    - Clustering score calculation (0-1)
    - Hotspot identification
    - Radius estimation
  - **Carrier Pattern Analysis**:
    - Unique carrier counting
    - Same-carrier percentage calculation
    - Bulk purchase detection (100% same carrier)
    - MVNO concentration analysis
  - **VoIP Concentration**:
    - Number type distribution analysis
    - VoIP percentage calculation
    - Threshold-based flagging (>50%)
    - Anonymity indicator correlation
  - **Risk Scoring Algorithm**:
    - Pattern-based scoring (20 points per pattern)
    - Threshold classification (Low <30, Medium 30-60, High ≥60)
    - Confidence level integration
    - Risk level categorization
- **Batch Processing Engine**
  - Parallel number validation
  - Concurrent lookups for performance
  - Result aggregation and analysis
  - Statistical computation (Counter, defaultdict)
  - JSON export with full analysis

### Enhanced OSINT Automation

- **Search Query Generation**
  - Optimized Google dork templates
  - Platform-specific query formatting
  - Email correlation queries
  - Data leak detection queries
  - Paste site search strings
- **Social Media Integration**
  - Facebook search URL generation
  - LinkedIn search URL generation
  - Twitter/X search URL generation
  - Instagram hashtag URL generation
  - Check-manually flags for user verification
- **Recommendation Engine**
  - TrueCaller lookup suggestions
  - Data breach database recommendations (HaveIBeenPwned, Dehashed)
  - Paste site search guidance (Pastebin, PasteBin dumps)
  - Court records and public database suggestions
  - Social media correlation strategies

### Historical Tracking System

- **Comprehensive Logging**
  - All lookups logged with microsecond timestamps
  - Carrier name storage
  - Location string storage
  - Number type tracking
  - Agency/officer/case number correlation
- **Change Detection Algorithms**
  - Carrier change identification over time
  - Location movement detection
  - First seen / last seen timestamps
  - Lookup frequency analysis
  - Agency correlation tracking
- **Historical Analysis**
  - Time series analysis of lookups
  - Carrier transition timeline
  - Geographic movement patterns
  - Multi-agency investigation detection
  - Statistical summaries

### Real-Time Carrier Integration Framework

- **Emergency Ping System**
  - Request structure definition
  - Carrier-specific procedures
  - Exigent circumstances documentation template
  - 24/7 contact number database
  - Response time estimates
- **CDR Request System**
  - Call Detail Record request templates
  - Portal URL database
  - Legal requirement checklists
  - Warrant documentation guidance
  - Typical turnaround time estimates
- **Carrier Portal Integration**
  - Verizon legal compliance portal URL
  - AT&T legal request portal URL
  - T-Mobile legal compliance portal URL
  - Sprint/T-Mobile merger notes
  - Regional carrier contact information

### Performance Optimizations

- **Database Indexing**
  - Multi-column index on (country_code, area_code)
  - Index on historical_tracking(number)
  - Index on historical_tracking(lookup_timestamp)
  - Index on porting_history(number)
  - Query execution plan optimization
- **Memory Management**
  - Lazy loading of worldwide database
  - Streaming batch analysis for large files
  - Cache result recycling
  - Garbage collection optimization
  - Connection pooling for database
- **Concurrent Processing**
  - Threaded OpenCellID API calls
  - Parallel batch validation
  - Async pattern detection
  - Non-blocking UI updates

-----

## How to Contribute

Want to add features to PhoneBookLOCA? Here’s how:

### Contribution Process

1. **Fork the repository**
   
   ```bash
   git fork https://github.com/DezTheJackal/PhoneBookLOCA.git
   ```
1. **Create a feature branch**
   
   ```bash
   git checkout -b feature-name
   ```
1. **Make your changes**
- Follow existing code style
- Add comments for complex logic
- Test on multiple platforms
1. **Credit yourself**
- Add your name to this CONTRIBUTORS.md file
- Document your changes in CHANGELOG.md
- Update README.md if adding user-facing features
1. **Submit a pull request**
- Clear description of changes
- List of new features/fixes
- Testing performed
- Screenshots if UI changes

### Contribution Guidelines

- **Maintain backwards compatibility** whenever possible
- **Follow existing code style** (PEP 8 for Python)
- **Credit original author** (DezTheJackal) in file headers
- **Test on multiple platforms** (Linux, macOS, Windows)
- **Update documentation** (README, CHANGELOG, this file)
- **Add yourself to contributors** in this file with detailed description

### Areas for Contribution

We welcome contributions in:

- **Geographic Data**: Additional area codes, cities, coordinates
- **Cell Tower Data**: More cell tower locations
- **International Support**: More country-specific parsing logic
- **Pattern Detection**: New algorithms for batch analysis
- **OSINT Sources**: Additional intelligence sources
- **Performance**: Optimization and speed improvements
- **UI/UX**: Enhanced user interface and experience
- **Documentation**: Better guides, examples, tutorials
- **Testing**: Unit tests, integration tests
- **Bug Fixes**: Issue resolution

### Code of Conduct

- Be respectful and professional
- Help others learn and grow
- Give credit where credit is due
- Follow legal and ethical guidelines
- Report security issues responsibly

-----

## Recognition

### Hall of Fame

- **DezTheJackal**: Creator and primary maintainer (v1.0, v2.1, v2.2)
- **0xb0rn3 | oxbv1**: Major contributor (v1.1, v2.0)

### Community Contributors

Want to see your name here? Submit a pull request!

-----

## Contact

- **Issues**: https://github.com/DezTheJackal/PhoneBookLOCA/issues
- **Pull Requests**: https://github.com/DezTheJackal/PhoneBookLOCA/pulls
- **Discussions**: https://github.com/DezTheJackal/PhoneBookLOCA/discussions

-----

<div align="center">

**Thank you to all contributors who make PhoneBookLOCA better!**

**Original tool by:** DezTheJackal  
**Community enhanced by:** Contributors worldwide

*For educational, authorized security research, and law enforcement use only*

</div>