import Scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class BrookingsSpider(scrapy.Spider):
    name = "Brookings Institution"
    allowed_domains = ['brookings.edu']
    start_urls = [
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
        ]

    rules = (
        Rule(LinkExtractor(allow=('\/blog\/', '\/articles\/', '\/on-the-record\/', '\/opinion\/', '\/product\/', '\/research\/', )), callback='parse_blog'),

        Rule(LinkExtractor(allow=('\/essay\/', )), callback='parse_essay'),
        Rule(LinkExtractor(allow=('\/techstream\/', )), callback='parse_techstream'),
        Rule(LinkExtractor(allow=('\/search\/', )), callback='parse_default')
    )

    def parse_blog(self, response):
        item = scrapy.Item()
        item['title'] = response.css('h1.report-title::text').get()
        item['authors'] = response.css('span.names a span::text').getall()
        item['date'] = response.css('time.date::text').get()
        item['topic'] = response.css('a.label::text').getall()
        item['tags'] = response.css('a.tag::text').getall()
        item['content'] = response.css('div.post-body').get()

    def parse_essay(self, response):
        item = scrapy.Item()
        item['title'] = response.css('h1.block--essay-hero__title::text').get()
        item['sub-title'] = response.css('div.block--essay-hero__sub-title::text').get()
        item['authors'] = response.css('div.block--essay-author a::text').getall()
        item['date'] = response.css('div.block--essay-pub-date div::text').get()
        item['content'] = response.css('div.post-body').get()
        item['copyright'] = response.css('span.copyright::text').get()

    def parse_techstream(self, response):
        item = scrapy.Item()
        item['title'] = response.css('a.techstream--title::text').get()
        item['authors'] = response.css('div.techstream--authors a span::text').getall()
        item['date'] = response.css('span.techstream--pubdate::text').get()
        item['content'] = response.css('div.techstream--content').get()

    def parse_default(self, response):
        for article in response.css('div.article-info'):
            yield {
                'title': article.css('h4.title a::text').get(),
                'author': article.css('div.authors a span::text').getall(),
                'date': article.css('time::text').get(),
                'url': article.css('h4.title a::attr(href)').get(),
            }

