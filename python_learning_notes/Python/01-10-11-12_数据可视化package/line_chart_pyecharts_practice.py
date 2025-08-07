# 导包,导入Line功能构建折线图对象
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts, TooltipOpts

# 得到折线图对象
line = Line()
# 添加x轴数据
line.add_xaxis(["中国", "美国", "英国"])
# 添加y轴数据
line.add_yaxis("GDP", [30, 20, 10])
# 生成图表
line.render()
# 点击运行之后发现什么都没有出现,因为图表已经被生成网页文件了,左侧生成一个新的网页文件render.html
# 打开该文件,右上角有浏览器打开的按钮,选择一个浏览器即可


# 全局配置选项
line.set_global_opts(
    title_opts=TitleOpts(is_show=True, title="GDP Comparison", pos_left="center", pos_bottom="1%"),
    # 全部是和标题相关的配置,title就是标题名, pos_left就是控制标题的横向位置,pos就是position位置,center就是居中
    # pos_bottom就是控制标题的纵向位置,bottom就是底部,相对底部的位置,这里设置为1%
    legend_opts=LegendOpts(is_show=True),
    # 图例功能
    toolbox_opts=ToolboxOpts(is_show=True),
    # 工具箱功能
    visualmap_opts=VisualMapOpts(is_show=True),
    # 视觉映射
    tooltip_opts=TooltipOpts(is_show=True),
    #提示框
)
# 生成图表
line.render()
# 注意,上面也有一个生成图表的代码,每次生成的render.html文件会是最后一次执行生成图表时生成的图表样式
# 而不会生成多份图表,我个人理解是覆盖了
# 每次生成的图表名称都是render.html, 之前生成的如果不重命名,后面再生成时会覆盖前面的文件

