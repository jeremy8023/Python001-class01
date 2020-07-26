# -*- coding: utf-8 -*-

# 1.使用 Scrapy 框架和 XPath 抓取猫眼电影的前 10 个电影名称、电影类型和上映时间
# 2. 为Scrapy添加代理IP功能
# 3. 将保存至 csv 文件的功能修改为保持到 MySQL，并在下载部分增加异常捕获和处理机制。
# 备注：代理 IP 可以使用 GitHub 提供的免费 IP 库
'''
    1.添加代理IP(settings.py + middlewares.py)
    2.用scrapy访问https://maoyan.com/films?showType=3，获得response对象(maoyan.py -> start_requests())
    3.用Selector选择前10个的电影名称、类型和上映时间(maoyan.py -> parse())
    4.连接数据库maoyan，并存储到movie_info表中(未完成)
    # values = [(id,'testuser'+str(id)) for id in range(4, 21) ]
    # cursor.executemany('INSERT INTO '+ TABLE_NAME +' values(%s,%s)' ,values)

'''

import scrapy
from scrapy.selector import Selector
#from maoyan_movies.items import MaoyanMoviesPipeline


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/']

    def start_requests(self):
        url = f'https://maoyan.com/films?showType=3'
        #拿到https://maoyan.com/films?showType=3的request对象，通过engine返回response对象给parse
        #注意：request对象和reponse对象是同一个
        yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        #拿到第一页所有电影的对象
        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        print(response.status)
        print(response)
        #选择前10个电影对象
        for movie in movies[:2]:
            # 存放movie_info的列表
            movie_info = {}
            #得到movie_names
            movie_name = movie.xpath('./div[1]/span[1]/text()').extract()[0]
            #movie_info.append(movie_name)
            movie_info['name'] = movie_name
            #得到movie_types
            # extract()将selector对象转换为list对象，之后可作为列表操作
            movie_type = movie.xpath('./div[@class="movie-hover-title"][2]/text()').extract()[1].strip()
            #movie_info.append(movie_type)
            movie_info['type'] = movie_type
            #得到movie_release
            movie_release = movie.xpath('./div[@class="movie-hover-title movie-hover-brief"]/text()').extract()[1].strip()
            #movie_info.append(movie_release)
            movie_info['release'] = movie_release
            # #将movie_info转换为元组对象，方便以后存入数据库
            # trans_movie_info = tuple(movie_info)
            # #添加每一个movie_info
            # movieslist.append(trans_movie_info)
            # print(movie_info)
            # yield一个字典对象
            yield movie_info



        








    
