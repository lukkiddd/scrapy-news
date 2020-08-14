# -*- coding: utf-8 -*-
import scrapy

class PrachataiSpider(scrapy.Spider):
    name = 'prachatai'
    allowed_domains = ['prachatai.com']
    start_urls = ['http://prachatai.com/']

    def __init__(self, *args, **kwargs):
        super(PrachataiSpider, self).__init__(*args, **kwargs)
        self.start_id = int(getattr(self, 'start_id', 0))
        self.end_id = int(getattr(self, 'end_id', 80000))

    def start_requests(self):
        url = "https://prachatai.com/print/{}"
        for i in range(self.start_id, self.end_id):
            yield scrapy.Request(url.format(i), callback=self.parse, meta={"url": url.format(i)})

    def parse(self, response):
        item = {
            "url": response.meta['url'],
            "id": response.meta['url'].split('/')[-1],
            "date": response.css(".submitted-by::text").extract_first().split(", ")[-1],
            "title": response.css('h2::text, .node-title::text').extract_first(),
            "body_html": ''.join(response.css('.field-name-body').extract()),
            "body_text": ''.join(response.css('.field-name-body p::text, .field-name-body h4 stong::text, .field-name-body span::text').extract()),
            "labels": response.css("div.field-type-taxonomy-term-reference div.field-item a::text").extract()
        }
        yield item