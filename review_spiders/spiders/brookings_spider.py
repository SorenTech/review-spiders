import Scrapy

class BrookingsSpider(scrapy.Spider):
    name = "Brookings Institution"

    def start_urls = [
            'https://www.brookings.edu/search/?post_type=post&orderby=date',
            'https://www.brookings.edu/search/?post_type=article&orderby=date',
            'https://www.brookings.edu/search/?post_type=essay&orderby=date',
            'https://www.brookings.edu/search/?post_type=interactive&orderby=date',
            'https://www.brookings.edu/search/?post_type=on-the-record&orderby=date',
            'https://www.brookings.edu/search/?post_type=opinion&orderby=date',
            'https://www.brookings.edu/search/?post_type=product&orderby=date',
            'https://www.brookings.edu/search/?post_type=research&orderby=date',
            'https://www.brookings.edu/search/?post_type=techstream&orderby=date',
            'https://www.brookings.edu/search/?post_type=testimony&orderby=date',
            'https://www.brookings.edu/search/?post_type=voter-vital&orderby=date'
        ]

    def parse(self, response):
        for article in response.css('div.article-info'):
            yield {
                'title': article.css('h4.title::text').get(),
                'author': article.css('div.authors::text').getall(),
                'date': article.css('time::text').get(),
                'url': article.css('h4 + a').get(),
                'content': /* follow-link here to get text */
            }
