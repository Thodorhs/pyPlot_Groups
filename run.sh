#!/bin/bash
python3 plot_data.py
epstopdf plot.eps --outfile=plot.pdf 
pdfcrop plot.pdf
