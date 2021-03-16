import scrapy
from ..items import FlipkartItem


class FlipkartspiderSpider(scrapy.Spider):
    name = 'flipkartspider'
    pageno =2
    # allowed_domains = ['www.flipkart.com']
    start_urls = [
        'https://www.flipkart.com/search?q=bags&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=1'
    ]

    def parse(self, response):
        item = FlipkartItem()

        div = response.css('._2B099V')
        for list in div:
            company = list.css('div._2WkVRV::text').extract()
            price = list.css('div._30jeq3::text').extract()
            size = list.css('a.IRpwTa::text').extract()


            item['item_company'] = company
            item['item_price'] = price
            item['item_size'] = size

            yield item

