import json
import scrapy
from datetime import datetime
from ..items import TimocomItem
from scrapy.loader import ItemLoader

origins = ['PL', 'NL']
destinations = ['DE', 'FR', 'IT']  # Example with multiple destinations

class FreightsSpider(scrapy.Spider):
    name = "freights"

    def start_requests(self):
        for origin in origins:
            for destination in destinations:
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