#! /usr/bin/env python 3

import sublime
import sublime_plugin





def filter_selections (positions):

	rows = { }

	for row, col in positions:

		if row in rows:
			rows[row] = min(rows[row], col)
		else:
			rows[row] = col

	return [(row, col) for row, col in rows.items( )]





def insertWhitespace(self, edit, selections, maxCol):

	for row, col in selections:

		point   = self.view.text_point(row, col)
		padding = ' ' * (maxCol - col)

		self.view.insert(edit, point, padding)





def align_selections (self, edit):

	selections      = self.view.sel( )
	cursorPositions = [ ]

	for region in selections:
		cursorPositions.append( self.view.rowcol(region.begin( )) )

	toAlign = filter_selections(cursorPositions)
	maxCol  = max(toAlign, key = lambda position: position[1])[1]

	insertWhitespace(self, edit, toAlign, maxCol)
