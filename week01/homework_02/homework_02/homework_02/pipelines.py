# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class Homework02Pipeline:
    def process_item(self, item, spider):

        moviename = item['moviename']
        movietype = item['movietype']
        releasetime = item['releasetime']
        output = f'|{moviename}|\t|{movietype}|\t|{releasetime}|\n\n'

        with open('./maoyan.csv', 'a+', encoding='utf-8') as f:
            f.write(output)
        return item
