import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class MoviSpider(CrawlSpider):
    name = 'movi'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/chart/top/?ref_=nv_mv_250']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//td[@class="title"]/a'), callback='parse_item'),
    )

    def parse_item(self, response):
        yield{
            'Title': response.xpath('//div[@class="title_wrapper"]/h1/text()').get(),
            'Year': response.xpath('//span[@id="titleYear"]/a/text()').get(),
            'Time': response.xpath('normalize-space((//time)/text())').get(),
            'Genere': response.xpath('//div[@class="subtext"]/a/text()').get(),
            'Rating': response.xpath('//span[@itemprop="ratingValue"]/text()').get(),
            'Rating_Count': response.xpath('//span[@itemprop="ratingCount"]/text()').get(),
            'Movi_Link': response.url
        }
