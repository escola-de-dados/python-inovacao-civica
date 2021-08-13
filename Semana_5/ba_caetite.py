import datetime
import re

import scrapy

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class BaCaetiteSpider(BaseGazetteSpider):
    name = "ba_caetite"
    TERRITORY_ID = "2905206"
    allowed_domains = ["procedebahia.com.br"]
    start_date = datetime.date(2017, 4, 3)
    start_urls = ["http://www.procedebahia.com.br/ba/caetite/edicoes"]

    def parse(self, response):
        editions = response.xpath("//div[@id='edicoes']/ul[@class!='grid']")
        for edition in editions:
            link = edition.xpath("./li[2]/a/@href").get()
            title = edition.xpath("./li[2]/text()").get()
            edition_number = re.search(r"Edição Nº. (\d+)", title).group(1)
            date_text = edition.xpath("./li[1]/a/text()").get().strip()
            date = datetime.datetime.strptime(date_text, "%d/%m/%Y").date()

            if date < self.start_date:
                return

            yield Gazette(
                date=date,
                edition_number=edition_number,
                file_urls=[link],
                power="executive",
            )

        next_page_link = response.xpath("//div[@class='proximo']/a/@href").get()
        if next_page_link:
            yield scrapy.Request(response.urljoin(next_page_link), callback=self.parse)
