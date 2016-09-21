# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.http import FormRequest
from douban.items import DoubanItem
from bs4 import BeautifulSoup
import txt_dict

class DoubanTitleSpider(scrapy.Spider):
    name = "douban.title"
    allowed_domains = ["douban.com"]
    """
    start_urls = (
        'http://www.douban.com',
    )
    """
    def start_requests(self):
        cookies = txt_dict.txt_dict()
        yield scrapy.Request(url='http://www.douban.com/', cookies=cookies, callback=self.parse)


    def parse(self, response):
        html_doc = response.body
        soup = BeautifulSoup(html_doc, "lxml")
        filename = "douban.title"
        with open(filename, 'wb') as f:
            f.write(response.body)
        item = DoubanItem()
        item['title'] = soup.title.string
        item['name'] = soup.find_all('span', class_="name")
        item['corp'] = soup.find_all('span', class_="corp")
        return item 
