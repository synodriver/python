# !/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@Author         :  刘华强
@Version        :
------------------------------------
@File           :  test1.py
@Description    :
@CreateTime     :  2019/12/14 21:59
------------------------------------
@ModifyTime     :
"""


import time
from concurrent.futures import ThreadPoolExecutor
def xx(x):
    print(f'{str(x)}开始')
    time.sleep(3)
    print(f"{str(x)}结束")


li = [1, 2, 3, 4, 5, 6, 7, 8]
# 1 创建线程池
pool = ThreadPoolExecutor(max_workers=8)


# 2 循环指派任务
[pool.submit(xx, (i,))for i in li]

# 3 关闭
pool.shutdown()