# -*- coding: utf-8 -*-
import scrapy
import re

from larsen_bidspotter.items import BidspotterItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose


class BidspotterSpider(scrapy.Spider):
    """
    https://doc.scrapy.org/en/latest/topics/spiders.html#spider-arguments
    The default __init__ method will take any spider arguments and copy them to the spider as attributes. 

    Attributes
    ----------
    url : str
        target auction url
    """

    name = 'bidspotter'
    allowed_domains = ['bidspotter.com']

    def start_requests(self):
        headers = {
            'Host': 'www.bidspotter.com',
            'Referer': self.url,
        }

        cookies = {
            'user_preference_pagesize': '500',
        }

        self.auction_id = re.search(r'/catalogue-id-(.+)$', self.url).group(1)

        yield scrapy.Request(self.url, headers=headers, cookies=cookies, callback=self.parse_auction_catalog)

    def parse_auction_catalog(self, response):
        lots = response.xpath('//article//h1[not(@*)]/a[@data-lot-id]')

        for lot in lots:
            yield response.follow(lot, callback=self.parse_lot)

    def parse_lot(self, response):
        l = ItemLoader(item=BidspotterItem(), response=response)
        l.default_input_processor = MapCompose(
            lambda x: x.strip(),
        )
        l.default_output_processor = TakeFirst()

        l.add_xpath('lot_number', '//p[@class="lot-number"]/text()')
        l.add_xpath('lot_title', '//h2[@ng-bind="lot.title"]/text()')
        l.add_xpath('lot_description', '//div[@data-tab="description"]/div[contains(@class, "tinyMCEContent")]/text()')
        l.add_xpath('image_urls', '//div[contains(@class, "lot-details-image ")]//img[@data-lazy]/@data-lazy')
        l.add_value('folder_name', self.auction_id)

        yield l.load_item()
