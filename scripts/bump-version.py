#!/usr/bin/env python3
"""Setzt eine neue Build-Kennung in index.html und version.json.
Vor jedem Commit ausführen, damit installierte Apps das Update erkennen."""
import json, re, time, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
build = time.strftime("%Y%m%d-%H%M%S", time.gmtime())
idx = root / "index.html"
s = idx.read_text()
s, n = re.subn(r'const BUILD = "[^"]*";', f'const BUILD = "{build}";', s, count=1)
assert n == 1, "BUILD-Konstante nicht gefunden"
idx.write_text(s)
(root / "version.json").write_text(json.dumps({"build": build}) + "\n")
print(build)
