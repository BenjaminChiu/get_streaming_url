# -*- coding: utf-8 -*-
# @Desc    : 文件注释
# @Time    : 2020-11-08 17:19
# @Author  : tank boy
# @File    : dy_4k.py
from bookmark import show_bookmark_douyu
from douyu import DouYu
from potPlayer import PotPlayer

if __name__ == '__main__':
    print("正在极速打开4k 直播间")
    real_url = DouYu('9249162').get_real_url()

    print(real_url)
    PotPlayer(real_url).run()