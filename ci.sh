#!/usr/bin/env bash

set -e -x
cd "$(dirname "$(realpath "${BASH_SOURCE[0]}")")"

randovania_version=6.1.0

echo "Installing Requirements"
python -m pip install randovania==$randovania_version cryptography

echo "Building html pages"
rm -rf build
python -m randovania database export-videos --output-dir build
cp -ar static_website/* build/
sed -i "s/{VERSION_TEMPLATE}/${randovania_version}/g" "build/install randovania.htm"
cp _config.yml build
