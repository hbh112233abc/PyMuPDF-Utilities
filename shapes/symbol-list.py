# -*- coding: utf-8 -*-
from __future__ import print_function

"""
Created on Sun Dec  9 08:34:06 2018

@author: Jorj
@license: GNU GPL 3.0+

Create a list of available symbols defined in shapes_and_symbols.py

This also demonstrates an example usage: how these symbols could be used
as bullet-point symbols in some text.

"""

import fitz
import shapes_and_symbols as sas

# list of available symbol functions and their descriptions
tlist = [
    (sas.arrow, "arrow (easy)"),
    (sas.caro, "caro (easy)"),
    (sas.clover, "clover (easy)"),
    (sas.diamond, "diamond (easy)"),
    (sas.dontenter, "do not enter (medium)"),
    (sas.frowney, "frowney (medium)"),
    (sas.hand, "hand (complex)"),
    (sas.heart, "heart (easy)"),
    (sas.pencil, "pencil (very complex)"),
    (sas.smiley, "smiley (easy)"),
]

r = fitz.Rect(50, 50, 100, 100)  # first rect to contain a symbol
d = fitz.Rect(0, r.height + 10, 0, r.height + 10)  # displacement to next ret
p = (15, -r.height * 0.2)  # starting point of explanation text
rlist = [r]  # rectangle list

for i in range(1, len(tlist)):  # fill in all the rectangles
    rlist.append(rlist[i - 1] + d)

doc = fitz.open()  # create empty PDF
page = doc.newPage()  # create an empty page
img = page.newShape()  # start a Shape (canvas)

for i, r in enumerate(rlist):
    tlist[i][0](img, rlist[i])  # execute symbol creation
    img.insertText(
        rlist[i].br + p, tlist[i][1], fontsize=r.height / 1.2  # insert description text
    )

# store everything to the page's /Contents object
img.commit()

import os

scriptdir = os.path.dirname(__file__)
doc.save(os.path.join(scriptdir, "symbol-list.pdf"))  # save the PDF