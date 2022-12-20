import scrapy
from characters.items import CharItem
from scrapy.loader import ItemLoader


class CharacterSpider(scrapy.Spider):
    name = "characters"

    # TODO use property
    start_urls = ["http://fullbellylaughs.com/guess-who-board-games-characters"]

    def parse(self, response):

        # //div[@class='row gtr-uniform']
        
        
        # for gwchar in response.xpath("//div[@class='row gtr-uniform']"):
        for gwchar in response.xpath("//div[@class='lpContent']"):
            itemLoader = ItemLoader(item=CharItem(), selector=gwchar)
            # //div[@class='gwcharacter']
            # class="col-10 col-10-medium col-6-xsmall"
            itemLoader.add_xpath('char_text', "//div[@class='gwcharacter']/p")
            # itemLoader.add_xpath('joke_text_holder', "//div[@class='joke-text-holder']/p")
            
            yield itemLoader.load_item()