#!/bin/bash
# Compila las tres versiones y el libro de respaldo (en serie: comparten out_md/ y el puerto de LibreOffice)
A2=/tmp/claude-0/-home-user-docs/8ca5c040-2adb-56b3-8e64-05d4e7e569ed/scratchpad/a2
cd $A2
rm -f out/build_*.log
LO_DPI=96 python3 build/build_a2.py out/anexo2 > out/build_limpio.log 2>&1; echo "limpio: $?" > out/run_all.status
python3 build/build_a2.py out/anexo2_soporte --soporte --anexo > out/build_soporte.log 2>&1; echo "soporte: $?" >> out/run_all.status
python3 build/build_a2.py out/anexoA --solo-anexo > out/build_anexoA.log 2>&1; echo "anexoA: $?" >> out/run_all.status
python3 build/gen_xlsx_anexoA.py out/anexoA_respaldo.xlsx > out/build_xlsx.log 2>&1; echo "xlsx: $?" >> out/run_all.status
echo FIN >> out/run_all.status
