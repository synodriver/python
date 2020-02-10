import random
import os
import time
from pynput.keyboard import Controller, Key, Listener
color = ''
map = {}
map['d'] = '绿'
map['f'] = '黄'
map['j'] = '红'
map['k'] = '蓝'
zi_rep = ['蓝', '红', '黄', '绿']
yanse = [31, 32, 33, 34]
zidian = {}
zidian['31'] = '红'
zidian['32'] = '绿'
zidian['33'] = '黄'
zidian['34'] = '蓝'
num = 0
score = 0
start_time = time.time()
def xxx():
    global yanse
    global zidian
    yan = random.choice(yanse)
    print('\033[1;%dm%s \033[0m'%(yan,random.choice(zi_rep)))
    return zidian[str(yan)]

# 监听按压
def on_press(key):
    global color
    global map
    global num
    global score
    try:
        if key.char  in ['d','f','k','j']:
            if map[str(key.char)]==color:
                print("\r正确")
                num+=1
                score+=1
            else:
                print("\r错误")
                num +=1
            color= xxx()
        else :
            print("\r错误输入重新输入")
        if num==10:
            end_time= time.time()
            TIME = end_time-start_time
            print('你花了'+str(TIME)+'秒的时间,\n正确率为：'+str(score*10)+'%')
            os._exit(0)

    except AttributeError:
        pass
        # print("正在按压:", format(key))
def start_listen():
    with Listener(on_press=on_press) as listener:
        listener.join()


if __name__ == '__main__':
    # 开始监听
    print('呈现\033[1;32m绿\033[0m颜色汉字时按\033[1;32mD\033[0m键，\033[1;33m黄\033[0m颜色汉字时按\033[1;33mF\033[0m键，\033[1;31m红\033[0m颜色汉字时按\033[1;31mJ\033[0m键，\033[1;34m蓝\033[0m颜色汉字时按\033[1;34mK\033[0m键，而不要管那个字的字义是什么')
    color=xxx()
    kb = Controller()
    # 开始监听,按esc退出监听
    start_listen()
