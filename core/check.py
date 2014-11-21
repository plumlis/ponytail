# 检查系统文件是否有缺失


import os
import configparser


def check_conf(filename):
    if not os.path.isfile('./config/'+filename):
        return False
    return True


def create_conf(filename):
    if not os.path.exists('config'):
        try:
            os.mkdir('config')
        except:
            print('创建目录出错')
    job = configparser.ConfigParser()
    job['Global'] = {
        'base_dir': './myimg',
        'default_catcher': 'kona'
    }
    job['web'] = {
        'useragent': 1,
        'web_header': 'Mozilla/5.0',
        'timesout': 30
    }
    with open(filename, 'w') as configwritefile:
        job.write(configwritefile)
