import webview
import screeninfo

screen_info=screeninfo.get_monitors()[0]

window = webview.create_window('Sumohub v0.1', 'sumohub/web_bs/index_mod2.html',width=screen_info.width,height=screen_info.height)
webview.start(http_server=True)