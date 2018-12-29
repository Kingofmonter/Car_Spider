# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class CarspiderPipeline(object):

    def __init__(self):

        self.conn = pymysql.connect('127.0.0.1','root','123','car_project',charset='utf8',use_unicode=True)
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
