import scrapy


class QuotesSpider(scrapy.Spider):
    name = "partidos"
    start_urls = ['https://es.wikipedia.org/wiki/Anexo:Resultados_de_las_elecciones_seccionales_de_Ecuador_de_2014']


    def parse(self, response):
        for l in response.css('.mw-parser-output'):
            cantones =l.xpath('//table[@class = "wikitable"]/tbody/tr/td[1]/a/text()').extract()
            partidos = l.xpath('//table[@class = "wikitable"]/tbody/tr/td[3]/a/text()').extract()
            nombres = l.xpath('//table[@class = "wikitable"]/tbody/tr/td[2]/text()').extract()
            for partido in partidos:
                yield {
                    'partido': partido
                }
 # for l in response.css('.mw-parser-output'):
 #    cantones =l.xpath('//table[@class = "wikitable"]/tbody/tr/td[1]/a/text()').extract()
 #    nombres = l.xpath('//table[@class = "wikitable"]/tbody/tr/td[2]/text()').extract()
 #    partidos = l.xpath('//table[@class = "wikitable"]/tbody/tr/td[3]/a/text()').extract()
