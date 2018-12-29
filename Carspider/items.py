# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CarspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    car_name = scrapy.Field()
    car_state = scrapy.Field()
    now_price = scrapy.Field()
    original_price = scrapy.Field()
    car_img = scrapy.Field()
    car_urls = scrapy.Field()



class Img699PicItem(scrapy.Item):
    # 分类的标题
    category=scrapy.Field()
    # 存放图片地址
    image_urls=scrapy.Field()
    # 下载成功后返回有关images的一些相关信息
    images=scrapy.Field()