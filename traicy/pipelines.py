from scrapy import signals
from scrapy.contrib.exporter import CsvItemExporter
from gspread_connect import save_to_gsheet
import pandas as pd

#  csvファイルを出力するために必要
class SalesPipeline(object):
    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        self.file = open('output.csv', 'w+b')
        self.exporter = CsvItemExporter(self.file)
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        self.file.close()


    def process_item(self, item, spider):
        self.exporter.export_item(item)
        data = pd.read_csv('./output.csv')
        save_to_gsheet(data)
        return item
