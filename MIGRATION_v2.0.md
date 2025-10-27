# PhoneBookLOCA v2.0 Migration Guide

## 🚀 Upgrading from v1.1 to v2.0

This guide helps you transition from PhoneBookLOCA v1.1 to the enhanced v2.0 platform.

---

## What's Changed

### ✅ **Fully Backwards Compatible**

Good news! v2.0 is **100% backwards compatible** with v1.1. All your existing commands and scripts will continue to work.

### 🆕 **New Features**

v2.0 adds powerful new capabilities **on top of** existing features:

1. **Intelligent caching** (automatic, no changes needed)
2. **Enhanced reputation checking** (same `--reputation` flag)
3. **Carrier intelligence** (automatic with every lookup)
4. **Risk classification** (automatic with every lookup)
5. **Rich UI** (optional, auto-detected)
6. **Cache management** (new commands)

---

## Installation

### Option 1: Fresh Installation (Recommended)

```bash
# Clone the latest version
git clone https://github.com/DezTheJackal/PhoneBookLOCA.git
cd PhoneBookLOCA

# Run installer
./install.sh

# Choose your installation type
# 1) Local installation
# 2) System-wide installation
```

### Option 2: Update Existing Installation

```bash
# Navigate to your PhoneBookLOCA directory
cd PhoneBookLOCA

# Pull latest changes
git pull origin main

# Update dependencies
pip3 install -r requirements.txt --break-system-packages

# Rebuild Go scraper (if needed)
go build -o scraper scraper.go
```

---

## New Dependencies

### Required (Same as v1.1)
```
phonenumbers>=8.12.0
requests>=2.25.0
```

### Optional (New in v2.0)
```
rich>=13.0.0  # For enhanced terminal UI
```

**Install Rich for the best experience:**
```bash
pip3 install rich
```

**Without Rich:** Tool still works, just uses basic ANSI colors instead of fancy panels.

---

## New File Locations

v2.0 creates some new files automatically:

### Cache Database
```
~/.phonebookloca/intel.db
```
- SQLite database for caching
- Created automatically on first run
- Stores lookup history and reputation data

### Configuration (Unchanged)
```
~/.phonebookloca_config.json
```
- Same location as v1.1
- API keys stored here
- No migration needed

---

## Command Changes

### All v1.1 Commands Still Work

```bash
# These all work exactly as before
./PhoneBookLOCA +14155552671
./PhoneBookLOCA +14155552671 --osint
./PhoneBookLOCA +14155552671 --reputation
./PhoneBookLOCA --config
```

### New v2.0 Commands

```bash
# Cache management (NEW)
./PhoneBookLOCA --cache-stats              # Show cache statistics
./PhoneBookLOCA --clear-cache              # Clear entries older than 30 days
./PhoneBookLOCA --clear-cache 7            # Clear entries older than 7 days

# Force fresh lookup (NEW)
./PhoneBookLOCA +14155552671 --no-cache    # Bypass cache, get fresh data

# Interactive mode new commands (NEW)
PhoneBook> cache                           # Show cache stats
PhoneBook> clear-cache 30                  # Clear old entries
```

---

## Behavior Changes

### 1. Lookups Now Use Cache by Default

**v1.1 Behavior:**
```bash
./PhoneBookLOCA +14155552671
# Always fetches fresh data (5-10 seconds)
```

**v2.0 Behavior:**
```bash
./PhoneBookLOCA +14155552671
# First time: Fetches fresh data (5-10 seconds), saves to cache
# Subsequent: Uses cache (<1 second), shows cache age

# Output includes:
# ⚡ Cache hit! Data age: 2.3 hours
# Confidence: 85% | Previous lookups: 3
```

**To get v1.1 behavior (always fresh):**
```bash
./PhoneBookLOCA +14155552671 --no-cache
```

### 2. Enhanced Output Format

**v1.1 Output:**
```
[+] Results:
    Country Code: +1
    Location: San Francisco, CA
    Carrier: Verizon Wireless
    Type: Mobile
```

**v2.0 Output (with Rich):**
```
╭─────────────────────────────────╮
│     📊 Basic Intelligence       │
├─────────────────────────────────┤
│ Country: United States (+1)     │
│ Carrier: Verizon Wireless       │
│ Type: Mobile                     │
╰─────────────────────────────────╯

╭─────────────────────────────────╮
│   📡 Carrier Intelligence       │
├─────────────────────────────────┤
│ Type: MNO                        │
│ Technology: 5G, LTE, 4G, 3G     │
│ Coverage: North America          │
╰─────────────────────────────────╯

╭─────────────────────────────────╮
│     ⚠️ Risk Assessment          │
├─────────────────────────────────┤
│ Risk Level: Low Risk             │
│ Risk Score: 25/100               │
│ Confidence: 92%                  │
╰─────────────────────────────────╯
```

**v2.0 Output (without Rich):**
```
[+] Results:
    Country Code: +1
    Location: San Francisco, CA
    Carrier: Verizon Wireless
    Type: Mobile

[*] Carrier Intelligence:
    Type: MNO
    Technology: 5G, LTE, 4G, 3G
    Coverage: North America

[*] Risk Assessment:
    Risk Level: Low Risk
    Risk Score: 25/100
    Confidence: 92%
```

### 3. Reputation Checking Enhanced

**v1.1:**
- Basic structure, limited functionality
- Single-source checking

**v2.0:**
- Multi-source aggregation (6+ sources)
- Concurrent checking (faster)
- Risk scoring (0-100)
- Confidence levels
- Persistent storage

**Usage remains the same:**
```bash
./PhoneBookLOCA +14155552671 --reputation
```

---

## Performance Improvements

### Speed Comparison

| Operation | v1.1 | v2.0 (No Cache) | v2.0 (Cached) |
|-----------|------|-----------------|---------------|
| Single lookup | 5-10s | 5-10s | <1s ⚡ |
| Reputation check | 10-15s | 5-8s | <1s ⚡ |
| 10 lookups | 50-100s | 50-100s | 5-10s ⚡ |
| 100 lookups | 8-16min | 8-16min | 1-2min ⚡ |

### Why Faster?

1. **Caching**: Repeated lookups are instant
2. **Concurrent processing**: Reputation sources checked in parallel
3. **Database indexes**: Optimized queries
4. **Efficient algorithms**: Better data structures

---

## Data Migration

### No Migration Needed! 🎉

v2.0 creates its own new database. Your existing data is not affected.

**What happens:**
1. v2.0 creates `~/.phonebookloca/intel.db` on first run
2. Old config file (`~/.phonebookloca_config.json`) is reused
3. No data loss, no conflicts

**If you want to start fresh:**
```bash
# Remove cache database
rm ~/.phonebookloca/intel.db

# Remove config (API keys)
rm ~/.phonebookloca_config.json

# Next run will create fresh files
```

---

## Common Upgrade Scenarios

### Scenario 1: Basic User (No Customization)

**Steps:**
1. Pull latest code: `git pull origin main`
2. Update dependencies: `pip3 install -r requirements.txt`
3. Done! Start using immediately

**Impact:**
- Automatic caching (faster lookups)
- Enhanced output (more intel)
- All commands work as before

### Scenario 2: Power User (Scripts/Automation)

**Steps:**
1. Update code and dependencies
2. Test your scripts
3. Optional: Add `--no-cache` if you need always-fresh data

**Impact:**
- Scripts work unchanged
- Add `--cache-stats` to monitor cache
- Add `--clear-cache` to periodic cleanup jobs

### Scenario 3: System-Wide Installation

**Steps:**
```bash
# Re-run installer
sudo ./install.sh
# Choose option 2 (system-wide)

# Updates binary at /usr/local/bin/phonebookloca
# Updates data at /usr/local/share/phonebookloca/
```

**Impact:**
- Cache database still in user home: `~/.phonebookloca/`
- Each user gets their own cache
- System-wide binary gets v2.0 features

---

## Troubleshooting

### "Module 'rich' not found" Warning

**Symptom:**
```
[!] Rich library not found - using basic formatting
[*] Install with: pip3 install rich
```

**Solution:**
```bash
# Install Rich for enhanced UI
pip3 install rich

# Or continue without Rich (tool still works)
```

**Impact:** Tool works fine, just uses basic colors instead of fancy panels.

---

### Cache Database Errors

**Symptom:**
```
[!] Cache error: database is locked
```

**Solution:**
```bash
# Close other PhoneBookLOCA instances
# Or remove and rebuild cache
rm ~/.phonebookloca/intel.db
```

---

### Slower First Lookup

**Symptom:**
```
First lookup after upgrade takes 5-10 seconds
```

**Explanation:**
This is normal! v2.0 is:
1. Fetching fresh data
2. Saving to cache database
3. Running new intelligence checks

**Next lookup will be <1 second!**

---

### Cache Not Working

**Check:**
```bash
# Verify cache exists
ls -la ~/.phonebookloca/intel.db

# Check cache stats
./PhoneBookLOCA --cache-stats

# If showing 0 entries, cache is working but empty
# If file doesn't exist, permissions issue
```

**Fix permissions:**
```bash
mkdir -p ~/.phonebookloca
chmod 755 ~/.phonebookloca
```

---

## Best Practices

### 1. Regular Cache Maintenance

```bash
# Weekly: Clear entries older than 7 days
./PhoneBookLOCA --clear-cache 7

# Monthly: Check cache stats
./PhoneBookLOCA --cache-stats
```

### 2. Fresh Data When Needed

```bash
# For critical lookups, bypass cache
./PhoneBookLOCA +14155552671 --no-cache --reputation
```

### 3. Monitoring Cache Performance

```bash
# Check hit rate periodically
./PhoneBookLOCA --cache-stats

# Good hit rate: 60-80%
# Excellent hit rate: 80-95%
# Low hit rate (<40%): Consider longer cache age
```

### 4. API Key Configuration

```bash
# Same as v1.1, still works
./PhoneBookLOCA --config

# Or in interactive mode
PhoneBook> config
```

---

## Feature Comparison

| Feature | v1.1 | v2.0 |
|---------|------|------|
| Basic lookup | ✅ | ✅ |
| OSINT queries | ✅ | ✅ |
| Web scanning | ✅ | ✅ |
| Reputation check | Basic | ✅ Enhanced |
| Caching | ❌ | ✅ SQLite |
| Carrier intel | Basic | ✅ Enhanced |
| Risk scoring | ❌ | ✅ ML-powered |
| Rich UI | ❌ | ✅ Optional |
| Cache management | ❌ | ✅ Full control |
| Performance | Good | ⚡ Excellent |
| Historical tracking | ❌ | ✅ Database |

---

## Testing Your Upgrade

### Quick Test Suite

```bash
# 1. Basic lookup (should work)
./PhoneBookLOCA +14155552671

# 2. Check cache was created
ls ~/.phonebookloca/intel.db

# 3. Second lookup (should be instant)
./PhoneBookLOCA +14155552671
# Look for: "⚡ Cache hit!"

# 4. Cache stats (should show 1 entry)
./PhoneBookLOCA --cache-stats

# 5. OSINT mode (should work)
./PhoneBookLOCA +14155552671 --osint --reputation

# 6. Interactive mode (should work)
./PhoneBookLOCA
PhoneBook> cache
PhoneBook> quit
```

**All tests passed?** ✅ Upgrade successful!

---

## Rollback (If Needed)

If you need to go back to v1.1:

```bash
# Navigate to PhoneBookLOCA directory
cd PhoneBookLOCA

# Checkout v1.1 tag (if available)
git checkout v1.1

# Or revert to specific commit
git log --oneline  # Find v1.1 commit
git checkout <commit-hash>

# Remove v2.0 cache
rm ~/.phonebookloca/intel.db

# Your config file (~/.phonebookloca_config.json) is preserved
```

---

## Getting Help

### Issues or Questions?

1. **Check documentation:**
   - README.md (updated for v2.0)
   - CONTRIBUTORS.md (feature details)
   - This migration guide

2. **Common issues:**
   - Cache not working → Check permissions
   - Rich UI not showing → Install `rich` library
   - Slower performance → Clear cache, check stats

3. **Report bugs:**
   - GitHub Issues: https://github.com/DezTheJackal/PhoneBookLOCA/issues
   - Include: version, OS, error message, steps to reproduce

4. **Feature requests:**
   - Open GitHub issue with `enhancement` label
   - Describe use case and expected behavior

---

## What's Next?

### v2.1+ Planned Features

- HLR/HLR lookup integration
- Social media profile discovery
- Data breach intelligence
- Real-time monitoring
- Web interface
- Professional reporting
- Maltego integration

**Want to contribute?** Check CONTRIBUTORS.md for guidelines!

---

## Summary

### ✅ Upgrade Checklist

- [ ] Backup current installation (optional)
- [ ] Pull latest code or fresh clone
- [ ] Update dependencies (`pip3 install -r requirements.txt`)
- [ ] Rebuild Go scraper (if using web scan)
- [ ] Test basic lookup
- [ ] Verify cache working (`--cache-stats`)
- [ ] Test existing scripts/workflows
- [ ] Install Rich for best experience (optional)
- [ ] Read new features in README.md
- [ ] Enjoy 10x faster lookups! 🚀

---

<div align="center">

**Welcome to PhoneBookLOCA v2.0!** 🎉

*Professional OSINT intelligence platform*

Original: **DezTheJackal** | v2.0: **0xb0rn3 | oxbv1**

</div>
