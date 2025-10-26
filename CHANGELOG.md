# Changelog

All notable changes to PhoneBookLOCA will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [2.0.0] - 2025-10-27

### 🚀 Major Release - Professional OSINT Platform Transformation

**Developed by:** 0xb0rn3 | oxbv1

This release transforms PhoneBookLOCA from a basic lookup tool into a professional-grade OSINT intelligence platform with enterprise features.

### Added

#### Core Infrastructure

- **SQLite Caching System**
  - Persistent cache database at `~/.phonebookloca/intel.db`
  - Automatic schema creation and management
  - Configurable freshness (default: 24 hours)
  - Confidence scoring per cached entry
  - Lookup count tracking
  - Historical event logging
  - Indexed queries for optimal performance
  - `--cache-stats` command to view statistics
  - `--clear-cache [days]` command to manage old entries
  - `--no-cache` flag to force fresh lookups
  - Interactive commands: `cache`, `clear-cache`

- **Advanced Reputation Engine**
  - Multi-source aggregation (6+ free sources)
  - Concurrent checking with ThreadPoolExecutor
  - Weighted scoring algorithm (0-100 scale)
  - Risk level classification (very_low to very_high)
  - Confidence scoring based on source responses
  - Report categorization (spam/scam/legitimate/robocall)
  - Persistent storage in reputation_intel table
  - Automatic integration with `--reputation` flag
  - Trend analysis (stable/increasing/decreasing)

- **Enhanced Carrier Intelligence**
  - MNO vs MVNO detection
  - Parent network identification for MVNOs
  - Network technology enumeration (5G, LTE, 4G, 3G)
  - Coverage area identification
  - Security features detection (STIR/SHAKEN, spam blocking)
  - Spam tolerance assessment
  - Carrier reputation system
  - Automatic with every lookup

- **ML-Powered Risk Classification**
  - Multi-factor risk scoring (0-100)
  - Weighted algorithm considering multiple indicators
  - Sub-type detection (personal, business, virtual, service)
  - Usage indicators (personal, business, disposable, VoIP, burner)
  - Anomaly detection framework
  - Automated recommendations
  - Confidence scoring per classification
  - Risk level categorization (Low/Medium/High)

- **Rich Terminal UI (Optional)**
  - Beautiful panel-based layout
  - Color-coded risk levels (green/yellow/red)
  - Structured information sections
  - Visual hierarchy for easy scanning
  - Progress indicators and spinners
  - Professional appearance
  - Graceful fallback to basic ANSI colors
  - Auto-detection of Rich library availability

#### Database Schema

```sql
-- Main lookups table with caching
CREATE TABLE lookups (
    number TEXT PRIMARY KEY,
    data TEXT,
    confidence_score REAL DEFAULT 0.8,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    lookup_count INTEGER DEFAULT 1,
    data_sources TEXT,
    reputation_score REAL DEFAULT 50.0
);

-- Reputation intelligence
CREATE TABLE reputation_intel (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    number TEXT,
    source TEXT,
    spam_reports INTEGER DEFAULT 0,
    scam_reports INTEGER DEFAULT 0,
    legitimate_reports INTEGER DEFAULT 0,
    last_reported TIMESTAMP,
    report_countries TEXT,
    FOREIGN KEY (number) REFERENCES lookups(number)
);

-- Historical tracking
CREATE TABLE number_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    number TEXT,
    event_type TEXT,
    event_data TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (number) REFERENCES lookups(number)
);
```

#### New Classes

- `IntelligenceCache` - Database management and caching logic
- `ReputationEngine` - Multi-source reputation aggregation
- `CarrierIntelligence` - Advanced carrier analysis
- `NumberClassifier` - ML-powered risk classification

#### New Commands

```bash
--cache-stats              # Show cache statistics
--clear-cache [days]       # Clear old cache entries
--no-cache                 # Force fresh lookup (bypass cache)
```

#### New Interactive Commands

```
cache                      # Show cache statistics
clear-cache [days]         # Clear old entries
```

### Changed

#### Performance

- **10x faster** repeated lookups with caching (<1s vs 5-10s)
- **Concurrent processing** for reputation checks (5-8s vs 10-15s)
- **Optimized database** queries with indexes
- **Efficient algorithms** for data processing

#### Output Format

- Enhanced terminal output with new intelligence sections:
  - Basic Intelligence (existing, enhanced)
  - Carrier Intelligence (new)
  - Risk Assessment (new)
  - Reputation Analysis (enhanced)
  - OSINT results (existing, enhanced)
- Cache hit indicators show data freshness
- Confidence scores displayed throughout
- Color-coded risk levels for quick assessment
- Professional panel layout with Rich (optional)

#### Behavior

- **Lookups now cache by default** (use `--no-cache` for old behavior)
- **Cache age displayed** on subsequent lookups
- **Lookup count tracked** per number
- **Reputation integrated** into main lookup flow
- **All data persisted** to database automatically

### Improved

#### Reputation Checking

- Multi-source aggregation instead of single source
- Concurrent checking for 3-5x speed improvement
- Weighted scoring algorithm for better accuracy
- Confidence levels based on source responses
- Persistent storage for historical analysis

#### Carrier Information

- Detailed carrier type detection (MNO/MVNO)
- Parent network identification
- Network technology enumeration
- Security features detection
- Coverage area analysis

#### Risk Assessment

- Comprehensive scoring algorithm
- Multi-factor analysis
- Automated recommendations
- Confidence scoring
- Usage pattern detection

#### User Experience

- Beautiful Rich UI (when available)
- Clear visual hierarchy
- Cache hit feedback
- Progress indicators
- Professional appearance
- Helpful error messages

### Dependencies

#### Added

- `rich>=13.0.0` - Optional, for enhanced terminal UI

#### Unchanged

- `phonenumbers>=8.12.0` - Core phone number functionality
- `requests>=2.25.0` - HTTP requests

### Performance Benchmarks

| Operation | v1.1 | v2.0 (No Cache) | v2.0 (Cached) |
|-----------|------|-----------------|---------------|
| Single lookup | 5-10s | 5-10s | <1s |
| Reputation check | 10-15s | 5-8s | <1s |
| 10 lookups | 50-100s | 50-100s | 5-10s |
| 100 lookups | 8-16min | 8-16min | 1-2min |

### Breaking Changes

**None!** v2.0 is fully backwards compatible with v1.1.

All existing commands and scripts continue to work without modification.

### Migration Notes

- No migration required
- Cache database created automatically on first run
- Existing config file (`~/.phonebookloca_config.json`) reused
- See MIGRATION_v2.0.md for detailed upgrade guide

### Documentation

- Updated README.md with v2.0 features
- Updated CONTRIBUTORS.md with detailed implementation notes
- Added MIGRATION_v2.0.md upgrade guide
- Added CHANGELOG.md (this file)

---

## [1.1.0] - 2025-10-06

### 🎯 OSINT Intelligence Platform

**Developed by:** 0xb0rn3 | oxbv1

Major feature release adding OSINT capabilities and professional features.

### Added

#### Web Intelligence

- **Go-powered web scraper**
  - Concurrent source checking with goroutines
  - 8+ sources checked simultaneously
  - 1-2 second scan completion
  - Clean JSON output
  - Animated loading interface
  - scraper.go implementation

- **OSINT Query Generation**
  - Google dorks for various platforms
  - Social media search queries
  - Data leak queries
  - Paste site queries
  - Email association searches

- **Lookup URL Generation**
  - TrueCaller direct links
  - Whitepages links
  - WhoCalledMe links
  - SpyDialer links
  - NumLookup links
  - Sync.me links

#### Security & Analysis

- **VoIP/Disposable Detection**
  - VoIP number identification
  - Toll-free number detection
  - Disposable number patterns
  - Service type classification

- **Reputation Checking Framework**
  - Basic reputation structure
  - Report counting
  - Source tracking

- **Pattern Analysis**
  - Session statistics
  - VoIP tracking in stats
  - Pattern detection in batches

- **Number Variant Generation**
  - Multiple format variants
  - Enumeration support
  - Format normalization

#### API Integration

- **NumVerify Integration**
  - Free tier support
  - Enhanced carrier data
  - Line type detection
  - Country validation

- **Twilio Lookup Integration**
  - Paid API support
  - Carrier name and type
  - National format
  - Enhanced validation

- **Configuration System**
  - Prompt-based API setup
  - Persistent key storage
  - `~/.phonebookloca_config.json`
  - Interactive configuration

#### Installation & Platform Support

- **Multi-platform Installer (install.sh)**
  - OS auto-detection (Linux, macOS, Windows)
  - Package manager detection (pacman, apt, dnf, yum, zypper, apk)
  - Auto-install Python/pip
  - Automatic `--break-system-packages` handling
  - System-wide or local installation modes
  - Go scraper compilation
  - Dependency verification

- **Cross-platform Compatibility**
  - All Linux distributions
  - macOS (Intel and Apple Silicon)
  - Windows (Git Bash, WSL)

#### Interactive & Batch Features

- **Enhanced Interactive Mode**
  - `osint <number>` - Full OSINT scan
  - `reputation <number>` - Reputation check
  - `config` - API configuration
  - `stats` - Session analytics
  - `export` - Export results
  - `clear` - Clear session cache
  - `help` - Show commands

- **Batch Processing Enhancements**
  - OSINT mode support
  - Reputation checking
  - Progress indicators
  - Success/failure tracking

- **Export Formats**
  - JSON export
  - CSV export
  - TXT export
  - Session results export

- **Text Scanning**
  - Extract numbers from text files
  - Phone number pattern matching
  - Bulk extraction

#### Technical Implementation

- **scraper.go**
  - Concurrent goroutines
  - HTTP client with timeouts
  - Result aggregation
  - Error handling
  - JSON output

- **Threading**
  - Loading animations
  - Concurrent operations
  - Non-blocking UI

- **Color-coded Output**
  - ANSI color codes
  - Status indicators
  - Visual hierarchy

- **Global requirements.txt**
  - Centralized dependencies
  - Version specifications
  - Easy maintenance

### Changed

- Enhanced output format with sections
- Improved error messages
- Better progress feedback
- Organized command structure

### Fixed

- Stderr/stdout separation for clean output
- Unicode handling in terminal
- Cross-platform path handling
- Permission issues with installer

---

## [1.0.0] - 2025-09-15 (Estimated)

### 🎉 Initial Release

**Created by:** DezTheJackal

First public release of PhoneBookLOCA - Phone Number Location Lookup Tool.

### Added

#### Core Features

- Phone number validation using phonenumbers library
- Geographic location lookup (country, region, city)
- Carrier/provider identification
- Number type detection (mobile, landline, toll-free, etc.)
- Timezone identification
- Format variants (E164, International, National, RFC3966)
- Regional information (country codes, region codes)

#### Usage Modes

- Single number lookup
- Interactive mode
- Basic batch processing
- Command-line interface

#### Output Formats

- Console output with colors
- JSON output
- Basic CSV export
- Plain text export

#### Dependencies

- phonenumbers library for core functionality
- requests library for HTTP
- Python 3.6+ support

### Architecture

- `PhoneIntel` class for main logic
- `Colors` class for ANSI codes
- Argument parsing with argparse
- Error handling and validation

---

## Version Comparison

| Feature | v1.0 | v1.1 | v2.0 |
|---------|------|------|------|
| Basic lookup | ✅ | ✅ | ✅ |
| Validation | ✅ | ✅ | ✅ |
| Location | ✅ | ✅ | ✅ |
| Carrier | ✅ | ✅ | ✅ Enhanced |
| Type detection | ✅ | ✅ | ✅ Enhanced |
| OSINT queries | ❌ | ✅ | ✅ |
| Web scanning | ❌ | ✅ | ✅ |
| Reputation | ❌ | Basic | ✅ Advanced |
| VoIP detection | ❌ | ✅ | ✅ Enhanced |
| API integration | ❌ | ✅ | ✅ |
| Installer | ❌ | ✅ | ✅ |
| Caching | ❌ | ❌ | ✅ SQLite |
| Risk scoring | ❌ | ❌ | ✅ ML-powered |
| Rich UI | ❌ | ❌ | ✅ Optional |
| Performance | Good | Good | ⚡ Excellent |

---

## Upcoming Features

### v2.1 (Planned)

- HLR/HLR Lookup integration for live network status
- Social media deep scan with profile discovery
- Data breach intelligence integration
- Enhanced geolocation with historical tracking
- Export format: PDF reports
- Export format: HTML reports

### v2.2 (Planned)

- Real-time monitoring system
- Alert configuration
- Webhook notifications
- Email alerts
- Monitoring dashboard

### v3.0 (Future)

- Web interface (Flask/FastAPI)
- REST API server
- Plugin architecture
- Maltego integration
- Machine learning models
- Relationship mapping
- Network graph visualization
- Advanced analytics dashboard

---

## Contributors

- **v1.0**: DezTheJackal (Original author)
- **v1.1**: 0xb0rn3 | oxbv1 (OSINT features, installer, web scanner)
- **v2.0**: 0xb0rn3 | oxbv1 (Professional platform transformation)

---

## Links

- **Repository**: https://github.com/DezTheJackal/PhoneBookLOCA
- **Issues**: https://github.com/DezTheJackal/PhoneBookLOCA/issues
- **Documentation**: README.md, CONTRIBUTORS.md, MIGRATION_v2.0.md

---

<div align="center">

**PhoneBookLOCA** - From basic lookup to professional OSINT platform

*For educational and authorized security research only*

</div>
