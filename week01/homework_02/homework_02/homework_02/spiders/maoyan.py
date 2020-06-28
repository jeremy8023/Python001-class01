# -*- coding: utf-8 -*-
import scrapy
from homework_02.items import Homework02Item
from scrapy.selector import Selector

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['https://maoyan.com/films?showType=3']
    start_urls = ['https://maoyan.com/films?showType=3']

    # 拿到maoyan首页的请求对象，也就是说，返回的是整个maoyan的html页面
    def start_requests(self):
        url = f'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url, callback=self.parse)

    
    #解析页面函数,response对象是engine给的，不用关心
    def parse(self, response):
        print(response.text)
        item = Homework02Item()
        moviesinfo = Selector(response=response).xpath('//div[@class="movie-hover-info"]')

        for movie in moviesinfo[:10]:
            #movie返回的是每个电影的div内容，类型是数组
            moviename = movie.xpath('./div[1]/text()').extract_first()
            movietype = movie.xpath('./div[3]/text()').extract()
            releasetime = movie.xpath('./div[4]/text()').extract()

            item['moviename'] = moviename
            item['movietype'] = movietype
            item['releasetime'] = releasetime

        yield item