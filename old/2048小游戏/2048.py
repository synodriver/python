# coding=utf-8
import random
import os
import sys
import time
from pynput.keyboard import Controller, Key, Listener
def youxiyingqing():
    summ = [0]
    a = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    def ppprint(num):
        x = random.randint(0,7)
        print("\033[0;3%sm" % x + f"{num}" + "\033[0m")
    def dayin():
        # print("233")
        os.system("cls")
        # print('-'*21)
        print('\033[033m{}\033[033m'.format('-'*21))
        for row in a:
            print(f"""{"|".join([str(col or ' ').center(4) for col in row])}""")
            # ppprint('{}'.format("|".join([str(col or ' ').center(4) for col in row])))
            print('\033[033m{}\033[033m'.format('-' * 21))
        # print("得分",summ[0])
    def init():
        for x in range(4):
            for y in range(4):
                a[x][y]=0
        shu =[2,2,2,2,2,2,2,4,4]
        x  = random.randint(0,3)
        y= random.randint(0,3)
        a[x][y] =random.choice(shu)
        while True:
            x = random.randint(0, 3)
            y = random.randint(0, 3)
            if(a[x][y]==0):
                a[x][y] = random.choice(shu)
                break
    def panduan():
        f= 0
        for x in range(4):
            for y in range(4):
                if a[x][y]==2048:
                    print("你赢了！！！！！！！！！")
                    # sys.exit()
                    # return
                    print("重新开始")
                    # youxiyingqing()
                    return
                if a[x][y]==0:
                    f=1
        if f==0:
            fff= 0
            for x in range(3):
                for y in range(3):
                    if a[x][y] in [a[x + 1][y], a[x][y + 1]]:
                        fff = 1
                        return
            if a[2][3]==a[3][3] or a[3][2]==a[3][3]:
                fff=1
                return
            if fff==0:
                print("你输了！！！")
                # sys.exit()
                # youxiyingqing()
                # init()
                # start()
                return
    def aaa():
        for x in range(4):
            for y in range(4):
                if a[x][y]!=0:
                    for yy in range(y):
                        if a[x][yy]==0:
                            a[x][yy]=a[x][y]
                            a[x][y]=0
            # print(a[x])
        for x in range(4):
            for y in range(3):
                if a[x][y]==a[x][y+1]:
                    summ[0] +=a[x][y]
                    a[x][y]*=2
                    a[x][y+1]=0
        for x in range(4):
            for y in range(4):
                if a[x][y]!=0:
                    for yy in range(y):
                        if a[x][yy]==0:
                            a[x][yy]=a[x][y]
                            a[x][y]=0
    def sss():
        for y in range(4):
            for x in range(4):
                if a[x][y] != 0:
                    for xx in range(3,x,-1):
                        if a[xx][y] == 0:
                            a[xx][y] = a[x][y]
                            a[x][y] = 0
        for y in range(4):
            for x in range(3,0,-1):
                if a[x][y]==a[x-1][y]:
                    summ[0] += a[x][y]
                    a[x][y]*=2
                    a[x-1][y]=0
        for y in range(4):
            for x in range(4):
                if a[x][y] != 0:
                    for xx in range(3,x,-1):
                        if a[xx][y] == 0:
                            a[xx][y] = a[x][y]
                            a[x][y] = 0
    def ddd():
        for x in range(4):
            for y in range(3,-1,-1):
                # print(a[x][y])
                if a[x][y]!=0:
                    for yy in range(3,y,-1):
                        if a[x][yy]==0:
                            a[x][yy]=a[x][y]
                            a[x][y]=0
        for x in range(4):
            for y in range(3,0,-1):
                if a[x][y]==a[x][y-1]:
                    summ[0] += a[x][y]
                    a[x][y]*=2
                    a[x][y-1]=0
        dayin()
        for x in range(4):
            for y in range(3,-1,-1):
                # print(a[x][y])
                if a[x][y]!=0:
                    for yy in range(3,y,-1):
                        if a[x][yy]==0:
                            a[x][yy]=a[x][y]
                            a[x][y]=0
    def www():
        for y in range(4):
            for x in range(4):
                if a[x][y]!=0:
                    for xx in range(x):
                        if a[xx][y]==0:
                            a[xx][y]=a[x][y]
                            a[x][y]=0
        for y in range(4):
            for x in range(3):
                if a[x][y]==a[x+1][y]:
                    summ[0] += a[x][y]
                    a[x][y]*=2
                    a[x+1][y]=0
        for y in range(4):
            for x in range(4):
                if a[x][y]!=0:
                    for xx in range(x):
                        if a[xx][y]==0:
                            a[xx][y]=a[x][y]
                            a[x][y]=0
    def suiji():
        zb=[]
        for x in range(4):
            zb.extend(x*10+y for y in range(4) if a[x][y]==0)
        # print(zb)
        if zb!=[]:
            x= random.choice(zb)
            a[int((x-x%10)/10)][x%10]=2
    init()
    dayin()
    def youxi(key):
        # for x in range(10):
        #     print()
        # op = input("输入wsad:")
        op= str (key)
        op = eval(op)
        op = str(op)
        # print(op)
        if op in {'Key.up', 'Key.down', 'Key.left', 'Key.right', '*'}:
            # print(op)
            if op =='Key.up':
                www()
            elif op =='Key.left':
                aaa()
            elif op == 'Key.down':
                sss()
            elif op =='Key.right':
                ddd()
            elif op =='*':
                init()
                # start()
            if op != '*':
                suiji()
            dayin()
            print("得分：",summ[0])
            print("按*重新开始" + '\n' + '操作按上下左右')
            panduan()
    with Listener(on_press=youxi) as listener:
        listener.join()
if __name__ == '__main__':
    youxiyingqing()

