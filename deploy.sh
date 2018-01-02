#!/usr/bin/env bash

set -o errexit
set -o nounset

git checkout gh-pages
./build.sh
git add .
git commit -m "[skip ci] Auto-commit. Build latest changes."
git push origin gh-pages
