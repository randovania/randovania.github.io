#!/usr/bin/env bash

set -e -x
shopt -s extglob
cd "$(dirname "$(realpath "${BASH_SOURCE[0]}")")"

echo "Building video database pages"
rm -rf _videos
mkdir _videos
uv run randovania development export-videos-yaml --output-dir _videos --as-frontmatter

echo "Copying readme sections"
rm -rf _includes/_readme
mkdir _includes/_readme
for section in WELCOME CREDITS
do uv run randovania development export-readme-section --section $section --output-dir _includes/_readme
done

echo "Extracting game data"
rm -rf assets/games
rm -rf _games
mkdir assets/games
mkdir _games
uv run randovania development extract-game-data --games-dir _games --covers-dir assets/games

echo "Copying Jekyll source"
echo "version: $(uv run -q python -c "import randovania; print(randovania.VERSION)")" > _data/rdv.yml
rm -rf build
mkdir build
cp -ar !(build) build
