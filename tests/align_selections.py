#! /usr/bin/env python 3

import os

dirpath = os.path.dirname(os.path.abspath(__file__))
cmdPath = os.path.join(dirpath, '../src/align_selections.py')

exec(open(cmdPath).read( ))





actual = filter_selections([

	[0, 0],

	[1, 0],
	[1, 1],
	[1, 2],

	[2, 0],
	[2, 3],
	[2, 0],
	[2, 1],
	[2, 1]

])

for ith, (row, col) in enumerate(actual):

	assert row == ith
	assert col == 0
