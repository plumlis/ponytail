# 适用于Konachan的图片抓取

import re
import configparser


def imglist(list):
    newlist = []
    for i in list:
        newlist.append(i.replace("\\/", "/"))
    return newlist


def makeurl(url, tag, safe, width, wide, page_start, page_end):
    # 生成网址用的函数，将网址根据各部分参数拆成a,b,c,d,e…………
    # a : base_url
    # b : tag列表
    # c : 限制级别
    # d : 大小筛选
    # e : 排序级别
    # f : 页面列表
    # 最后输出列表 list
    if not tag or not page_start or page_start <= 0 or page_start > page_end:
        return False
    a = url
    b = ''
    c = ''
    d = ''
    e = ''
    if len(tag.split('+')) > 1:
        b = 'tags='+tag
    elif len(tag.split('+')) == 1:
        b = 'tag='+tag
    else:
        return False
    if safe == '1':
        c = 'rating:safe'
    if width == '1':
        d = '%20width:1680..%20height:1050..%20'
    if wide == '1':
        e = 'order:wide%20'
    f = '&page='
    list = []
    for i in range(page_start, page_end+1):
        finalurl = a + b + c + d + e + f + str(i)
        list.append(finalurl)
    return list


def decode(page):
    list = re.findall(r'file_url":"(.*)","is_shown_in_index', str(page))
    finallist = imglist(list)
    return finallist


class main:
    def __init__(self, configfile):
        job = configparser.ConfigParser()
        job.read(configfile)
        self.tag = job['catcher']['tag']
        self.safe = job['catcher']['safe']
        self.width = job['catcher']['width']
        self.wide = job['catcher']['wide']
        self.base_url = job['catcher']['base_url']
        if job['navigator']['Autonav'] == 0:
            self.page_start = 1
            self.page_end = 1
        else:
            self.page_start = int(job['navigator']['page_start'])
            self.page_end = int(job['navigator']['page_end'])
        self.urllist = makeurl(self.base_url,
                               self.tag,
                               self.safe,
                               self.width,
                               self.wide,
                               self.page_start,
                               self.page_end)
    def create_conf(self, filename):
        # job = configparser.ConfigParser()
        # with open(filename, 'w') as configfile:
        #    configfile.write()
        pass
