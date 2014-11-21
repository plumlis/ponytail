# 直接将弄来的URL挨个抓取返回成网页地址

import urllib.request
import socket


def make_connections(url, agent={'User-Agent': 'Mozilla/5.0'}, text=True, timesout=30):
    try:
        req = urllib.request.Request(url, None, agent)
        fp = urllib.request.urlopen(req, None, timesout)
        page = fp.read()
        html = page.decode('utf8')
        fp.close()
    except urllib.error.URLError as error:
        print(error)
    except socket.timeout as error:
        html = ''
        print('Times Out')
    return html
