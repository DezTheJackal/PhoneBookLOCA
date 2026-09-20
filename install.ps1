<#
.SYNOPSIS
    PhoneBookLOCA v2.3.0 - Native Windows Installer (PowerShell)
    Original tool by: DezTheJackal

.DESCRIPTION
    Installs Python dependencies and (optionally) puts PhoneBookLOCA on PATH
    as a `phonebookloca` command. Equivalent to install.sh for Linux/macOS.

.EXAMPLE
    powershell -ExecutionPolicy Bypass -File install.ps1
#>

$ErrorActionPreference = "Stop"

function Write-Info($msg)  { Write-Host "[*] $msg" -ForegroundColor Yellow }
function Write-Ok($msg)    { Write-Host "[+] $msg" -ForegroundColor Green }
function Write-Err($msg)   { Write-Host "[!] $msg" -ForegroundColor Red }

Write-Host ""
Write-Host "===================================================" -ForegroundColor Cyan
Write-Host "  PhoneBookLOCA v2.3.0 - Windows Installer          " -ForegroundColor Magenta
Write-Host "===================================================" -ForegroundColor Cyan
Write-Host ""

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ScriptDir

# --- Check Python -----------------------------------------------------
Write-Info "Checking Python installation..."
$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) { $python = Get-Command python3 -ErrorAction SilentlyContinue }

if (-not $python) {
    Write-Err "Python 3 was not found on PATH."
    Write-Host "Install it from https://www.python.org/downloads/ (check 'Add python.exe to PATH') then re-run this script."
    exit 1
}

$pyExe = $python.Source
$pyVersion = & $pyExe --version
Write-Ok "Found $pyVersion at $pyExe"

# --- Install dependencies ---------------------------------------------
Write-Info "Installing Python dependencies from requirements.txt..."
try {
    & $pyExe -m pip install -r requirements.txt
    Write-Ok "Dependencies installed"
} catch {
    Write-Err "pip install failed: $_"
    Write-Host "Try manually: $pyExe -m pip install -r requirements.txt"
    exit 1
}

# --- Optional: build the Go OSINT scraper ------------------------------
$go = Get-Command go -ErrorAction SilentlyContinue
if ($go -and (Test-Path "scraper.go")) {
    Write-Info "Go found - building scraper.exe..."
    & go build -o scraper.exe scraper.go
    if ($LASTEXITCODE -eq 0) {
        Write-Ok "Built scraper.exe"
    } else {
        Write-Err "Go build failed (optional feature - continuing)"
    }
} else {
    Write-Info "Go not found - skipping optional web scraper (all other features work fine)."
    Write-Host "  Install from https://go.dev/dl/ and re-run this script to enable it."
}

# --- Offer to add a `phonebookloca` shim on PATH ------------------------
Write-Host ""
$choice = Read-Host "Add a 'phonebookloca' command to your user PATH? [y/N]"
if ($choice -match '^[Yy]') {
    $installDir = Join-Path $env:LOCALAPPDATA "PhoneBookLOCA"
    New-Item -ItemType Directory -Force -Path $installDir | Out-Null
    Copy-Item -Recurse -Force "$ScriptDir\*" $installDir

    $shim = Join-Path $installDir "phonebookloca.cmd"
    "@echo off`r`n`"$pyExe`" `"$installDir\PhoneBookLOCA`" %*" | Set-Content -Encoding ASCII $shim

    $userPath = [Environment]::GetEnvironmentVariable("Path", "User")
    if ($userPath -notlike "*$installDir*") {
        [Environment]::SetEnvironmentVariable("Path", "$userPath;$installDir", "User")
        Write-Ok "Added $installDir to your user PATH (open a new terminal for it to take effect)"
    }
    Write-Ok "Installed. Run 'phonebookloca' from any new terminal window."
} else {
    Write-Info "Skipped. Run it in place with: $pyExe PhoneBookLOCA <number>"
}

Write-Host ""
Write-Ok "Installation complete!"
Write-Host "Quick start:"
Write-Host "  $pyExe PhoneBookLOCA +14155552671"
Write-Host "  $pyExe PhoneBookLOCA +14155552671 --geo --osint"
Write-Host "  $pyExe PhoneBookLOCA --le-mode"
Write-Host ""
