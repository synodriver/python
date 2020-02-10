import pandas as pd
from pyecharts.charts import Line,Bar,Pie,Scatter
from pyecharts import options as opts

# # 在线人数画图
# file_path = 'b站在线人数统计.xlsx'
# df = pd.read_excel(file_path,index_col = "date_time",parse_dates=True)
# line=(
#     Line()
#     .add_xaxis(df.index.to_list())
#     .add_yaxis("星期四-星期五",df["星期四-星期五"].to_list())
#     .add_yaxis("五-六",df["星期五-星期六"].to_list())
#     .add_yaxis("六-天",df["星期六-星期天"].to_list())
#     .add_yaxis("天-一",df["星期天-星期一"].to_list())
#     .add_yaxis("一-二",df["星期一-星期二"].to_list())
#     .add_yaxis("二-三",df["星期二-星期三"].to_list())
#     .add_yaxis("三-四",df["星期三-星期四"].to_list())
#     .set_global_opts(title_opts = {"text":"b站一周的在线人数"},tooltip_opts=opts.TooltipOpts(trigger="axis",axis_pointer_type='cross')
#     )
# )

# line.render()



# # 输出处理
# file_path = 'b站在线人数统计.xlsx'
# df = pd.read_excel(file_path)
# print(df.max())
# print(df.min())
# print(df.mean())
# print(df.median())
# print(df.std())
# print(df.var())



# # 最大值，最小值，平均值，中位数画图

# file = '数据处理.xlsx'
# df = pd.read_excel(file,index_col='时间')
# line= (
#     Line()
#     .add_xaxis(df.index.to_list())
#     .add_yaxis("最大值",df['max'].to_list())
#     .add_yaxis('最小值',df['min'].to_list())
#     .add_yaxis('平均值',df['mean'].to_list())
#     .add_yaxis('中位数',df['mid'].to_list())
#     .set_global_opts(title_opts={"text":"b站在线人数简单分析"},tooltip_opts=opts.TooltipOpts(trigger="axis",axis_pointer_type='cross'))
# )
# line.render()


# file_path = r'F:\python\代码\B站\爬虫项目\b站_播放_评论_硬币数 - 副本 - 副本.xlsx'
# df = pd.read_excel(file_path,index='播放量')
# del df['av号']
# del df['标签']
# del df['标题']
# # df = df[100:200]
# df = df[df['播放量']>100000]
# df = df[df['播放量']<9000000]
# df = df.reset_index(drop=True)

# print(df.head())
# setattr = (
#     Scatter()
#     .add_xaxis(df.index.to_list())
#     .add_yaxis("评论数",df['评论数'].to_list())
#     .add_yaxis("硬币数",df['硬币数'].to_list())
#     .add_yaxis("转发数",df['转发数'].to_list())
#     .add_yaxis("收藏",df['收藏'].to_list())
#     .add_yaxis("点赞数",df['点赞数'].to_list())

#     .set_global_opts(title_opts = {"text":"播放量与各属性的关系图"},tooltip_opts=opts.TooltipOpts(trigger="axis",axis_pointer_type='cross'))
# )
# setattr.render()



# import matplotlib.pyplot as plt
# file_path = r'F:\python\代码\B站\爬虫项目\b站_播放_评论_硬币数 - 副本 - 副本.xlsx'
# df = pd.read_excel(file_path,index='播放量')
# del df['av号']
# del df['标签']
# del df['标题']
# df = df[df['播放量']>100000]
# df = df[df['播放量']<9000000]
# df = df.reset_index(drop=True)
# # print(df.head())
# print(df.head())
# x = df['播放量'].to_list()
# # print(x)
# # print(y)
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
# plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
# plt.scatter(x,df['点赞数'].to_list(),label='点赞数')
# plt.scatter(x,df['评论数'].to_list(),label='评论数')
# plt.scatter(x,df['硬币数'].to_list(),label='硬币数')
# plt.scatter(x,df['转发数'].to_list(),label='转发数')
# plt.scatter(x,df['收藏'].to_list(),label='收藏')

# plt.legend()
# plt.show()



# file_path = 'b站_播放_评论_硬币数.xlsx'
# df = pd.read_excel(file_path,index = "播放量")
# # print(df.head)
# scatter = (
#     Scatter()
#     .add_xaxis(df.index.to_list())
#     .add_yaxis("评论数",df['评论数'].to_list())
#     .add_yaxis("硬币数",df['硬币数'].to_list())
#     .add_yaxis("转发数",df['转发数'].to_list())
#     .add_yaxis("收藏",df['收藏'].to_list())
#     .set_global_opts(title_opts = {"text":"关系"},tooltip_opts=opts.TooltipOpts(trigger="axis",axis_pointer_type='cross'))
# )

# scatter.render()



