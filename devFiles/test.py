#!/usr/bin/env python

import os
cmd = """osascript -e 'tell app "Firefox" to activate'"""
def stupidtrick():
     os.system(cmd)
#stupidtrick()