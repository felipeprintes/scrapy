# -*- coding: utf-8 -*-
import scrapy
from extensao.extensao.items import ExtensaoItem

class ExtensaoSpider(scrapy.Spider):
    name = 'Extensao'
    allowed_domains = ['https://www.geografiaopinativa.com.br/2013/09/lista-de-estados-brasileiros-por.html']
    start_urls = ['http://www.geografiaopinativa.com.br/2013/09/lista-de-estados-brasileiros-por.html/']

    def __init__(self, extensaoTerritorial,vet):
        self.extensaoTerritorial = extensaoTerritorial
        self.vet = vet

    def print_vet(vet):
        print(vet)

    def parse(self, response):
        estado = response.xpath("//td[@class='xl66']//text()").extract()
        extensao = response.xpath("//td[@class='xl67']//text()").extract()

        extensaoTerritorial = ExtensaoItem(estado = estado, extensao = extensao)
        
        self.print_item(extensaoTerritorial)

        return extensaoTerritorial

    def print_item(self, extensaoTerritorial):
        vet = []
        j = 0 
        print("Estado ---- Extensao")
        print("---------------------")
        for i in extensaoTerritorial['estado']:
            while j<len(extensaoTerritorial['extensao']):
                print("{}: {}".format(i, extensaoTerritorial['extensao'][j]))
                j+=1
                vet.append(i)
                break
        return vet