import urllib.request
import re
import socket


#  输入基本信息
def input_info():
    print('Ponytail 图片抓取下载器')
    print('#'*20)
    input('按回车继续')
    print('输入抓取站点')
    site = input('输入kona或者yanre：')
    print('是否要下载18X的图片')
    safe = input('Y / N：')
    print('是否优先下载宽屏')
    wide = input('Y / N：')
    print('输入你要下载的tag,之间用"+"分割')
    tag = input('输入tag：')
    print('是否只下载大图：')
    width = input('Y / N：')
    print('输入下载起始页：')
    page_start = input('页码：')
    print('输入下载结束页：')
    page_end = input('页码：')
    if not site or not page_start or not page_end or not tag:
        return input_info()
    return get_url(site, safe, width, wide, tag)

"""
#  设置基本参数
site = 'kona'
#  可用kona和yanre
safe = True
#  要不要下载18X的东西
wide = True
#  是否优先下载宽屏
tag = 'ponytail'
#  网站的tag，可以用+分割，两边没有空格，当然你要确保这个tag是可用的
width = True
#  是否要下载大图
"""
page_start = 1
#  下载起始页
page_end = 37
##  下载结束页



# 伪装浏览器，获取图片和网页
def user_agent(url, text):
    web_header = {'User-Agent': 'Mozilla/5.0'}
    web_timeout = 30
    try:
        req = urllib.request.Request(url, None, web_header)
        fp = urllib.request.urlopen(req, None, web_timeout)
        page = fp.read()
        # 抓网页用text,抓图片走单独的
        if text:
            html = page.decode('utf8')
        else:
            html = page
        fp.close()
    except urllib.error.URLError as error:
        print(error.message)
    except socket.timeout as error:
        user_agent(url)
    return html


# 解析图片地址并抓取图片
def get_img(url):
    getlink = url.replace("\\/", "/")
    print('Now getting {link}'.format(link=getlink))
    finalimg = user_agent(getlink, text=False)
    return finalimg


# 通过URL地址得到图片地址然后完成存储
def page_sheet(pageid):
    url = baseurl+'&page={id}'.format(id=pageid)
    print ('Now we are tracking:/n {url}'.format(url=url))
    page = user_agent(url, text='True')
    #  print(page)
    findimg = 0
    list = re.findall(r'file_url":"(.*)","is_shown_in_index', str(page))
    #  print(list)
    for ponytailimg in list:
        finalimg = get_img(ponytailimg)
        findimg += 1
        # 借鉴来的，比自己写的逼格高一点
        with open('./myimg'+'/'+ponytailimg[-11:], 'wb') as code:
            code.write(finalimg)
        print(findimg)
    return findimg


# 生成需要访问的页面,其实我测试参数顺序abcde也是可以的，只是为了和官方搜索一样所以调整了一下顺序:
def get_url(site, safe, width, wide, tag):
    if site == "kona":
        a = 'http://konachan.com/post?'
    elif site == "yanre":
        a = 'https://yande.re/post?'
    else:
        return error(1)
    if safe:
        b = 'rating:safe'
    if width:
        c = '%20width:1680..%20height:1050..%20'
    if wide:
        d = 'order:wide%20'
    tagmany = tag.split('+')
    if len(tagmany) > 1:
        e = 'tags='+tag
    elif len(tagmany) == 1:
        e = 'tag='+tag
    else:
        return error(2)
    return a+e+c+d+b


# 报错地址
def error(o):
    if o == 1:
        return '来源非法'
    if o == 2:
        return '没有tag'
    else:
        return '未知错误'


baseurl = input_info()
total = 0
for i in range(page_start, page_end):
    total += page_sheet(i)
print ('Got {total}'.format(total=total))
