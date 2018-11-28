# -*- coding: utf-8 -*-

import scrapy
import re

from scrapy.loader.processors import MapCompose, Identity


def clear_image_url(val):
    return re.sub(r'\?.+$', '', val)


class BidspotterItem(scrapy.Item):
    lot_number = scrapy.Field()
    lot_title = scrapy.Field()
    lot_description = scrapy.Field()
    image_urls = scrapy.Field(
        input_processor=MapCompose(
            clear_image_url,
        ),
        output_processor=Identity()
    )
    images = scrapy.Field()
    folder_name = scrapy.Field()
