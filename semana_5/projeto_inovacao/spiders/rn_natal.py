import scrapy


class RnNatalSpider(scrapy.Spider):
    name = 'rn_natal'
    start_urls = ['https://www.natal.rn.gov.br/dom/']

    def parse(self, response):
        yield {"body": response.text}
