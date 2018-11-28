# -*- coding: utf-8 -*-

from scrapy.http import Request
from scrapy.pipelines.images import ImagesPipeline


class LarsenBidspotterPipeline(object):
    def process_item(self, item, spider):
        return item

class LotImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        return [Request(img_url, meta={'image_name': item['lot_number'], 'folder_name': item['folder_name'], 'img_index': img_index}) for img_index, img_url in enumerate(item.get('image_urls', []), 1)]


    def file_path(self, request, response=None, info=None):
        return 'bidspotter/{folder_name}/{image_name}_{image_index}.jpg'.format(
            folder_name=request.meta['folder_name'],
            image_name=request.meta['image_name'],
            image_index=request.meta['img_index']
        )
