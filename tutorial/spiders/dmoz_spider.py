# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import scrapy
from tutorial.items import DmozItem
class DmozSpider(scrapy.Spider):
	name="dmoz"
	allowed_domains=["http://www.chinadmoz.org/"]
	start_urls=["http://www.chinadmoz.org/industry/1/",
	"http://www.chinadmoz.org/industry/3/"
	]
	def parse(self,response):
		sel =scrapy.selector.Selector(response)
		sites=sel.xpath('//ul/li/div[@class="listbox"]')
		#items=[]
		for site in sites:
			item=DmozItem()
			item['title']=site.xpath('h4/@title').extract()
			item['link']=site.xpath('h4/a/@href').extract()
			item['desc']=site.xpath('p/text()').extract()
			yield item
			#items.append(item)
			
		#return items