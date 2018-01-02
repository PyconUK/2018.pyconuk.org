#!/usr/bin/env bash

set -o nounset

git branch -D gh-pages

set -o errexit
git checkout -b gh-pages
./build.sh
git add .
git commit -m "[skip ci] Auto-commit. Build latest changes."
git push origin gh-pages -f
