#!/usr/bin/env bash

set -e -x
shopt -s extglob
cd "$(dirname "$(realpath "${BASH_SOURCE[0]}")")"

randovania_version=7.4.0

echo "Installing Requirements"
python -m pip install randovania==$randovania_version cryptography

echo "Copying Jekyll source"
echo "version: $randovania_version" >> _data/rdv.yml
rm -rf build
mkdir build
cp -ar !(build) build
echo "Building video database pages"
mkdir videos
python -m randovania database export-videos --output-dir videos

# insanely ugly hack!!! refactor ASAP!!!
declare -A games
games["Another Metroid 2 Remake"]=am2r
games["Cave Story"]=cave_story
games["Metroid Dread"]=dread
games["Metroid Prime"]=prime1
games["Metroid Prime 2 Echoes"]=prime2
games["Metroid Prime 3 Corruption"]=prime3
games["Metroid Samus Returns"]=samus_returns
games["Super Metroid"]=super_metroid

for i in "${!games[@]}"
do
    long="$i"
    short="${games[$i]}"
    mkdir -p "build/games/$short/videos"
    cp -ar "videos/$long/." "build/games/$short/videos"
done
