#! /usr/bin/env python 3

import os
import sublime
import sublime_plugin
import random
import re
import sys





__version__ = '0.1.0'
__authors__ = ['Ryan Grannell (@RyanGrannell)']





class CharAlignCommand (sublime_plugin.TextCommand):

	def run (self):

		view       = self.view
		selection  = view.sel( )

		settings   = view.settings( )
		tab_size   = int(settings.get('tab_size', 8))
		use_spaces = settings.get('translate_tabs_to_spaces')

		if len(selection) > 1:
			print(selection)
