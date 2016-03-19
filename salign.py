#! /usr/bin/env python 3

import sublime
import sublime_plugin
from   cmds import *





class AlignCommand(sublime_plugin.TextCommand):

	def run(self, edit):

		view = self.view

		if len(view.sel( )) > 0:
			alignSelections(self, edit)
