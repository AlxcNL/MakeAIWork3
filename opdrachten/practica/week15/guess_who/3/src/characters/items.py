# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags

def remove_whitespace(value):
    return value.strip()    

class CharItem(scrapy.Item):
    # define the fields for your item here like:
    char_text = scrapy.Field(
        input_processor = MapCompose(remove_tags, remove_whitespace),
        output_processor = TakeFirst()

    )
