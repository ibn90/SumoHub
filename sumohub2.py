from cefpython3 import cefpython as cef
from screeninfo import get_monitors

import ctypes
import platform
import sys
import base64
import os

if os.path.exists("sumohub/web_bs/index_mod2.html"):
    HTML_PATH="sumohub/web_bs/index_mod2.html"
else:
    print("HTML INDEX UNREACHABLE. REINSTALL APP")
    raise FileNotFoundError

def main():
    switches={
        # "no-sandbox":"",
        "disable-gpu":"",
        "disable-web-security":""
    }
    check_versions()
    sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
    cef.Initialize(switches=switches)
    window_info = cef.WindowInfo()
    parent_handle = 0

    # This call has effect only on Mac and Linux.
    # All rect coordinates are applied including X and Y parameters.
    screen_info=get_monitors()[0]
    window_info.SetAsChild(parent_handle, [0, 0, screen_info.width,screen_info.height])
    url="file:///sumohub/web_bs/index_mod.html"
    browser = cef.CreateBrowserSync(url=html_to_data_uri(get_html(HTML_PATH)),
                                    window_info=window_info,
                                    window_title="Window size")
    if platform.system() == "Windows":
        window_handle = browser.GetOuterWindowHandle()
        insert_after_handle = 0
        # X and Y parameters are ignored by setting the SWP_NOMOVE flag
        SWP_NOMOVE = 0x0002
        # noinspection PyUnresolvedReferences
        ctypes.windll.user32.SetWindowPos(window_handle, insert_after_handle,
                                          0, 0, 900, 640, SWP_NOMOVE)
    cef.MessageLoop()
    del browser
    cef.Shutdown()

def check_versions():
    ver = cef.GetVersion()
    print("[hello_world.py] CEF Python {ver}".format(ver=ver["version"]))
    print("[hello_world.py] Chromium {ver}".format(ver=ver["chrome_version"]))
    print("[hello_world.py] CEF {ver}".format(ver=ver["cef_version"]))
    print("[hello_world.py] Python {ver} {arch}".format(
           ver=platform.python_version(),
           arch=platform.architecture()[0]))    # main()
    print()
    assert cef.__version__ >= "57.0", "CEF Python v57.0+ required to run this"

def get_html(HTML_PATH):
    with open(HTML_PATH) as fread:
        return fread.read()

def html_to_data_uri(html, js_callback=None):
    # This function is called in two ways:
    # 1. From Python: in this case value is returned
    # 2. From Javascript: in this case value cannot be returned because
    #    inter-process messaging is asynchronous, so must return value
    #    by calling js_callback.
    html = html.encode("utf-8", "replace")
    b64 = base64.b64encode(html).decode("utf-8", "replace")
    ret = "data:text/html;base64,{data}".format(data=b64)
    if js_callback:
        js_print(js_callback.GetFrame().GetBrowser(),
                 "Python", "html_to_data_uri",
                 "Called from Javascript. Will call Javascript callback now.")
        js_callback.Call(ret)
    else:
        return ret

if __name__ == '__main__':
    main()
