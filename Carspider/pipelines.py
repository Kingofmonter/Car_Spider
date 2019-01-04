# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy import Request
from urllib import parse

class CarspiderPipeline(object):

    def __init__(self):

        self.conn = pymysql.connect('127.0.0.1','root','root','car_project',charset='utf8',use_unicode=True)
        self.cursor = self.conn.cursor()
        print('链接成功')

    def process_item(self, item, spider):

        insert_sql = """
            insert into project(car_name,car_state,now_price,original_price,car_img,car_urls)
            values (%s,%s,%s,%s,%s,%s)
        """

        for x,y,z,i,n,m in zip(item['car_name'],item['car_state'],item['now_price'],item['original_price'],item['car_img'],item['car_urls']):
            print(x,y,z,i,n,m)

            self.cursor.execute(insert_sql,(x,y,z,i,n,m))
            self.conn.commit()
        print('爬虫结束')


class CarImgPipeline(ImagesPipeline):


    def get_media_requests(self, item, info):

        for img_url in item['car_img']:
            yield Request(parse.urljoin('https:',img_url))

    def item_completed(self, results, item, info):
        img_path = [x['img_path'] for ok,x in results if ok]
        if not img_path:
            raise DropItem('no Image')

        item['img_path'] = img_path
        return item



class CarProjectPipeline(object):

    def __init__(self):

        self.conn = pymysql.connect('127.0.0.1','root','root','car_project',charset='utf8',use_unicode=True)
        self.cursor = self.conn.cursor()
        print('链接成功')

    def process_item(self, item, spider):

        insert_sql = """
            insert into project_detail(car_url,car_title,car_details,car_address,car_basic,car_describe,car_score)
            values (%s,%s,%s,%s,%s,%s,%s)
        """

        for x,y,z,i,n,m in zip(item['car_title'],item['car_details'],item['car_address'],item['car_basic'],item['car_describe'],item['car_score']):
            print(x,y,z,i,n,m)

            self.cursor.execute(insert_sql,(item['car_url'],x,y,z,i,n,m))
            self.conn.commit()
        print('爬虫结束')