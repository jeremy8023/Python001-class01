'''
    作业要求：
    1.安装并使用 requests、bs4 库，
    2.爬取猫眼电影（https://maoyan.com/films?showType=3）的前 10 个电影名称、电影类型和上映时间，
    3.并以 UTF-8 字符集保存到 csv 格式的文件中。
'''

'''
    整体思路：
    pageturn可以自动翻页，遍历每一个页面
    requests+bs4.beautifulsope用来打卡每一个电影的详情页面
    requests+xpath（lxml.xtree）用来抽取电影的详情信息
    pandas用来保存页面信息
'''

# 1.导入相关包
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

# 2.获取猫眼电影（https://maoyan.com/films?showType=3）的网页信息
myurl = 'https://maoyan.com/films?showType=3'

#拼装header
myurl = 'https://maoyan.com/films?showType=3'
cookie = '__mta=174554781.1593244768753.1593263013742.1593264446269.22; uuid_n_v=v1; uuid=1F2DC520B84C11EA909D9FF2C00A78C38E050B724EB54FA6B72BEB2B4AE607C0; _csrf=c507274905316cfcd2b1f6b1a9abb20583c766753aa56a8c49f0257541d15f17; mojo-uuid=28fc2f6d4bab70569b5057c1faa895c5; _lxsdk_cuid=172f4c9d7abc8-06f4ce6e31b605-31617402-13c680-172f4c9d7ab76; _lxsdk=1F2DC520B84C11EA909D9FF2C00A78C38E050B724EB54FA6B72BEB2B4AE607C0; recentCis=352%3D65%3D1212%3D150; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593244769,1593341483; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593341499; __mta=174554781.1593244768753.1593264446269.1593341499084.23; _lxsdk_s=172fac2aee8-a8a-968-2cd%7C%7C1'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
header = {'user-agent':user_agent,'cookie':cookie}
#拿到html，并转换为BeautifulSoup
response = requests.get(myurl, headers=header)
bs_info = bs(response.text,'html.parser')

# 3.解析前10个电影名称、电影类型和上映时间
movieinfo = []
temp = []

for movietags in bs_info.find_all('div', limit=10, class_='movie-hover-info'):

    movielist = movietags.find_all('div')

    moviename = movielist[0].find('span',).text
    movietype = movielist[1].get_text().strip()
    movieshowtime = movielist[3].get_text().strip()
    movieinfo = [moviename, movietype, movieshowtime]
    temp.append(movieinfo)
print("-"*100)
print(temp)

# 4.以UTF-8字符集保存到csv格式
top10movies = pd.DataFrame(data = temp)
top10movies.to_csv('./movietop10.csv', encoding='utf8', index=False, header=False)
