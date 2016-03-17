#! /usr/bin/env python 3

import sublime
import sublime_plugin






# dsa:              asddsaasdsadsad
# dsaaaaaa:              asddsaasdsadsad
# dfs:              asddsaasdsadsad
# s:              asddsaasdsadsad
# dfssssssssss:              asddsaasdsadsad
# ds:              asddsaasdsadsad
# dfskdfkdsfkdsfk:              asddsaasdsadsad





def filterSelections (positions):

	rows = { }

	for row, col in positions:

		if row in rows:
			rows[row] = min(rows[row], col)
		else:
			rows[row] = col

	return [(row, col) for row, col in rows.items( )]





def alignSelections (self, edit):

	view            = self.view
	selections      = view.sel( )
	cursorPositions = [ ]

	for region in selections:
		cursorPositions.append( view.rowcol(region.begin( )) )

	toAlign = filterSelections(cursorPositions)
	maxCol  = max(toAlign, key = lambda position: position[1])[1]

	print( maxCol )



class AlignCommand(sublime_plugin.TextCommand):

	def run(self, edit):

		view       = self.view
		selection  = view.sel( )
		settings   = view.settings( )
		tab_size   = int(settings.get('tab_size', 8))
		use_spaces = settings.get('translate_tabs_to_spaces')

		if len(selection) > 0:
			alignSelections(self, edit)
