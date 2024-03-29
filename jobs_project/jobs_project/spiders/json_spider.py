import json
import scrapy
from jobs_project.items import JobsProjectItem
from jobs_project.spiders.helper import nullify

class JobSpider(scrapy.Spider):
	name = "job_spider"
	custom_settings = {
    	'ITEM_PIPELINES': {
        		'jobs_project.pipelines.JobsProjectPipeline': 300,
				'jobs_project.pipelines.SaveToDatabasePipeline': 400,
				'jobs_project.pipelines.SaveToMongoDBPipeline': 500,
    	},
	}

	def __init__(self, **kwargs):
		pass

	def start_requests(self):
		yield scrapy.Request(
						url='file:///home/adil/Desktop/Software-Engineer-Scraping-Pipeline/s01.json', 
						callback=self.parse,
					)


	def parse(self, response):
		data 	 =  json.loads(response.text)
		length   =  len(data["jobs"])
		for i in range(length):
			job = JobsProjectItem()
			job = nullify(job)
			keys = data["jobs"][i]["data"].keys()
			for key in keys:
				if key != "meta_data" and key != "categories":
					job[key] = data["jobs"][i]["data"][key]
			yield job