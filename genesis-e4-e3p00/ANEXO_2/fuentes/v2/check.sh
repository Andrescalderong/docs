#!/bin/bash
# Uso: v2/check.sh sNN [opciones de check_cap]   (expande macros y verifica sec/sNN.md)
A2=/tmp/claude-0/-home-user-docs/8ca5c040-2adb-56b3-8e64-05d4e7e569ed/scratchpad/a2
f=$1; shift
python3 $A2/v2/expand.py $A2/sec/$f.md >/dev/null || exit 1
python3 -I $A2/build/check_cap.py $A2/out_md/$f.md "$@"
