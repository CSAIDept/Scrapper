import scrapy
from ..items import CircularItem

class CircularSpider(scrapy.Spider):
    name = "circular"
    start_urls = [
        "https://www.imsnsit.org/imsnsit/notifications.php"
    ]

    def parse(self, response):
        items = CircularItem()
        all = response.xpath('//tr')  # select all table items
        for x in all:
            date = x.xpath('.//td/font[@size="3"]/text()').get()  # filter them by date
            if not date:
                continue
            cirName = x.xpath('.//a/font/text()').get()
            cirLink = x.xpath('.//a[@title="NOTICES / CIRCULARS"]/@href').get()
            items["Name"] = cirName
            items["href"] = cirLink
            items["Date"] = date
            yield items



