# -*- coding: utf-8 -*-
import scrapy
import re


class ThaipbsSpider(scrapy.Spider):
    name = 'thaipbs'
    allowed_domains = ['news.thaipbs.or.th']
    start_urls = ['http://news.thaipbs.or.th/content']

    def __init__(self, *args, **kwargs):
        super(ThaipbsSpider, self).__init__(*args, **kwargs)
        self.start_id = int(getattr(self, 'start_id', 0))
        self.end_id = int(getattr(self, 'end_id', 80000))

    def start_requests(self):
        url = "http://news.thaipbs.or.th/content/{}"
        for i in range(self.start_id, self.end_id):
            yield scrapy.Request(url.format(i), callback=self.parse,
                    meta={'dont_redirect': True, 'id': i})

    def parse(self, response):
        
        title = response.css(".content-title::text").extract_first()
        metadata = response.css(".content-meta span::text").extract()
        content = response.css('article *::text').extract()
        content = ' '.join(content).strip()
        content = re.sub("\s+", " ", content)

        time = metadata[0]
        date = metadata[1].strip()
        datetime = date + " " + time

        tags = response.css('.tag-list a::text').extract()
        category = response.css(".breadcrumb a::text").extract()[-1]

        yield {
            "id": response.meta.get("id"),
            "url": response.url,
            "body_html": str(response.body),
            "title": title,
            "category": category,
            "labels": tags,
            "body_text": content,
            "datetime": datetime,
        }
