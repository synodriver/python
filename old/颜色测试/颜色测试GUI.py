import random
import tkinter as tk
import time
import  os
zi_rep = ['蓝', '红', '黄', '绿','蓝', '红', '黄', '绿','蓝', '红', '黄', '绿','蓝', '红', '黄', '绿','蓝', '红', '黄', '绿','蓝', '红', '黄', '绿']
yanse = ['blue','red','yellow','green','blue','red','yellow','green','blue','red','yellow','green','blue','red','yellow','green','blue','red','yellow','green']
score= 0
color = ''
num = 0
win = tk.Tk()
win.geometry('1920x1080')
def kaishi():
    global color
    global score
    global  num
    score = 0
    num = 0
    color = random.choice(yanse)
    t1 = tk.Text(win,fg=color, font=("黑体", '600'),width=2, height=1)
    t1.place(x=0, y=0)
    t1.delete(0.0,'end')
    t1.insert(0.0, random.choice(zi_rep))
    l1 = tk.Label(win, font=('','50'), text=f"得分为：{score}                   ")
    l1.place(x= 1000,y= 50)
    tk.Label(win, font=('', '50'), text='正确率为：0.00\t%').place(x=1000, y=200)
def red():
    global score
    global color
    global num
    if color =='red':
        score+=1
    color = random.choice(yanse)
    t1 = tk.Text(win,fg=color, font=("黑体", '600'),width=2, height=1)
    t1.place(x=0, y=0)
    t1.delete(0.0,'end')
    t1.insert(0.0, random.choice(zi_rep))
    l1 = tk.Label(win, font=('', '50'), text=f"得分为：{str(score)}")
    l1.place(x=1000, y=50)
    num+=1
    tk.Label(win, font=('', '50'), text='正确率为：' + str('%.2f'%(score * 10 / num)) + '\t%').place(x=1000, y=200)
def yellow():
    global score
    global color
    global num
    if color =='yellow':
        score+=1
    color = random.choice(yanse)
    t1 = tk.Text(win,fg=color, font=("黑体", '600'),width=2, height=1)
    t1.place(x=0, y=0)
    t1.delete(0.0,'end')
    t1.insert(0.0, random.choice(zi_rep))
    l1 = tk.Label(win, font=('', '50'), text=f"得分为：{str(score)}")
    l1.place(x=1000, y=50)
    num+=1
    tk.Label(win, font=('', '50'), text='正确率为：' + str('%.2f'%(score * 10 / num)) + '\t%').place(x=1000, y=200)
def blue():
    global score
    global color
    global num
    if color =='blue':
        score+=1
    color = random.choice(yanse)
    t1 = tk.Text(win,fg=color, font=("黑体", '600'),width=2, height=1)
    t1.place(x=0, y=0)
    t1.delete(0.0,'end')
    t1.insert(0.0, random.choice(zi_rep))
    l1 = tk.Label(win, font=('', '50'), text=f"得分为：{str(score)}")
    l1.place(x=1000, y=50)
    num+=1
    tk.Label(win, font=('', '50'), text='正确率为：' + str('%.2f'%(score * 10 / num)) + '\t%').place(x=1000, y=200)
def green():
    global score
    global color
    global num
    if color =='green':
        score+=1
    color = random.choice(yanse)
    t1 = tk.Text(win,fg=color, font=("黑体", '600'),width=2, height=1)
    t1.place(x=0, y=0)
    t1.delete(0.0,'end')
    t1.insert(0.0, random.choice(zi_rep))
    l1 = tk.Label(win, font=('', '50'), text=f"得分为：{str(score)}")
    l1.place(x=1000, y=50)
    num+=1
    tk.Label(win, font=('', '50'), text='正确率为：' + str('%.2f'%(score * 10 / num)) + '\t%').place(x=1000, y=200)

b0 =tk.Button(win,text = '开始',font = ("","50"),command = kaishi).place(x= 1400,y = 400)
b1 =tk.Button(win,text = '红',font = ("","50"),command = red).place(x= 600,y = 900)
b2 =tk.Button(win,text = '黄',font = ("","50"),command = yellow).place(x= 800,y = 900)
b3 =tk.Button(win,text = '蓝',font = ("","50"),command = blue).place(x= 1000,y = 900)
b4 =tk.Button(win,text = '绿',font = ("","50"),command = green).place(x= 1200,y = 900)

win.mainloop()




