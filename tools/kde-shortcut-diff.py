#!/usr/bin/env python3
# UGLY script to check which KWin shortcuts are not used in db.py

import subprocess
import sys
sys.path.append('..')
import db

kde_cmd = "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.shortcutNames"
ret = subprocess.check_output(kde_cmd, shell=True, stderr=subprocess.STDOUT)
ret = ret.decode('utf-8')

shortcuts = ret.split("\n")

# Replace numbers in commands (redundant commands)
filtered_shortcuts = []
for sh in shortcuts:
    if not sh:
        continue
    sh = ''.join(i for i in sh if not i.isdigit())
    if not sh in filtered_shortcuts:
        filtered_shortcuts.append(sh)

commands = []

for cmd in db.commands():
    if "command" in cmd:
        commands.append(cmd["command"])
    else:
        all_commands = cmd["commands"]
        for a in all_commands:
            commands.append(a)

for sh in filtered_shortcuts:
    stripped = sh.strip()
    found = False
    for c in commands:
        if stripped in c:
            found = True

    if not found:
        print(sh)
