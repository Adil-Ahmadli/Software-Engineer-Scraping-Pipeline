import json
import scrapy

class JobSpider(scrapy.Spider):
	name = 'job_spider'
	#custom_settings = {
    #	'ITEM_PIPELINES': {
    #    		'job_spider.pipelines.yourPipeline': 300,
    #	},
	#}

	def __init__(self, **kwargs):
		pass

	def start_requests(self):
		# your code here
		# make sure you can send a request locally at the file
		# if you can't get this to work, do not waste too much time here
		# instead load the json file inside parse_page
		yield scrapy.Request(
					url='file:////home/PATH_TO_JSON', 
					callback=self.parse_page,
					)
		pass
			

	def parse(self, response):
        # your code here
		# load json files using response.text
        # loop over data
		# return items
		pass