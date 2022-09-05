#!/usr/bin/env bash

set -e -x
cd "$(dirname "$(realpath "${BASH_SOURCE[0]}")")"

echo "Installing Requirements"
python -m pip install --upgrade -r requirements.txt

echo "Building html pages"
rm -rf build
python -m randovania database export-videos --output-dir build
cp README.md build
cp _config.yml build
