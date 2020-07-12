# 一、背景
在数据分析的完整流程中 (数据收集、存储、清洗、展示)，数据收集的多少对最终分析结果有着直接影响，因此需要对外网的数据进行收集并整理，用于支持后续的分析。

# 二、要求
改造基于 requests 爬虫，增加多线程功能，实现通过拉勾网，获取 北、上、广、深四地 python 工程师的平均薪水待遇，并将获取结果存入数据库。
1. 通过多线程实现 requests 库的多线程方式。
2. 获取北京、上海、广州、深圳四个地区，各地区 100 个 python 工程师职位的职位名称和薪资水平。
3. 相同地区、相同职位及相同待遇的职位需去重。
4. 将获取的内容存入数据库中。

# 三、选做：
使用图形库展示各地区 python 工程师薪资分布情况，使用不同颜色代表该地区 python 工程师薪资高低情况（建议使用 echart 或 matplotlib，具体图形库不限）。

# 四、说明：
1. 如果网页提示“操作太频繁”等提示，需清理 cookie ，重新获取 url，降低频率或采用其他反爬虫方式解决。
2. 禁止爬取网站中的个人信息。