#!/usr/bin/env python
# coding=utf-8

from reportlab.lib import colors
from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF


data = [
    # YR   MO PREDICTED HIGH   LOW
    (2014, 1, 137.1, 138.1, 136.1),
    (2014, 2, 138.5, 139.5, 137.5),
    (2014, 3, 140.3, 142.3, 138.3),
    (2014, 4, 141.3, 144.3, 138.3),
    (2014, 5, 140.3, 144.3, 136.3),
    (2014, 6, 138.5, 142.5, 134.5),
    (2014, 7, 136.2, 141.2, 131.2),
    (2014, 8, 132.8, 138.8, 126.8),
    (2014, 9, 129.6, 136.6, 122.6),
    (2014, 10, 127.5, 135.5, 119.5),
    (2014, 11, 126.0, 134.0, 118.0),
    (2014, 12, 125.3, 134.3, 116.3),
]

drawing = Drawing(200, 150)

pred = [row[2]-60 for row in data]
high = [row[3]-60 for row in data]
low = [row[4]-60 for row in data]
times = [10 * row[1] + 30 for row in data]

drawing.add(PolyLine(zip(times, pred), strokeColor=colors.blue))
drawing.add(PolyLine(zip(times, high), strokeColor=colors.red))
drawing.add(PolyLine(zip(times, low), strokeColor=colors.green))
drawing.add(String(60, 120, 'Sunspots', fontSize=15, fillColor=colors.red))

renderPDF.drawToFile(drawing, 'report1.pdf', 'Sunspots')
