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
ciyun('2.txt')
# ciyun_img('2.txt','1.png')