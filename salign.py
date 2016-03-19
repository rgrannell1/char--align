#! /usr/bin/env python 3

import os
import sublime
import sublime_plugin

dirpath = os.path.dirname(os.path.abspath(__file__))
cmdPath = os.path.join(dirpath, 'cmds.py')

exec(open(cmdPath).read( ))




class AlignCommand(sublime_plugin.TextCommand):

	def run(self, edit):

		view = self.view

		if len(view.sel( )) > 0:
			alignSelections(self, edit)
