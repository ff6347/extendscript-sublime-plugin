import sublime, sublime_plugin
from subprocess import call


class ExtendScriptCommand(sublime_plugin.TextCommand):
    def run(self):
        #if self.view and self.view.is_dirty():
            #self.view.run_command("save")
        browser_command = """
        tell application "Firefox" to activate
        """
        call(['osascript', '-e', """tell application "Firefox" to activate"""])
        #subprocess.Popen("""osascript -e 'tell app "Firefox" to activate' """, shell=True)