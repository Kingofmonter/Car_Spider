import scrapy
import requests
from scrapy import Request
from urllib import parse
from ..items import CarspiderItem


class CarSpider(scrapy.Spider):
    name = 'car'
    allowed_domains = ['https://www.che168.com/wenzhou/']
    start_urls = ['https://www.che168.com/china/a0_0msdgscncgpi1ltocsp1exx0/']

    def parse(self, response):
        #全部汽车信息
        car_name = response.css('.list-photo-li .list-photo-info .car-series::text').extract()
        car_state = response.css('.list-photo-li .list-photo-info p::text').extract()
        now_price = response.css('.list-photo-li .list-photo-info .price-box .price::text').extract()
        original_price = response.css('.list-photo-li .list-photo-info .price-box .original-price::text').extract()
        car_img = response.css('.list-photo-li .img img::attr(src)').extract()
        car_urls = response.css('.list-photo-li .carinfo::attr(href)').extract()
        next_url = response.css('.page-item-next::attr(href)').extract()[0]

        item = CarspiderItem(car_name=car_name,car_state=car_state,now_price=now_price,original_price=original_price,car_img=car_img,car_urls=car_urls)

        yield item
        # item = CarspiderItem()
        # item['car_name'] = car_name
        # item['car_state'] =


        # for car_url in car_urls:
        #     yield Request(url=parse.urljoin('https://www.che168.com', car_url), callback=self.detail_parse,
        #                   dont_filter=True)

        if next_url:
            yield Request(url=parse.urljoin('https://www.che168.com', next_url), callback=self.parse, dont_filter=True)

    def detail_parse(self, response):
        #汽车详情页面
        car_title = response.css('.car-title h2::text').extract()
        car_details = response.css('.details ul li span').extract()
        car_address = response.css('.car-address::text').extract()
        car_basic = response.css('.infotext-list .grid-6::text').extract()
        car_describe = response.css('.businessmen-note .tip-content::text').extract()[0]
        car_score = response.css('#kb_agvCount::text').extract()

        car_price = response.css('.grid-10 img::attr(src2)').extract()

    def img_base(self, response, **kwargs):
        #图片下载
        if kwargs:
            pass