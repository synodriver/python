def ciyun_img(path1,path2):
   from PIL import Image
   from wordcloud import WordCloud, ImageColorGenerator
   import matplotlib.pyplot as plt
   import numpy as np
   import jieba
   path_txt = path1 #'C://Users/Administrator/Desktop/all.txt'
   path_img = path2 #"C://Users/Administrator/Desktop/timg.jpg"
   f = open(path_txt, 'r', encoding='UTF-8').read()
   background_image = np.array(Image.open(path_img))
   cut_text = " ".join(jieba.cut(f))
   wordcloud = WordCloud(
       # 设置字体，不然会出现口字乱码，文字的路径是电脑的字体一般路径，可以换成别的
       font_path="C:/Windows/Fonts/simfang.ttf",
       background_color="white",
       # mask参数=图片背景，必须要写上，另外有mask参数再设定宽高是无效的
       mask=background_image).generate(cut_text)
   # 生成颜色值
   image_colors = ImageColorGenerator(background_image)
   # 下面代码表示显示图片
   plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation="bilinear")
   plt.axis("off")
   plt.show()
def ciyun(path):
   from wordcloud import WordCloud
   import matplotlib.pyplot as plt  #绘制图像的模块
   import  jieba                    #jieba分词
   path_txt=path
   f = open(path_txt,'r',encoding='UTF-8').read()
   cut_text = " ".join(jieba.cut(f))
   wordcloud = WordCloud(
      font_path="C:/Windows/Fonts/simfang.ttf",
      background_color="white",width=1000,height=880).generate(cut_text)
   plt.imshow(wordcloud, interpolation="bilinear")
   plt.axis("off")
   plt.show()
def cipin(path):
    import jieba
    txt = open(path,'r',encoding='utf-8').read()
    words =jieba.lcut(txt)	# 精准切词
    count={}
    for word in words:
        if len(word) ==1:
            continue
        else:
            count[word]=count.get(word,0)+1
    result = sorted(count.items(),key=lambda x:x[1],reverse=True)
    for i in range(20):
        word,count=result[i]
        print(str(i+1)+','+word,',',count)

path = r'F:\python\代码\B站在线人数\词云分析\游戏区评论.txt'

## 画饼图
# import pandas as pd 
# df = pd.read_excel('cipin.xlsx')
# print(df)
# print(df['单词'].to_list(),df['词频'].to_list())
# from pyecharts import options as opts
# from pyecharts.charts import Pie
# pie = (
#     Pie()
#     .add(" ",[list(z) for z in zip(df['单词'].to_list(), df['词频'].to_list())])
#     .set_global_opts(title_opts=opts.TitleOpts(title="游戏区词频统计"))
#     .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
# )
# pie.render('词频统计.html')