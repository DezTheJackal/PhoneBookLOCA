#!/bin/bash
#
# PhoneBookLOCA v1.1 - Installation & Build Script
# Original tool by: DezTheJackal
# Install script maintained by: 0xb0rn3 | oxbv1
#
# Multi-platform installer for all Linux distros, macOS, and Windows
# Features: System-wide installation, package manager detection, dependency auto-install
#

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
MAGENTA='\033[0;35m'
NC='\033[0m' # No Color

# Detect OS
detect_os() {
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        echo "linux"
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        echo "macos"
    elif [[ "$OSTYPE" == "cygwin" ]] || [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
        echo "windows"
    else
        echo "unknown"
    fi
}

# Detect Linux package manager
detect_package_manager() {
    if command -v pacman &> /dev/null; then
        echo "pacman"
    elif command -v apt &> /dev/null; then
        echo "apt"
    elif command -v dnf &> /dev/null; then
        echo "dnf"
    elif command -v yum &> /dev/null; then
        echo "yum"
    elif command -v zypper &> /dev/null; then
        echo "zypper"
    elif command -v apk &> /dev/null; then
        echo "apk"
    else
        echo "unknown"
    fi
}

# Check if running as root
is_root() {
    [ "$EUID" -eq 0 ]
}

OS=$(detect_os)
PKG_MANAGER=$(detect_package_manager)

echo -e "${BLUE}╔═══════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║  ${MAGENTA}PhoneBookLOCA v1.1${BLUE} - Installation & Build Script  ║${NC}"
echo -e "${BLUE}║  ${CYAN}Original: DezTheJackal${BLUE} | ${CYAN}Installer: 0xb0rn3${BLUE}      ║${NC}"
echo -e "${BLUE}╚═══════════════════════════════════════════════════════╝${NC}"
echo ""
echo -e "${YELLOW}[*] Detected OS: ${GREEN}$OS${NC}"
if [ "$OS" == "linux" ]; then
    echo -e "${YELLOW}[*] Package Manager: ${GREEN}$PKG_MANAGER${NC}"
fi
echo ""

# Get script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd "$SCRIPT_DIR"

# Check if requirements.txt exists
if [ ! -f "requirements.txt" ]; then
    echo -e "${RED}[!] requirements.txt not found in current directory${NC}"
    exit 1
fi

# Ask for installation type
echo -e "${CYAN}╔═══════════════════════════════════════════════════════╗${NC}"
echo -e "${CYAN}║  Installation Options                                 ║${NC}"
echo -e "${CYAN}╚═══════════════════════════════════════════════════════╝${NC}"
echo ""
echo -e "${YELLOW}Choose installation type:${NC}"
echo -e "  ${GREEN}1)${NC} Local installation (current directory only)"
echo -e "  ${GREEN}2)${NC} System-wide installation (available globally)"
echo ""
read -p "Enter choice [1-2]: " INSTALL_TYPE

SYSTEM_WIDE=false
if [ "$INSTALL_TYPE" == "2" ]; then
    SYSTEM_WIDE=true
    if ! is_root; then
        echo -e "${YELLOW}[!] System-wide installation requires root privileges${NC}"
        echo -e "${YELLOW}[*] Re-run with: sudo ./install.sh${NC}"
        exit 1
    fi
fi

echo ""

# Install Python if needed
echo -e "${YELLOW}[*] Checking Python installation...${NC}"
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
    echo -e "${GREEN}[✓] Python 3 found: $PYTHON_VERSION${NC}"
else
    echo -e "${RED}[!] Python 3 is not installed${NC}"
    echo -e "${YELLOW}[*] Attempting to install Python 3...${NC}"
    
    case $PKG_MANAGER in
        pacman)
            if is_root; then
                pacman -S --noconfirm python python-pip
            else
                echo -e "${YELLOW}[*] Run: sudo pacman -S python python-pip${NC}"
                exit 1
            fi
            ;;
        apt)
            if is_root; then
                apt update && apt install -y python3 python3-pip
            else
                echo -e "${YELLOW}[*] Run: sudo apt install python3 python3-pip${NC}"
                exit 1
            fi
            ;;
        dnf)
            if is_root; then
                dnf install -y python3 python3-pip
            else
                echo -e "${YELLOW}[*] Run: sudo dnf install python3 python3-pip${NC}"
                exit 1
            fi
            ;;
        yum)
            if is_root; then
                yum install -y python3 python3-pip
            else
                echo -e "${YELLOW}[*] Run: sudo yum install python3 python3-pip${NC}"
                exit 1
            fi
            ;;
        zypper)
            if is_root; then
                zypper install -y python3 python3-pip
            else
                echo -e "${YELLOW}[*] Run: sudo zypper install python3 python3-pip${NC}"
                exit 1
            fi
            ;;
        apk)
            if is_root; then
                apk add python3 py3-pip
            else
                echo -e "${YELLOW}[*] Run: sudo apk add python3 py3-pip${NC}"
                exit 1
            fi
            ;;
        *)
            echo -e "${RED}[!] Could not auto-install Python${NC}"
            echo -e "${YELLOW}[*] Please install Python 3.6+ manually${NC}"
            exit 1
            ;;
    esac
    
    echo -e "${GREEN}[✓] Python 3 installed${NC}"
fi

# Check pip
echo -e "${YELLOW}[*] Checking pip installation...${NC}"
if command -v pip3 &> /dev/null; then
    echo -e "${GREEN}[✓] pip3 found${NC}"
else
    echo -e "${RED}[!] pip3 is not installed${NC}"
    
    case $PKG_MANAGER in
        pacman)
            if is_root; then
                pacman -S --noconfirm python-pip
            else
                echo -e "${YELLOW}[*] Run: sudo pacman -S python-pip${NC}"
                exit 1
            fi
            ;;
        apt)
            if is_root; then
                apt install -y python3-pip
            else
                echo -e "${YELLOW}[*] Run: sudo apt install python3-pip${NC}"
                exit 1
            fi
            ;;
        *)
            echo -e "${YELLOW}[*] Trying to install pip via Python...${NC}"
            python3 -m ensurepip --upgrade
            ;;
    esac
fi

# Install Python dependencies from global requirements.txt
echo ""
echo -e "${YELLOW}[*] Installing Python dependencies from requirements.txt...${NC}"
echo -e "${CYAN}    Using global requirements.txt from: $SCRIPT_DIR/requirements.txt${NC}"

INSTALL_SUCCESS=false

# Try different installation methods
if $SYSTEM_WIDE; then
    # System-wide installation
    if pip3 install -r requirements.txt &> /dev/null; then
        echo -e "${GREEN}[✓] Python dependencies installed system-wide${NC}"
        INSTALL_SUCCESS=true
    elif pip3 install -r requirements.txt --break-system-packages &> /dev/null; then
        echo -e "${GREEN}[✓] Python dependencies installed (--break-system-packages)${NC}"
        INSTALL_SUCCESS=true
    else
        echo -e "${RED}[!] Failed to install dependencies${NC}"
        exit 1
    fi
else
    # Local installation
    if pip3 install --user -r requirements.txt &> /dev/null; then
        echo -e "${GREEN}[✓] Python dependencies installed locally${NC}"
        INSTALL_SUCCESS=true
    elif pip3 install --user -r requirements.txt --break-system-packages &> /dev/null; then
        echo -e "${GREEN}[✓] Python dependencies installed (--break-system-packages)${NC}"
        INSTALL_SUCCESS=true
    elif pip3 install -r requirements.txt --break-system-packages &> /dev/null; then
        echo -e "${GREEN}[✓] Python dependencies installed${NC}"
        INSTALL_SUCCESS=true
    else
        echo -e "${RED}[!] Failed to install dependencies${NC}"
        echo -e "${YELLOW}[*] Try manually: pip3 install -r requirements.txt --break-system-packages${NC}"
        exit 1
    fi
fi

# Make Python script executable
echo ""
echo -e "${YELLOW}[*] Making PhoneBookLOCA executable...${NC}"
chmod +x PhoneBookLOCA
echo -e "${GREEN}[✓] PhoneBookLOCA is now executable${NC}"

# Install system-wide if requested
if $SYSTEM_WIDE; then
    echo ""
    echo -e "${YELLOW}[*] Installing PhoneBookLOCA system-wide...${NC}"
    
    # Copy main script to /usr/local/bin
    cp PhoneBookLOCA /usr/local/bin/phonebookloca
    chmod +x /usr/local/bin/phonebookloca
    echo -e "${GREEN}[✓] Installed to: /usr/local/bin/phonebookloca${NC}"
    
    # Create data directory
    DATA_DIR="/usr/local/share/phonebookloca"
    mkdir -p "$DATA_DIR"
    
    # Copy supporting files
    if [ -f "scraper" ]; then
        cp scraper "$DATA_DIR/"
        chmod +x "$DATA_DIR/scraper"
        echo -e "${GREEN}[✓] Go scraper installed to: $DATA_DIR/scraper${NC}"
    fi
    
    # Update the main script to use system paths
    sed -i "s|Path(__file__).parent / 'scraper'|Path('$DATA_DIR/scraper')|g" /usr/local/bin/phonebookloca 2>/dev/null || \
    sed -i '' "s|Path(__file__).parent / 'scraper'|Path('$DATA_DIR/scraper')|g" /usr/local/bin/phonebookloca 2>/dev/null
    
    echo -e "${GREEN}[✓] System-wide installation complete${NC}"
    echo -e "${CYAN}[*] You can now run: ${GREEN}phonebookloca${CYAN} from anywhere${NC}"
fi

# Check if Go is installed (optional)
echo ""
echo -e "${YELLOW}[*] Checking for Go (optional - for web scraper)...${NC}"
if command -v go &> /dev/null; then
    GO_VERSION=$(go version 2>&1 | awk '{print $3}')
    echo -e "${GREEN}[✓] Go found: $GO_VERSION${NC}"
    
    # Build Go scraper
    echo -e "${YELLOW}[*] Building OSINT web scraper (Go)...${NC}"
    
    if [ -f "scraper.go" ]; then
        if go build -o scraper scraper.go; then
            echo -e "${GREEN}[✓] Go scraper built successfully: ./scraper${NC}"
            
            # Copy to system location if system-wide
            if $SYSTEM_WIDE; then
                cp scraper "$DATA_DIR/"
                chmod +x "$DATA_DIR/scraper"
                echo -e "${GREEN}[✓] Scraper installed to: $DATA_DIR/scraper${NC}"
            fi
            
            # Test the scraper
            echo -e "${YELLOW}[*] Testing scraper...${NC}"
            if ./scraper +14155552671 > /dev/null 2>&1; then
                echo -e "${GREEN}[✓] Scraper test passed!${NC}"
            else
                echo -e "${YELLOW}[!] Scraper test failed, but binary was created${NC}"
            fi
        else
            echo -e "${RED}[!] Go build failed${NC}"
        fi
    else
        echo -e "${RED}[!] scraper.go not found${NC}"
    fi
else
    echo -e "${YELLOW}[!] Go is not installed (optional)${NC}"
    echo -e "${YELLOW}[*] Web scraper (--web-scan) will not be available${NC}"
    echo -e "${YELLOW}[*] All other features will work fine${NC}"
    echo ""
    echo -e "${CYAN}To install Go:${NC}"
    
    case $PKG_MANAGER in
        pacman)
            echo -e "  ${GREEN}sudo pacman -S go${NC}"
            ;;
        apt)
            echo -e "  ${GREEN}sudo apt install golang-go${NC}"
            ;;
        dnf)
            echo -e "  ${GREEN}sudo dnf install golang${NC}"
            ;;
        yum)
            echo -e "  ${GREEN}sudo yum install golang${NC}"
            ;;
        zypper)
            echo -e "  ${GREEN}sudo zypper install go${NC}"
            ;;
        apk)
            echo -e "  ${GREEN}sudo apk add go${NC}"
            ;;
        *)
            if [ "$OS" == "macos" ]; then
                echo -e "  ${GREEN}brew install go${NC}"
            elif [ "$OS" == "windows" ]; then
                echo -e "  Download from: ${GREEN}https://golang.org/dl/${NC}"
            fi
            ;;
    esac
    
    echo ""
    echo -e "${YELLOW}[*] After installing Go, re-run this script to build the scraper${NC}"
fi

# Final message
echo ""
echo -e "${BLUE}╔═══════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║  ${GREEN}Installation Complete!${BLUE}                               ║${NC}"
echo -e "${BLUE}╚═══════════════════════════════════════════════════════╝${NC}"
echo ""
echo -e "${GREEN}[+] PhoneBookLOCA v1.1 is ready to use!${NC}"
echo ""

if $SYSTEM_WIDE; then
    echo -e "${MAGENTA}═══════════════════ SYSTEM-WIDE MODE ═══════════════════${NC}"
    echo -e "${YELLOW}Quick Start (from anywhere):${NC}"
    echo -e "  ${BLUE}phonebookloca${NC}                          # Interactive mode"
    echo -e "  ${BLUE}phonebookloca +14155552671${NC}            # Single lookup"
    echo -e "  ${BLUE}phonebookloca +14155552671 --osint${NC}    # OSINT mode"
    if command -v go &> /dev/null && [ -f "scraper" ]; then
        echo -e "  ${BLUE}phonebookloca +14155552671 --osint --web-scan${NC}  # With web scanner"
    fi
    echo ""
    echo -e "${CYAN}[*] Installed to: /usr/local/bin/phonebookloca${NC}"
    echo -e "${CYAN}[*] Data directory: $DATA_DIR${NC}"
else
    echo -e "${MAGENTA}════════════════════ LOCAL MODE ════════════════════════${NC}"
    echo -e "${YELLOW}Quick Start (from this directory):${NC}"
    echo -e "  ${BLUE}./PhoneBookLOCA${NC}                          # Interactive mode"
    echo -e "  ${BLUE}./PhoneBookLOCA +14155552671${NC}            # Single lookup"
    echo -e "  ${BLUE}./PhoneBookLOCA +14155552671 --osint${NC}    # OSINT mode"
    if command -v go &> /dev/null && [ -f "scraper" ]; then
        echo -e "  ${BLUE}./PhoneBookLOCA +14155552671 --osint --web-scan${NC}  # With web scanner"
    fi
    echo ""
    echo -e "${CYAN}[*] For system-wide installation, run: sudo ./install.sh${NC}"
fi

echo ""
echo -e "${YELLOW}Full Documentation:${NC}"
echo -e "  ${BLUE}cat README.md${NC}"
echo ""
echo -e "${GREEN}Happy hunting! 🔍${NC}"
echo -e "${CYAN}Original tool by: ${MAGENTA}DezTheJackal${NC}"
echo -e "${CYAN}v1.1 installer by: ${MAGENTA}0xb0rn3 | oxbv1${NC}"
echo ""
