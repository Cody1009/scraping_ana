# -*- coding: utf-8 -*-
import scrapy
import os
import glob
import csv
import pandas as pd

from gspread_connect import save_to_gsheet


class AnaSpider(scrapy.Spider):
    name = 'ana'
    allowed_domains = ['ana.co.jp']
    start_urls = ['https://www.ana.co.jp/ja/jp/inttour/theme/sale/timesale/']

    def parse(self, response):
        sales = response.css('div.res-coolumn-3-box')
        for sale in sales:
            sale_name = sale.css('div.res-coolumn-3-box>p.res-textbox::text').extract_first()

            price_bold = sale.css('div.res-coolumn-3-box>p.priceArea::text').extract_first()
            price_normal = sale.css('div.res-coolumn-3-box>p.priceArea>span.priceSml::text').extract_first()
            price = price_bold + price_normal

            sale_period = sale.css('div.res-coolumn-3-box>p.periodBox::text')[1].extract()

            sale_link = sale.css(
                'div.res-coolumn-3-box>div.htlCstSrcBtn>p.res-btn-link>a::attr("href")').extract_first()

            yield {"セール名": sale_name, "価格": price, "期間": sale_period, "リンク先": sale_link}

    def close(self, reason):
        # 空のcsvファイルがないとエラーが出る
        save_to_gsheet()


