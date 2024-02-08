import scrapy


class IetfSpider(scrapy.Spider):
    name = "ietf"
    allowed_domains = ["pythonscraping.com"]
    start_urls = ["https://pythonscraping.com/linkedin/ietf.html"]

    def parse(self, response):
        # title = response.css('span, title::text').get()
        # title = response.xpath('//span[@class="title"]/text()').get()
        return {
            "number": response.xpath('//span[@class="rfc-no"]/text()').get(),
            "title": response.xpath('//meta[@name="DC.Date.Title"]/@content'),
            "author": response.xpath('//meta[@name="DC.Creator"]/@content'),
            'date': response.xpath('//span[@class="date"]/text()').get(),
            'description': response.xpath('//meta[@name="DC.Description"]/@content'),
            'company': response.xpath('//span[@class="author-name"]/text()').get(),
            'address': response.xpath('//span[@class="address"]/text()').get(),
            'headings': response.xpath('//span[@class="subheading"]/text()').get(),
            'text': w3lib.html.remove_tags(response.xpath('//div[@class="text"]').get()),
            
            }
        # pass
