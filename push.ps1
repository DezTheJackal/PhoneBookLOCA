<#
.SYNOPSIS
    push.ps1 - Stage, commit, tag and push a PhoneBookLOCA release (Windows).
    Uses YOUR git credentials/remote - this script cannot push on its own
    behalf, it just automates the commands you'd otherwise run by hand.

.EXAMPLE
    .\push.ps1 -Message "v2.3.0: dormant features, cross-platform, bug fixes"
    .\push.ps1 -Message "v2.3.0" -Tag "v2.3.0"
#>

param(
    [Parameter(Mandatory=$true)][string]$Message,
    [string]$Tag
)

$ErrorActionPreference = "Stop"

function Info($m) { Write-Host "[*] $m" -ForegroundColor Cyan }
function Ok($m)   { Write-Host "[+] $m" -ForegroundColor Green }
function Warn($m) { Write-Host "[!] $m" -ForegroundColor Yellow }
function Err($m)  { Write-Host "[!] $m" -ForegroundColor Red }

try {
    git rev-parse --is-inside-work-tree | Out-Null
} catch {
    Err "Not inside a git repository."
    exit 1
}

Info "Current status:"
git status --short

$changes = git status --porcelain
if (-not $changes) {
    Warn "Nothing to commit - working tree is clean."
    exit 0
}

$confirm = Read-Host "`nStage all changes and commit with this message? [y/N]"
if ($confirm -notmatch '^[Yy]') {
    Warn "Aborted."
    exit 0
}

git add -A
git commit -m "$Message"
Ok "Committed."

if ($Tag) {
    $existing = git tag --list $Tag
    if ($existing) {
        Warn "Tag $Tag already exists - skipping tag creation."
    } else {
        git tag -a $Tag -m "$Message"
        Ok "Tagged $Tag."
    }
}

$branch = git rev-parse --abbrev-ref HEAD
Info "Pushing branch '$branch' to origin..."
git push origin $branch

if ($Tag) {
    Info "Pushing tag '$Tag'..."
    git push origin $Tag
}

Ok "Done."
