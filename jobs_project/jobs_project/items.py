import scrapy

class JobsProjectItem(scrapy.Item):
    slug = scrapy.Field() 
    language = scrapy.Field()
    languages = scrapy.Field()
    req_id = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    street_address = scrapy.Field()
    city = scrapy.Field()
    state = scrapy.Field()
    country = scrapy.Field()
    country_code = scrapy.Field()
    postal_code = scrapy.Field()
    location_type = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
    #categories = scrapy.Field()
    tags = scrapy.Field()
    tags1 = scrapy.Field()
    tags2 = scrapy.Field()
    tags5 = scrapy.Field()
    tags6 = scrapy.Field()
    tags8 = scrapy.Field()
    brand = scrapy.Field()
    department = scrapy.Field()
    recruiter_id = scrapy.Field()
    promotion_value = scrapy.Field()
    salary_frequency = scrapy.Field()
    salary_value = scrapy.Field()
    salary_min_value = scrapy.Field()
    salary_max_value = scrapy.Field()
    salary_currency = scrapy.Field()
    employment_type = scrapy.Field()
    work_hours = scrapy.Field()
    benefits = scrapy.Field()
    hiring_organization = scrapy.Field()
    source = scrapy.Field()
    posted_date = scrapy.Field()
    posting_expiry_date = scrapy.Field()
    apply_url = scrapy.Field()
    internal = scrapy.Field()
    searchable = scrapy.Field()
    applyable = scrapy.Field()
    li_easy_applyable = scrapy.Field()
    ats_code = scrapy.Field()
    #meta_data = scrapy.Field()
    update_date = scrapy.Field()
    create_date = scrapy.Field()
    category = scrapy.Field()
    location_name = scrapy.Field()
    full_location = scrapy.Field()
    short_location = scrapy.Field()
