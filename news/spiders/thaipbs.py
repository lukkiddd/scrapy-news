# -*- coding: utf-8 -*-
import scrapy
import re


class ThaipbsSpider(scrapy.Spider):
    name = 'thaipbs'
    allowed_domains = ['news.thaipbs.or.th']
    start_urls = ['http://news.thaipbs.or.th/content']

    def start_requests(self):
        url = "http://news.thaipbs.or.th/content/{}"
        for i in range(0, 300000):
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
