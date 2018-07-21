# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from .const import MONGO_CONNSTR, MONGO_DB, MONGO_COLLECTION

class IpProxyPipeline(object):
    def __init__(self):
        self.cli_mongo = pymongo.MongoClient(MONGO_CONNSTR)
        self.db = self.cli_mongo[MONGO_DB]
        self.coll = self.db[MONGO_COLLECTION]

    def process_item(self, item, spider):
        self.coll.update({'ip': item['ip'], 'port': item['port']}, {'$set': item}, True)

        return item

    def close_spider(self, spider):
        self.cli_mongo.close()
