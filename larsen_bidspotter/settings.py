# -*- coding: utf-8 -*-

BOT_NAME = 'larsen_bidspotter'

SPIDER_MODULES = ['larsen_bidspotter.spiders']
NEWSPIDER_MODULE = 'larsen_bidspotter.spiders'

IMAGES_STORE = ''
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''

USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'

ROBOTSTXT_OBEY = False

FEED_EXPORT_ENCODING = 'utf-8'
FEED_EXPORT_FIELDS = ['lot_number', 'lot_title', 'lot_description', ]

ITEM_PIPELINES = {
    'larsen_bidspotter.pipelines.LotImagesPipeline': 10,
}
# IMAGES_STORE = '/absolute/path/to/folder/with/images'
