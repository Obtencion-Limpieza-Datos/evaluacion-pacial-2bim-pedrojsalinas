import scrapy

class AlcaldeItem(scrapy.Item):
    canton = scrapy.Field()
    nombre = scrapy.Field()
    partido = scrapy.Field()
