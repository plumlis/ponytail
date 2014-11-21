# 进度条的显示


import sys


def progress(blocks, blocksize, total, width=100):
    # 据说这玩意被称为回调函数
    # blocks：下载几块了
    # blocksize：每块多大
    # total：文件一共多大
    percentage = width * blocks * blocksize // total
    if percentage > width:
        percentage = width
    sys.stdout.write('[' + percentage * '#' + (width - percentage) * '-' + ']' + str(percentage * 100 // width) + '%' + '\r')
    sys.stdout.flush()
