#!/bin/bash

python3 latex2pdf.py teamreport.csv schedule.tex out_schedule.tex
python3 latex2pdf.py teamreport.csv cover.tex out_cover.tex
python3 latex2pdf.py teamreport.csv id.tex out_id.tex

echo "Packets have been generated"

