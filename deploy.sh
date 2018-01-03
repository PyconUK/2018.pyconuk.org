#!/usr/bin/env bash

set -o errexit
set -o nounset

./build.sh
git checkout gh-pages
git add .
git commit -m "[skip ci] Auto-commit. Build latest changes."
git push origin gh-pages
