import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from review_spiders.items import ReviewItem

class LawfareSpider(scapy.Spider):
    name="Lawfare"
    allowed_domains=['lawfareblog.com']
    start_urls = [
        'https://www.lawfareblog.com/'
    ]

    rules = (
        Rule(LinkExtractor(allow=('*'), callback='parse_blog'))
    )

    def parse_blog(self, response):
        item = ReviewItem()
        item['publisher'] = "Lawfare"
        item['weight'] = 1.5
        item['title'] = response.css('h1.title::text').get()
        item['authors'] = response.css('a.author__link::text').getall()
        item['date'] = response.css('div.article_top__meta__inner datetime::text').get()
        item['topic'] = response.css('div.pane-node-field-article-topics div ul li a::text').getall()
        item['tags'] = response.css('div.pane-node-field-article-tags div ul li a::text').getall()
        item['content'] = response.css('div.pane-node-body').get()
