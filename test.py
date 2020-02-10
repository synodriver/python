
import random
num = 10
mapp=[]
xianshi=[]
def init():
    for i in range(9):
        mapp.append(["0","0","0","0","0","0","0","0","0"])
    lei = 0
    while lei<num:
        x = int(random.randint(0,8))
        y = int(random.randint(0,8))
        if (mapp[x][y]=="0"):
            mapp[x][y]='*'
            lei+=1
    def hefa(x,y):
        if 0<=x<9 and 0<=y<9:
            if mapp[x][y]=="*":
                return True
            return False
        return False
    for i in range(9):
        for j in range(9):
            if mapp[i][j]!="*":
                sum = 0
                if hefa(i-1,j-1):
                    sum+=1
                if hefa(i-1,j):
                    sum+=1
                if hefa(i-1,j+1):
                    sum+=1
                if hefa(i,j-1):
                    sum+=1
                if hefa(i,j+1):
                    sum+=1
                if hefa(i+1,j-1):
                    sum+=1
                if hefa(i+1,j):
                    sum+=1
                if hefa(i+1,j+1):
                    sum+=1
                mapp[i][j]=sum
    for i in range(9):
        xianshi.append(["/","/","/","/","/","/","/","/","/"])
def dayin(hanshu):
    print("  1 2 3 4 5 6 7 8 9")      
    for i in range(9):
        print(i+1,end='|')
        for j in range(9):
            print(hanshu[i][j],end='|')
        print()
def kai(x,y):
    if 0<=x<9 and 0<=y<9:
        if xianshi[x][y]=='/' and mapp[x][y]==0 :
            xianshi[x][y]=mapp[x][y]
            kai(x-1,y-1)
            kai(x-1,y)
            kai(x-1,y+1)
            kai(x,y-1)
            kai(x,y+1)
            kai(x+1,y-1)
            kai(x+1,y)
            kai(x+1,y+1)
            return 
        elif mapp[x][y]=="*":
            return 
        else :
            xianshi[x][y]=mapp[x][y]
            return 
def chuli(x,y):
    if not (0<=x<9 and 0<=y<9):
        print("重新输入")
        return 
    if mapp[x][y]==0:
        kai(x,y)
    else :
        xianshi[x][y]=mapp[x][y]
import os 
def main():
    init()
    dayin(xianshi)
    print("插旗规则输入0 0,探雷直接输入坐标！！")
    while True:
        x,y =map(int,input("请输入x和y轴的坐标：").split())
        if x==0 and y==0:
            x,y =map(int,input("旗子的位置坐标: ").split())
            x = x-1
            y = y-1
            xianshi[x][y]='*'
            flag = 1
            for i in range(9):
                for j in range(9):
                    if xianshi[i][j]=='/':
                        flag=0
            if flag==1:
                os.system("cls")
                dayin(xianshi)
                print("你赢了")
                return 
        else :
            x = x-1
            y = y-1
            chuli(x,y)
            if mapp[x][y]=="*":
                os.system("cls")
                dayin(xianshi)
                print('你输了！！')
                return 
            flag = 1
            for i in range(9):
                for j in range(9):
                    if xianshi[i][j]=='/':
                        flag=0
            if flag==1:
                os.system("cls")
                dayin(xianshi)
                print("你赢了")
                return
        os.system("cls")
        dayin(xianshi)

if __name__ == "__main__":
    main()
    os.system("pause")
    print("2333")
