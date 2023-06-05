import scrapy
from scrapy import Selector, Request
from scrapy.http import HtmlResponse

from demo.items import MovieItem


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250?start=0&filter=']

    def parse(self, response: HtmlResponse):
        sel = Selector(response)
        movie_items = sel.css('#content > div > div.article > ol > li')
        for movie_sel in movie_items:
            item = MovieItem()
            item['title'] = movie_sel.css('.title::text').extract_first()
            item['score'] = movie_sel.css('.rating_num::text').extract_first()
            item['motto'] = movie_sel.css('.inq::text').extract_first()
            yield item

        hrefs = sel.css('#content > div > div.article > div.paginator > a::attr("href")')
        for href in hrefs:
            full_url = response.urljoin(href.extract())
            yield Request(url=full_url)