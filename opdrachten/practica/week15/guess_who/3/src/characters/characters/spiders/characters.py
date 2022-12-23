import scrapy

from characters
from scrapy.loader import ItemLoader
import logging

class CharacterSpider(scrapy.Spider):
    name = "characters"

    logging.basicConfig(logging.DEBUG)

    # TODO use property
    start_urls = ["http://fullbellylaughs.com/guess-who-board-games-characters"]

    def parse(self, response):

        # //div[@class='row gtr-uniform']
        resp = response.xpath("//div[@class='lpContent']")
        logging.DEBUG(resp)

        # for gwchar in response.xpath("//div[@class='row gtr-uniform']"):
        for gwchar in response.xpath("//div[@class='lpContent']"):
            itemLoader = ItemLoader(item=items.CharItem(), selector=gwchar)
            # //div[@class='gwcharacter']
            # class="col-10 col-10-medium col-6-xsmall"
            itemLoader.add_xpath('char_text', "//div[@class='gwcharacter']/p")
            # itemLoader.add_xpath('joke_text_holder', "//div[@class='joke-text-holder']/p")
            
            yield itemLoader.load_item()