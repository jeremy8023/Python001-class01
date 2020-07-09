# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

'''
    #pymysql连接mysql的一般流程
    1.创建connection
    2.创建游标对象cursor
    3.增删改查IDUS
    4.关闭游标对象cursor
    5.关闭connection对象
'''
import pymysql

dbInfo = {
    'host' : 'localhost',
    'port' : 3306,
    'user' : 'root',
    'password' : '123',
    'db' : 'test'
}


'''
    1.接收yield传过来的item参数
    2.将数据准备成mysql需要的格式
'''

class MaoyanMoviesPipeline:

    def process_item(self, item, spider):
        # 拿到每个电影的信息
        moviename = item['name']
        movietype = item['type']
        movierelease = item['release']

        conn = pymysql.connect(
            host = self.host,
            port = self.port,
            user = self.user,
            password = self.password,
            db = self.db
        )
        # 游标建立的时候就开启了一个隐形的事物
        cur = conn.cursor()
        try:
            values = [moviename,movietype, movierelease]
            print(values)
            cur.execute('INSERT INTO  movieinfo values(%s,%s,%s)' ,values)
            # 关闭游标
            cur.close()
            conn.commit()
        except:
            conn.rollback()
        # 关闭数据库连接
        conn.close()

        return item