import os
import sys
import time
import tkinter as tk
def get_mm(timee):
    a = [0,31,59,90,120,151,181,212,243,273,304,334,365]
    month = a[int(timee[5:7])-1]*24*3600
    day = int(timee[8:10])*3600*24
    hh = int(timee[11:13])*3600
    mm = int(timee[14:16])*60
    ss = int(timee[17:19])
    # print(hh+mm+ss+day+month)
    sumtime = hh+mm+ss+day+month
    return int(sumtime)
def main():
    try:
        s = '2019-%02d-%02d %02d:%02d:%02d'%(int(e1.get()),int(e2.get()),int(e3.get()),int(e4.get()),int(e5.get()))
        # s = '2019-'+input("09 05 12:00:00这种格式：")
        try:
            os.system('shutdown.exe -a')
        except:
            pass
        timee = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        shezhi = get_mm(s)
        xianzai = get_mm(timee)
        cha = get_mm(s)-get_mm(timee)
        print(cha)
        os.system(f"shutdown.exe -s -t {str(cha)}")
    except:
        pass
def opp():
    os.system('shutdown.exe -a')
if __name__ == "__main__":
    win = tk.Tk()
    win.title('关机系统')
    win.geometry('350x250')
    t1 = tk.Label(win,text = '月份：',font= ('黑体','15'))
    t1.place(x= 0,y= 0)
    t2 = tk.Label(win,text = '日份：',font= ('黑体','15'))
    t2.place(x= 0,y= 30)
    t3 = tk.Label(win,text = '时：',font= ('黑体','15'))
    t3.place(x= 0,y= 60)
    t4 = tk.Label(win,text = '分：',font= ('黑体','15'))
    t4.place(x= 0,y= 90)
    t5 = tk.Label(win,text = '秒：',font= ('黑体','15'))
    t5.place(x= 0,y= 120)
    e1 = tk.Entry(win, font=('微软雅黑', '15'))
    e1.place(x= 70,y=0)
    e2 = tk.Entry(win, font=('微软雅黑', '15'))
    e2.place(x= 70,y=30)
    e3 = tk.Entry(win, font=('微软雅黑', '15'))
    e3.place(x= 70,y=60)
    e4 = tk.Entry(win, font=('微软雅黑', '15'))
    e4.place(x= 70,y=90)
    e5 = tk.Entry(win, font=('微软雅黑', '15'))
    e5.place(x= 70,y=120)
    b1 = tk.Button(win,text = '点击计划关机设置',font = ('微软雅黑','15'),command = main)
    b1.place(x = 100,y = 150)
    b2 = tk.Button(win, text='点击关闭计划关机', font=('微软雅黑', '15'), command=opp)
    b2.place(x=100, y=200)
    win.mainloop()
