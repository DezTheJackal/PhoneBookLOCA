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
