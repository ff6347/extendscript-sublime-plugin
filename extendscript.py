# -- coding: utf-8 --
# Copyright (c)  2012
# Fabian "fabiantheblind" Morón Zirfas
# Permission is hereby granted, free of charge, to any
# person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the Software
# without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to  permit persons to
# whom the Software is furnished to do so, subject to
# the following conditions:
# The above copyright notice and this permission notice
# shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF  CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTIO
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# see also http://www.opensource.org/licenses/mit-license.php

import sublime
import sublime_plugin
import subprocess
import re
# run it via view.run_command('extend_script') in the console
# TO DO Options
#   * Key Binding
#   * Autosafe (if is dirty or something like this)
#   * Application Chooser
#   * Version Chooser
#   * Ond some other Fancy stuff


class ExtendScriptCommand(sublime_plugin.TextCommand):
    def run(self, edit):

        my_tell = "tell application "
        target_app = '"Adobe InDesign CS5"'
        my_to_do = "to do script alias "
        my_lang = " language javascript"

        filepath = self.view.file_name()

        #sublime.error_message(self.view.file_name())

        filepath = re.sub("\/", ":", filepath)
        filepath = filepath[1:]
        finalpath = '"%s"' % filepath

        #sublime.error_message(finalpath)

        as_string = my_tell + target_app + my_to_do + finalpath + my_lang

        #sublime.error_message(as_string)

        my_call = subprocess.call(['osascript', '-e', as_string])
