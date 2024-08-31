import json
import scrapy
from datetime import datetime

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

        # Extract values from the JSON
        datanow = data['DATANOW']
        last_update = datetime.fromtimestamp(data['LASTUPDATE'])
        destination = response.meta['destination']
        origin = response.meta['origin']

        print("Origin: ",origin," Destination: ", destination," Freights: ", datanow," Last update: ",last_update)