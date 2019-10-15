import eel
import screeninfo
import os

screen=screeninfo.get_monitors()[0]
TEMPLATE_PATH="sumohub/web_bs/index_template.html"
INDEX_PATH="sumohub/web_bs/index_main.html"

if os.path.exists(INDEX_PATH):
    os.remove(INDEX_PATH)

if not os.path.exists(INDEX_PATH):
    with open(INDEX_PATH,"w") as fwrite:
        with open(TEMPLATE_PATH,"r") as fread:
            template=fread.read()
        template=template.replace("SCREEN_WIDTH",str(screen.width))
        fwrite.write(template)

@eel.expose
def search_id(ID):
    aux=ID.split(" ")
    if len(aux)==1:
        return(aux[0])
    else:
        return(aux)
    

#Modified eel. reinstall if any problems
try:
    eel.init("sumohub/web_bs")
    eel.start("index_main.html", options={"chromeFlags": ["--start-maximized","--aggressive-cache-discard","--enable-aggressive-domstorage-flushing"]})
   
except (SystemExit, MemoryError, KeyboardInterrupt):
    pass
