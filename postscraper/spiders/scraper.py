# Scraping from URLs

import scrapy

from ..items import PostscraperItem


# Used when scraping from a sitemap
# from scrapy.spiders import SitemapSpider

# class FilteredSitemapSpider(SitemapSpider):
class MySpider(scrapy.Spider):
    name = 'postscraper'
    start_urls = [


'https://example.com/',

 ]
    # sitemap_urls = ['http://example.com/sitemap.xml']


    def parse(self, response):
        
        items = PostscraperItem()

        allContent = response.css('body')

        for content in allContent:
            title = content.css('h1::text').extract()
            post = content.css('.entry-content').extract()


            items['title'] = title
            items['post'] = post

            yield items

        # for sitemap
        # response.url
        # next_page = response.css('.a').getall()
        # yield response.follow(next_page, callback = self.parse)

