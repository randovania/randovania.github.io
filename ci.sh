#!/usr/bin/env bash

set -e -x
shopt -s extglob
cd "$(dirname "$(realpath "${BASH_SOURCE[0]}")")"

randovania_version=8.6.0
echo "Installing Requirements"

# python -m pip install randovania[website]==$randovania_version
# FIXME: hack for missing README
python -m pip download randovania==$randovania_version --no-deps --no-binary randovania
tar xf randovania-$randovania_version.tar.gz
python -m pip install -e ./randovania-$randovania_version[website]

echo "Building video database pages"
rm -rf _videos
mkdir _videos
python -m randovania development export-videos-yaml --output-dir _videos --as-frontmatter

echo "Copying readme sections"
rm -rf _includes/_readme
mkdir _includes/_readme
for section in WELCOME CREDITS
do python -m randovania development export-readme-section --section $section --output-dir _includes/_readme
done

echo "Extracting game data"
rm -rf assets/games
rm -rf _games
mkdir assets/games
mkdir _games
python -m randovania development extract-game-data --games-dir _games --covers-dir assets/games

# Remove the extracted randovania so we don't accidentally deploy it
rm -rf ./randovania-$randovania_version ./randovania-$randovania_version.tar.gz 

echo "Copying Jekyll source"
echo "version: $randovania_version" > _data/rdv.yml
rm -rf build
mkdir build
cp -ar !(build) build
