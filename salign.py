#! /usr/bin/env python 3

import os
import sublime
import sublime_plugin

dirpath = os.path.dirname(os.path.abspath(__file__))
cmdPath = os.path.join(dirpath, 'src/align_selections.py')

exec(open(cmdPath).read( ))





class AlignCommand(sublime_plugin.TextCommand):

	def run(self, edit):

		if len(self.view.sel( )) > 0:
			align_selections(self, edit)
