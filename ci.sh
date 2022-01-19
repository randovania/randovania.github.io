#!/usr/bin/env bash

set -e -x
cd "$(dirname "$(realpath "${BASH_SOURCE[0]}")")"

echo "Setting up venv"
python3.9 -m venv venv
source venv/bin/activate
python -c "import sys; assert sys.version_info[0:2] == (3, 9), 'Python 3.9 required'"

echo "Installing Requirements"
python -m pip install --upgrade -r requirements.txt

echo "Building html pages"
rm -rf build
python -m randovania database export-videos --output-dir build
cp README.md build
cp _config.yml build
