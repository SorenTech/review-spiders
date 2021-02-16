# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exporters import JsonLinesItemExporter

class ReviewSpidersPipeline:
    def close_spider(self, spider):
        exporter.finish_exporting()

    def _exporter_for_item(self, item):
        adapter = ItemAdapter(item)
        f = open('~/Code/soren-review/test-data.json')
        exporter = JsonLinesItemExporter(f)
        exporter.start_exporting()

    def process_item(self, item, spider):
        exporter = self._exporter_for_item(item)
        exporter.export_item(item)
        return item



