#!/usr/bin/env bash

set -e -x
shopt -s extglob
cd "$(dirname "$(realpath "${BASH_SOURCE[0]}")")"

uv venv
source .venv/bin/activate
uv pip install randovania[website]==$(cat randovania-version.txt)
./build.sh