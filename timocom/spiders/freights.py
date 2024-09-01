import json
import scrapy
import time 
from datetime import datetime
from ..items import TimocomItem
from scrapy.loader import ItemLoader


origins = ['AL','AM','AT','AZ','BA','BE','BG','BY','CH','CY','CZ','DE','DK','EE','ES','EU','FI','FR','GB','GE','GR','HR','HU','IE','IS','IT','KZ','LI','LT','LU','LV','MC','MD','ME','MK','MT','NL','NO','PL','PT','RO','RS','RU','SE','SI','SK','TR','UA']
destinations = ['AL','AM','AT','AZ','BA','BE','BG','BY','CH','CY','CZ','DE','DK','EE','ES','EU','FI','FR','GB','GE','GR','HR','HU','IE','IS','IT','KZ','LI','LT','LU','LV','MC','MD','ME','MK','MT','NL','NO','PL','PT','RO','RS','RU','SE','SI','SK','TR','UA']

class FreightsSpider(scrapy.Spider):
    name = "freights"

    def start_requests(self):
        for origin in origins:
            for destination in destinations:
                
                time.sleep(1) # Slowdown scraping to 1 reqs/sec
                
                yield scrapy.Request(
                    url="https://services.timocom.com/api/barometerData",
                    method="POST",
                    meta={
                        "zyte_api": {
                            "httpResponseBody": True,
                            "httpResponseHeaders": True,
                        },
                        "origin": origin,
                        "destination": destination
                    },
                    body='{"fromCountry":"'+ origin +'","toCountry":"' + destination + '","relationType":"international"}'
                )

    def parse(self, response):
        data = json.loads(response.text)
        item = TimocomItem()

        item["freights"] = data['DATANOW']
        item["origin"] = response.meta['origin']
        item["destination"] = response.meta['destination']
        item["last_updated"] = str(datetime.fromtimestamp(data['LASTUPDATE']))

        return item