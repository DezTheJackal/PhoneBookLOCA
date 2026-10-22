# Changelog

All notable changes to PhoneBookLOCA will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

-----

## [2.3.1] - 2026-10-21

### 🔎 OSINT Update - Accurate Links + Data-Breach Check

**Developed by:** DezTheJackal. No existing command or flag changed.

### Added
- **Data-breach check** inside `--osint` / `osint <number>` / `--le-mode`, with **no API required**:
  - *Offline*: searches breach files (`.csv .tsv .txt .json .jsonl .sql .log`, optionally `.gz`) in
    `~/.phonebookloca/breach_data/` (or `PHONEBOOKLOCA_BREACH_DIR`). Matches every common storage form of
    the number (E.164, `00` prefix, national, formatted) on whole fields, so longer numbers do not
    false-match. Folder is auto-created; capped at 25 hits/file and 100 total.
  - *Online (optional)*: Have I Been Pwned (`HIBP_API_KEY`) and LeakCheck (`LEAKCHECK_API_KEY`).
  - Free manual links are always shown (Have I Been Pwned, Max Intel Phone Lookup) plus the open-source
    tools PhoneInfoga and Ignorant. No paid platform (e.g. Intelligence X) is linked.
- `.gitignore` excluding `breach_data/`, `reports/`, local databases and built scraper binaries.
- **Breach report files**: when a breach is found, `BREACH_<number>_<timestamp>.json` and `.html` are
  written to `~/.phonebookloca/reports/breach/`. No files are written when nothing is found. Raw leaked
  values (passwords, emails, names) and matching lines are never stored - only source/file name, line
  number, date and exposed field names.
- Messaging-app links (`wa.me`, `t.me`, `signal.me`) and clickable Google search links for each dork.
- Recommendation added to LE reports when a number appears in a breach.

- **LE mode over a number list**: `--le-mode --batch numbers.txt` asks the case details once, runs every
  number through the full LE flow (geolocation, porting, OSINT, breach check), creates one case per number
  (`<case>-001`, `-002`, …), and writes a combined summary (`LE_Summary_*.csv/.html/.json`). Blank lines,
  `#` comments and duplicates are skipped; bad numbers are logged in the summary and the run continues.
  Also available in interactive mode as `le-mode --batch numbers.txt`.
  `--le-mode` and `--batch` still behave exactly as before when used on their own.

### Fixed
- Truecaller link used the numeric calling code (`/search/27/...`); it now uses the ISO region
  (`/search/za/...`).
- Whitepages link used undashed digits and appeared for every country; it now uses the dashed US format and
  only appears for `+1` numbers.
- Dorks now cover E.164, international and local number formats instead of E.164/national digits only.
- A cached plain lookup no longer suppresses `--geo`/`--osint` output requested later; OSINT/breach data is
  always fetched live.
- HTML breach reports escape all values.

-----

## [2.3.0] - 2026-09-20

### 🔧 Maintenance Release - Bug Fixes, Cross-Platform Support, Dormant Features

**Developed by:** DezTheJackal

This release fixes real bugs found in v2.2, brings full Windows/macOS support, implements features that
were documented in earlier changelogs/README sections but never actually wired into the code, and adds
a new cyberpunk visual identity.

### Fixed
- Crash in `--le-mode`: a stray `returnPhoneBookLOCA` token (invalid Python, left over from an editing
  mistake) has been replaced with a plain `return`.
- Area-code geolocation silently returning `country`-level precision for numbers whose area code isn't
  3 digits (e.g. UK `020`). Lookup now tries 4-, 3-, 2-, and 1-digit prefixes and takes the first match.
- First-run crash when `~/.phonebookloca`'s parent directory didn't already exist (`mkdir` now uses
  `parents=True`).
- Bare `except:` blocks replaced with specific exception types throughout, so real failures are visible
  with `--verbose` instead of being silently swallowed.
- `shutil.which()` returning `None` for an unbuilt Go scraper could resolve to `Path("")`, which
  `.exists()` treats as the current directory — fixed to only check a candidate path when one was
  actually found.
- Removed duplicate "PhoneBookLOCA Quote Fix" / "Quote Fixer" utility files left over from a stale
  encoding-bug workaround; the underlying bug they patched around no longer exists in this codebase.

### Added
- **Cross-platform Windows support**: `colorama` initialization for correct ANSI color rendering on
  `cmd.exe`, and a native `install.ps1` PowerShell installer (the existing `install.sh` only ever worked
  under WSL/Git Bash on Windows).
- **Confidence scoring** for both porting detection (0-100%, with named indicators) and geolocation
  precision (`country`/`area_code`/`cell_tower` mapped to 30/70/90%).
- **Risk-scored batch analysis**: clustering, same-carrier percentage, and VoIP ratio combine into a
  0-100 risk score and Low/Medium/High rating; the full report is now saved to disk automatically
  (`batch_analysis_<timestamp>.json`, or `--output <path>`) — previously described in this changelog but
  never implemented.
- **`osint` command and `--osint` flag**: generates Google dorks and public lookup-service URLs, and
  invokes the previously-orphaned `scraper.go` binary automatically if it has been built (cross-platform:
  `scraper` / `scraper.exe`).
- **Historical data in reports**: first/last seen, total lookups, and carrier-change detection, now
  actually displayed from the `history` table that v2.2 started populating but never surfaced.
- **CSV and HTML export** for LE-mode reports, alongside the existing JSON export.
- **LE case metadata**: case type and priority are now captured and stored alongside case number,
  officer, and agency.
- **`data/area_codes.json`**: the worldwide area-code table moved out of the script into an external,
  git-diffable data file. Added South African coverage (Johannesburg, Cape Town, Durban, Pretoria, Port
  Elizabeth, Bloemfontein), which had no entries at all in v2.2 despite the "worldwide" branding.
- **`data/carrier_contacts.json`**: a small, extensible reference of public carrier legal-compliance
  contact portals, surfaced in LE-mode reports and recommendations.
- **Cyberpunk logo** (`assets/logo.svg`) and square icon variant (`assets/icon.svg`) for the README header
  and GitHub social preview/avatar use.
- **`push.sh` / `push.ps1`**: maintainer scripts to stage, commit, tag, and push a release using the
  user's own git credentials.
- `--version` flag and top-level exception handler so an unexpected error prints a short message instead
  of a raw traceback (full traceback still available via `--verbose`).

### Changed
- README rewritten to describe only what the tool actually does — removed aspirational claims (200+
  countries, ML classification, a reputation engine) that were never implemented, and dropped the
  hardcoded "carrier emergency contact" phone numbers in favor of the versioned, correctable
  `data/carrier_contacts.json`.
- `requirements.txt` updated to include `colorama` (Windows-only) and note actual minimum Python version
  (3.8+, matching `f-string`/`pathlib` usage already in the script).

-----



### 🌍 Major Release - Worldwide Database + Advanced Analytics

**Developed by:** DezTheJackal

This release expands PhoneBookLOCA from North America to worldwide coverage and adds advanced intelligence features for pattern detection and analysis.

### Added

#### Worldwide Database Coverage

- **Comprehensive Geographic Database**
  - 200+ countries with major cities
  - Accurate coordinates (latitude/longitude) for all entries
  - Population data for context analysis
  - Timezone information for temporal correlation
  - Country, region, city, county-level data
- **Regional Coverage**
  - **North America**: All 50 US states, Canadian provinces, Mexico (expanded from v2.1)
  - **Europe**: UK, Germany, France, Spain, Italy, Netherlands, Belgium, Switzerland, Austria, Poland, Scandinavia, Ireland
  - **Asia**: Japan, China, India, South Korea, Thailand, Malaysia, Singapore, Philippines, Vietnam, Indonesia, Pakistan, Bangladesh
  - **Middle East**: UAE, Saudi Arabia, Israel, Turkey, Iran
  - **South America**: Brazil, Argentina, Chile, Colombia, Peru, Venezuela
  - **Africa**: South Africa, Egypt, Nigeria, Kenya, Morocco
  - **Oceania**: Australia, New Zealand
- **Database Schema Enhancements**
  
  ```sql
  CREATE TABLE area_code_mapping (
      country_code TEXT,
      area_code TEXT,
      city TEXT,
      region TEXT,
      country TEXT,
      latitude REAL,
      longitude REAL,
      population INTEGER,
      timezone TEXT,
      PRIMARY KEY (country_code, area_code)
  );
  ```

#### OpenCellID Integration (Optional Free API)

- **40 Million+ Cell Towers Worldwide**
  - Real cell tower location data (vs sample data in v2.1)
  - Distance calculations using Haversine formula
  - Technology detection (5G, LTE, 4G, 3G)
  - Sample count for reliability assessment
  - Automatic integration when API key configured
- **API Features**
  - Free tier: 1000 requests/day
  - Get cell tower by MCC/MNC/LAC/CellID
  - Search nearby towers by coordinates
  - Radius search up to 10km
  - JSON response format
- **Implementation**
  
  ```python
  class OpenCellIDIntegration:
      def get_cell_tower(mcc, mnc, lac, cellid)
      def search_nearby_towers(lat, lon, radius)
  ```
- **Configuration**
  
  ```bash
  export OPENCELLID_API_KEY="your_key_here"
  # Tool auto-detects and uses API
  ```

#### Number Porting Detection System

- **Comprehensive Porting Analysis**
  - Carrier mismatch detection (area code vs actual carrier)
  - MVNO identification (carriers requiring porting from MNO)
  - VoIP number flagging (commonly ported)
  - Historical porting database
  - Confidence scoring (0.0-1.0)
- **Detection Methods**
  - Heuristic analysis (carrier patterns)
  - Historical database checking
  - MVNO parent network identification
  - VoIP/number type analysis
- **Porting Database**
  
  ```sql
  CREATE TABLE porting_history (
      number TEXT,
      original_carrier TEXT,
      current_carrier TEXT,
      original_area_code TEXT,
      port_detected_date TIMESTAMP,
      confidence REAL,
      detection_method TEXT
  );
  ```
- **Output Example**
  
  ```
  ⚠️ Porting Detected:
  Confidence: 75%
  Indicators:
    • Carrier mismatch: Expected AT&T, found Verizon
    • MVNO carrier detected
    • Number likely ported - location may not match area code
  ```

#### Batch Analysis & Pattern Detection

- **Multi-Number Analysis**
  - Analyze 5-1000+ numbers simultaneously
  - Geographic clustering detection
  - Carrier pattern analysis
  - Temporal pattern recognition
  - Risk assessment and scoring
- **Pattern Detection Algorithms**
  - **Geographic Clustering**: Detect numbers concentrated in specific areas
  - **Burner Farm Detection**: Identify bulk purchases (same carrier, same area)
  - **VoIP Concentration**: Flag high VoIP usage (anonymity indicator)
  - **Impossible Travel**: Detect geographic impossibilities
  - **Carrier Patterns**: Same carrier usage across batch
- **Suspicious Pattern Identification**
  
  ```python
  - "High geographic clustering: 15 numbers in 2 locations"
  - "All 15 numbers on same carrier - possible bulk purchase"
  - "High VoIP usage: 12/15 numbers are VoIP - anonymity attempt"
  ```
- **Risk Scoring**
  - 0-100 scale risk score
  - Risk levels: Low, Medium, High
  - Confidence percentages
  - Pattern count tracking
- **Usage**
  
  ```bash
  # Create file with numbers (one per line)
  ./PhoneBookLOCA --batch numbers.txt
  
  # Output: JSON report with patterns
  numbers_analysis.json
  ```

#### Enhanced OSINT Automation

- **Automated Intelligence Gathering**
  - Google dork generation (optimized queries)
  - Social media presence URLs
  - Data breach checking recommendations
  - Paste site search queries
  - Lookup service URL generation
- **Search Query Generation**
  
  ```python
  'google_dorks': [
      '"{number}"',
      '"{number}" (email OR contact OR phone)',
      'site:facebook.com "{number}"',
      'site:linkedin.com "{number}"',
      'intext:"{number}" (database OR leak)',
  ]
  ```
- **Social Media URLs**
  - Facebook search links
  - LinkedIn search links
  - Twitter/X search links
  - Instagram hashtag links
- **Investigative Recommendations**
  - TrueCaller lookup
  - Data breach database checks
  - Paste site searches
  - Court records guidance
  - Social media correlation

#### Historical Tracking System

- **Comprehensive Lookup Logging**
  - All lookups logged with timestamps
  - Carrier tracking over time
  - Location movement detection
  - Agency/officer tracking
  - Case number correlation
- **Historical Analysis**
  
  ```python
  {
      'first_seen': '2024-11-15 14:30:00',
      'last_seen': '2025-01-20 10:15:00',
      'total_lookups': 8,
      'carrier_changes': True,
      'carriers_seen': ['AT&T', 'Verizon'],
      'location_changes': True,
      'locations_seen': ['San Francisco', 'Oakland'],
      'lookup_agencies': ['SFPD', 'FBI']
  }
  ```
- **Database Schema**
  
  ```sql
  CREATE TABLE historical_tracking (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      number TEXT,
      lookup_timestamp TIMESTAMP,
      carrier TEXT,
      location TEXT,
      number_type TEXT,
      agency TEXT,
      officer TEXT,
      case_number TEXT,
      notes TEXT
  );
  ```

#### Real-Time Carrier Integration Framework

- **Emergency Ping Request System**
  - Structured request framework
  - Carrier contact information
  - Legal requirement documentation
  - Exigent circumstances guidance
  - Note: Requires LE credentials for actual use
- **CDR Request System**
  - Call Detail Record request framework
  - Portal URLs for major carriers
  - Legal documentation requirements
  - Typical response time estimates
- **Carrier Contact Database**
  - Verizon: 1-888-483-7200 (emergency 24/7)
  - AT&T: 1-800-635-6840 (emergency 24/7)
  - T-Mobile: 1-888-987-4500 (emergency 24/7)
  - Email addresses for legal departments
  - Online portal URLs
- **Implementation Note**
  
  ```python
  class CarrierAPIIntegration:
      def emergency_ping(number, case_number, officer_badge)
      def request_cdr(number, case_number, warrant_number)
  ```
  
  Returns guidance and contact information (not actual tracking)

### Changed

#### Geolocation Engine

- **Worldwide Support**
  - Now handles international phone numbers correctly
  - Country-specific area code parsing
  - Variable area code lengths (2-4 digits)
  - Regional timezone mapping
- **Enhanced Precision Levels**
  - **Exchange-level**: ±5 km (when data available)
  - **Area code-level**: ±50 km (standard)
  - **City-level**: ±25 km (international)
  - **Country-level**: ±200 km (fallback)
  - **Cell tower**: ±5-10 km (with OpenCellID)
- **Confidence Scoring Improvements**
  - Base confidence: 0.6-0.8 depending on precision
  - OpenCellID bonus: +0.1 confidence
  - Porting penalty: -30% confidence if detected
  - Historical data bonus: +0.05 confidence

#### Output Format Enhancements

- **Porting Information Display**
  
  ```
  ⚠️ Porting Analysis:
  Likely Ported: Yes (75% confidence)
  Current Carrier: Verizon Wireless
  Expected Carrier: AT&T
  Indicators:
    • Carrier mismatch
    • MVNO detected
  ```
- **Historical Data Display**
  
  ```
  📜 Historical Data:
  First Seen: 2024-11-15
  Last Seen: 2025-01-20
  Total Lookups: 8
  Carrier Changes: Yes
  Agencies: SFPD, FBI
  ```
- **Cell Tower Display (OpenCellID)**
  
  ```
  📡 Cell Towers: 5 nearby
  Primary Tower:
    • Distance: 2.3 km
    • Range: 5 km
    • Technology: 5G, LTE
    • Samples: 1547
  ```

#### Interactive Mode Commands

- **New Commands**
  
  ```
  batch <file>          Batch analysis from file
  osint <number>        OSINT intelligence generation
  geo <number>          Enhanced geolocation (unchanged)
  le-mode              Law enforcement mode (unchanged)
  ```

#### Law Enforcement Reports

- **Enhanced Report Content**
  - Porting analysis section
  - Historical tracking data
  - OpenCellID tower data (if available)
  - Pattern analysis (for batch cases)
  - Expanded legal guidance
- **Report Exports**
  - JSON: Machine-readable with all data
  - CSV: Spreadsheet-compatible
  - HTML: Professional formatted with all sections

### Improved

#### Performance Optimizations

- **Database Indexing**
  
  ```sql
  CREATE INDEX idx_hist_number ON historical_tracking(number)
  CREATE INDEX idx_hist_timestamp ON historical_tracking(lookup_timestamp)
  CREATE INDEX idx_porting ON porting_history(number)
  ```
- **Concurrent Processing**
  - OpenCellID API calls async where possible
  - Batch analysis parallelized
  - Cache lookups optimized
- **Memory Efficiency**
  - Streaming batch analysis for large files
  - Lazy loading of worldwide database
  - Efficient cache management

#### User Experience

- **Better Error Messages**
  - Clear OpenCellID configuration guidance
  - Porting detection explanations
  - Batch file format help
  - International number format examples
- **Progress Indicators**
  - Batch analysis progress bars
  - OpenCellID query status
  - Report generation progress
- **Help System**
  - Updated help text with v2.2 features
  - Command examples
  - Feature descriptions

### Dependencies

#### No New Required Dependencies

- `phonenumbers>=8.12.0` (unchanged)
- `requests>=2.25.0` (unchanged)
- `rich>=13.0.0` (unchanged, optional)

#### Optional API Keys

- OpenCellID API key (free, 1000 req/day)
  - Registration: https://opencellid.org/
  - Configuration: `export OPENCELLID_API_KEY="key"`

### Performance Benchmarks

|Operation           |v2.1 |v2.2         |Improvement|
|--------------------|-----|-------------|-----------|
|US lookup           |5-10s|5-10s (first)|Same       |
|International lookup|N/A  |5-10s (first)|New feature|
|Cached lookup       |<1s  |<1s          |Same       |
|With OpenCellID     |N/A  |3-8s (first) |New feature|
|Batch (10 numbers)  |N/A  |15-30s       |New feature|
|Batch (100 numbers) |N/A  |2-5min       |New feature|

### Breaking Changes

**None!** v2.2 is fully backwards compatible with v2.1.

All existing commands, scripts, and workflows continue to work without modification.

### Migration Notes

- No migration required from v2.1
- Database schema automatically updated on first run
- Worldwide database loaded automatically
- OpenCellID optional - works without API key
- All v2.1 features retained and enhanced

### Documentation

- Updated README.md with v2.2 worldwide features
- Added SETUP_v2.2.md installation guide
- Updated CONTRIBUTORS.md with DezTheJackal v2.2 credits
- Added CHANGELOG.md v2.2 section (this file)

### Known Limitations

- **Worldwide Database**
  - Not all cities covered (focuses on major cities)
  - Some countries have limited data
  - Area code extraction varies by country
- **OpenCellID**
  - Requires API key for full functionality
  - Free tier limited to 1000 requests/day
  - Coverage varies by country
- **Porting Detection**
  - Heuristic-based (not 100% accurate)
  - Requires carrier pattern data
  - Best for US/Canada numbers

### Future Enhancements (Planned for v2.3+)

- HLR/HLR Lookup integration for live status
- Enhanced worldwide database (more cities)
- Machine learning porting detection
- Real carrier API integration (with credentials)
- Advanced pattern detection algorithms
- Graph visualization for batch analysis

-----

## [2.1.0] - 2025-11-26

### 🚨 Major Release - Law Enforcement Edition

**Developed by:** DezTheJackal

[Previous v2.1 changelog content remains unchanged…]

-----

## [2.0.0] - 2025-10-27

### 🚀 Major Release - Professional OSINT Platform Transformation

**Developed by:** 0xb0rn3 | oxbv1

[Previous v2.0 changelog content remains unchanged…]

-----

## [1.1.0] - 2025-10-06

### 🎯 OSINT Intelligence Platform

**Developed by:** 0xb0rn3 | oxbv1

[Previous v1.1 changelog content remains unchanged…]

-----

## [1.0.0] - 2025-09-15 (Estimated)

### 🎉 Initial Release

**Created by:** DezTheJackal

[Previous v1.0 changelog content remains unchanged…]

-----

## Version Comparison Matrix

|Feature            |v1.0|v1.1 |v2.0  |v2.1  |v2.2                |
|-------------------|----|-----|------|------|--------------------|
|Basic lookup       |✅   |✅    |✅     |✅     |✅                   |
|US/Canada          |✅   |✅    |✅     |✅     |✅ Enhanced          |
|Worldwide          |❌   |❌    |❌     |❌     |✅ **200+ countries**|
|OSINT queries      |❌   |✅    |✅     |✅     |✅ Enhanced          |
|Caching            |❌   |❌    |✅     |✅     |✅                   |
|Reputation         |❌   |Basic|✅     |✅     |✅                   |
|Enhanced geo       |❌   |❌    |❌     |✅     |✅ Worldwide         |
|LE tools           |❌   |❌    |❌     |✅     |✅ Enhanced          |
|Cell towers        |❌   |❌    |Sample|Sample|✅ **40M+ real**     |
|Porting detection  |❌   |❌    |❌     |❌     |✅ **New**           |
|Batch analysis     |❌   |❌    |❌     |❌     |✅ **New**           |
|Historical tracking|❌   |❌    |❌     |❌     |✅ **New**           |
|Pattern detection  |❌   |❌    |❌     |❌     |✅ **New**           |
|OSINT automation   |❌   |Basic|✅     |✅     |✅ **Enhanced**      |

-----

## Contributors by Version

- **v1.0**: DezTheJackal (Original creator)
- **v1.1**: 0xb0rn3 | oxbv1 (OSINT features, installer, web scanner)
- **v2.0**: 0xb0rn3 | oxbv1 (Professional platform transformation)
- **v2.1**: DezTheJackal (Law enforcement geolocation)
- **v2.2**: DezTheJackal (Worldwide database + advanced features)

-----

## Links

- **Repository**: https://github.com/DezTheJackal/PhoneBookLOCA
- **Issues**: https://github.com/DezTheJackal/PhoneBookLOCA/issues
- **Releases**: https://github.com/DezTheJackal/PhoneBookLOCA/releases
- **Documentation**: README.md, SETUP_v2.2.md, CONTRIBUTORS.md

-----

<div align="center">

**PhoneBookLOCA** - From basic lookup to worldwide OSINT platform

*For educational, authorized security research, and law enforcement only*

Created by **DezTheJackal** | Enhanced by the community

</div>
