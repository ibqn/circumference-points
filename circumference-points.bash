#!/usr/bin/env bash

set -e

source './venv/bin/activate'

exec python3 circumference-points.py $@
