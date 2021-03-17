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
        imagelink = response.css('img').xpath('@src').extract()
        div = response.css('._373qXS')
        for list in div:
            company = list.css('div._2WkVRV::text').extract()
            price = list.css('div._30jeq3::text').extract()
            size = list.css('a.IRpwTa::text').extract()
            productlink = list.css('._2UzuFa ').xpath("@href").extract()


            
            item['item_company'] = company
            item['item_price'] = price
            item['item_size'] = size
            item['item_imagelink'] = ['https:'+imagelink[0]]
            item['item_productlink'] = productlink

            yield item

        nextpage = 'https://www.flipkart.com/search?q=bags&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page='+ str(FlipkartspiderSpider.pageno)
        if FlipkartspiderSpider.pageno <= 3:
            FlipkartspiderSpider.pageno += 1
            yield response.follow(nextpage,callback=self.parse)
