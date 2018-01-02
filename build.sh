#!/usr/bin/env bash

set -o errexit
set -o nounset

pip3 install -r requirements.txt

pyscss theme/style.scss > theme/static.css
