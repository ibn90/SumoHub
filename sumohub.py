import eel

#Modified eel. reinstall if any problems
try:
    eel.init("sumohub/web_bs")
    eel.start("index_mod.html", options={"chromeFlags": ["--start-maximized","--aggressive-cache-discard"]})
except (SystemExit, MemoryError, KeyboardInterrupt):
    pass
