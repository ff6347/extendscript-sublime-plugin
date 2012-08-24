import sublime
import sublime_plugin
import subprocess
import re


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

        my_script_string = my_tell + target_app + my_to_do + finalpath + my_lang

        #sublime.error_message(my_script_string)

        my_call = subprocess.call(['osascript', '-e', my_script_string])
