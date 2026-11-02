#!/bin/bash
# uso: _vista.sh nombre...  -> genera scratchpad/vista_a2/nombre.jpg (fondo blanco) para inspección
cd /tmp/claude-0/-home-user-docs/8ca5c040-2adb-56b3-8e64-05d4e7e569ed/scratchpad/a2/figs
python3 - "$@" <<'PY'
import sys
sys.path.insert(0,'.')
import ver
for n in sys.argv[1:]:
    print(ver.ver(f'out/{n}.png', out=f'/tmp/claude-0/-home-user-docs/8ca5c040-2adb-56b3-8e64-05d4e7e569ed/scratchpad/vista_a2/{n}.jpg', ancho=1600))
PY
