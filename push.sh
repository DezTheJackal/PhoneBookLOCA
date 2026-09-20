#!/bin/bash
#
# push.sh - Stage, commit, tag and push a PhoneBookLOCA release.
# Uses YOUR git credentials/remote - this script cannot push on its own
# behalf, it just automates the commands you'd otherwise run by hand.
#
# Usage:
#   ./push.sh "commit message"
#   ./push.sh "commit message" v2.3.0     # also creates and pushes a tag
#
set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

MESSAGE="$1"
TAG="$2"

if [ -z "$MESSAGE" ]; then
    echo -e "${RED}[!] Usage: ./push.sh \"commit message\" [tag]${NC}"
    exit 1
fi

if ! git rev-parse --is-inside-work-tree &>/dev/null; then
    echo -e "${RED}[!] Not inside a git repository.${NC}"
    exit 1
fi

echo -e "${CYAN}[*] Current status:${NC}"
git status --short

if [ -z "$(git status --porcelain)" ]; then
    echo -e "${YELLOW}[!] Nothing to commit - working tree is clean.${NC}"
    exit 0
fi

echo ""
read -p "Stage all changes and commit with this message? [y/N] " CONFIRM
if [[ ! "$CONFIRM" =~ ^[Yy]$ ]]; then
    echo -e "${YELLOW}[*] Aborted.${NC}"
    exit 0
fi

git add -A
git commit -m "$MESSAGE"
echo -e "${GREEN}[+] Committed.${NC}"

if [ -n "$TAG" ]; then
    if git rev-parse "$TAG" &>/dev/null; then
        echo -e "${YELLOW}[!] Tag $TAG already exists - skipping tag creation.${NC}"
    else
        git tag -a "$TAG" -m "$MESSAGE"
        echo -e "${GREEN}[+] Tagged $TAG.${NC}"
    fi
fi

BRANCH=$(git rev-parse --abbrev-ref HEAD)
echo -e "${CYAN}[*] Pushing branch '$BRANCH' to origin...${NC}"
git push origin "$BRANCH"

if [ -n "$TAG" ]; then
    echo -e "${CYAN}[*] Pushing tag '$TAG'...${NC}"
    git push origin "$TAG"
fi

echo -e "${GREEN}[+] Done.${NC}"
