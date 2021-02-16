# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exporters import JsonLinesItemExporter

class ReviewSpidersPipeline:
    def open_spider(self, spider):
        self.items_to_export = {}

    def close_spider(self, spider):
        for exporter in self.items_to_export.values():
            exporter.finish_exporting()

    def _exporter_for_item(self, item):
        adapter = ItemAdapter(item)
        if item not in items_to_export:
            f = open('~/Code/soren-review/test-data.json', "w")
            exporter = JsonLinesItemExporter(f)
            exporter.start_exporting()
            self.items_to_export = exporter
        return self.items_to_export

    def process_item(self, item, spider):
        exporter = self._exporter_for_item(item)
        exporter.export_item(item)
        return item



