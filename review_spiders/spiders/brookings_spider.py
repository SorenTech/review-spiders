import Scrapy

class BrookingsSpider(scrapy.Spider):
    name = "Brookings Institution"

    def start_urls = [
            'https://www.brookings.edu/'
        ]

    def parse(self, response):
        for article in response.css('div.article-info'):
            yield {
                'title': article.css('h4.title::text').get(),
                'author': article.css('div.authors::text').getall(),
                'date': article.css('time::text').get(),
                'topics': article.css('a.label::text').getall(),
                'url': article.css('h4 + a').get(),
                'content': /* follow-link here to get text */
            }
