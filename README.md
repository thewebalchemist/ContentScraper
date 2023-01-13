## Project Description
**What you should know:**
At least some basics of Python and HTML

## What is Scrapy

Scrapy is a web crawling and scraping framework for Python. To follow links in a page and scrape content in the followed pages, you can use the `FollowAllSpider` class from the `scrapy.spiders` module, which automatically follows all links found in the initial page(s).

You can also create your own spider class and override the `parse` method, where you can specify the links to follow using the `yield` statement and the `response.follow()` method.

For example, in the parse method you can use `response.xpath()` or `response.css()` to select the links to follow, then using `yield` statement with `response.follow()` method to follow the links and scrape the content in the followed pages.

    import scrapy
    
    class ExampleSpider(scrapy.Spider):
        name = "example"
        start_urls = [
            'http://www.example.com/page1',
            'http://www.example.com/page2',
        ]
    
    def parse(self, response):
        for link in response.css('a::attr(href)').getall():
            yield response.follow(link, self.parse_page)
    
    def parse_page(self, response):
        yield {
            'title': response.css('title::text').get(),
            'content': response.css('p::text').getall(),
        }`

 

You can then run the spider using the `scrapy crawl` command, passing the spider name as an argument.


`scrapy crawl example` 

This is a basic example, you can adjust and customize it as per your requirement.
