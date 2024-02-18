from itemadapter import ItemAdapter
import psycopg2
from psycopg2.extensions import register_adapter, AsIs
import json
import pymongo

def adapt_dict(dict_var):
    return AsIs("'" + json.dumps(dict_var) + "'")


class JobsProjectPipeline:
    def process_item(self, item, spider):
        return item


class SaveToDatabasePipeline:
    def __init__(self):
        register_adapter(dict, adapt_dict)
        self.connection = psycopg2.connect(
            host='localhost',
            port=5432,
            database='jobs',
            user='postgres',
            password='postgres'
        )
        self.cursor = self.connection.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS raw_table (
                id SERIAL PRIMARY KEY,
                slug TEXT,
                language TEXT,
                languages TEXT[],
                req_id TEXT,
                title TEXT,
                description TEXT,
                street_address TEXT,
                city TEXT,
                state TEXT,
                country TEXT,
                country_code TEXT,
                postal_code TEXT,
                location_type TEXT,
                latitude double precision,
                longitude double precision,
                tags text[],
                tags1 text[],
                tags2 text[],
                tags5 text[],
                tags6 text[],
                tags8 text[],
                brand text,
                department text,
                recruiter_id text,
                promotion_value integer,
                salary_frequency text,
                salary_value integer,
                salary_min_value integer,
                salary_max_value integer,
                salary_currency text,
                employment_type text,
                work_hours text,
                benefits text[],
                hiring_organization text,
                source text,
                posted_date DATE,
                posting_expiry_date DATE,
                apply_url text,
                internal boolean,
                searchable boolean,
                applyable boolean,
                li_easy_applyable boolean,
                ats_code text,
                update_date DATE,
                create_date DATE,
                category text[],
                location_name text,
                full_location text,
                short_location text
                )""")            
        self.connection.commit()

    def process_item(self, item, spider):
        self.cursor.execute("""
            INSERT INTO raw_table (
            slug, language, languages, req_id, title, description, street_address, city, state, country, country_code,
            postal_code, location_type, latitude, longitude, tags, tags1, tags2, tags5, tags6, tags8, brand,
            department, recruiter_id, promotion_value, salary_frequency, salary_value, salary_min_value, salary_max_value,
            salary_currency, employment_type, work_hours, benefits, hiring_organization, source, posted_date,
            posting_expiry_date, apply_url, internal, searchable, applyable, li_easy_applyable, ats_code,
            update_date, create_date, category, location_name, full_location, short_location) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", (
                item['slug'], item['language'], item['languages'], item['req_id'], item['title'],
                item['description'], item['street_address'], item['city'], item['state'], item['country'],
                item['country_code'], item['postal_code'], item['location_type'], item['latitude'],
                item['longitude'], item['tags'], item['tags1'], item['tags2'],
                item['tags5'], item['tags6'], item['tags8'], item['brand'], item['department'],
                item['recruiter_id'], item['promotion_value'], item['salary_frequency'], item['salary_value'],
                item['salary_min_value'], item['salary_max_value'], item['salary_currency'],
                item['employment_type'], item['work_hours'], item['benefits'], item['hiring_organization'],
                item['source'], item['posted_date'], item['posting_expiry_date'], item['apply_url'],
                item['internal'], item['searchable'], item['applyable'], item['li_easy_applyable'],
                item['ats_code'], item['update_date'], item['create_date'],
                item['category'], item['location_name'], item['full_location'], item['short_location']
            ))
        
        self.connection.commit()
        return item
    
    def close_spider(self, spider):
        self.cursor.close()
        self.connection.close()


class SaveToMongoDBPipeline:
    def __init__(self):
        self.client = pymongo.MongoClient("localhost", 5433)
        self.db = self.client["jobs"]
        self.collection = self.db["raw_collection"]

    def process_item(self, item, spider):
        self.collection.insert_one({
            "slug": item['slug'],
            "language": item['language'],
            "languages": item['languages'],
            "req_id": item['req_id'],
            "title": item['title'],
            "description": item['description'],
            "street_address": item['street_address'],
            "city": item['city'],
            "state": item['state'],
            "country": item['country'],
            "country_code": item['country_code'],
            "postal_code": item['postal_code'],
            "location_type": item['location_type'],
            "latitude": item['latitude'],
            "longitude": item['longitude'],
            "tags": item['tags'],
            "tags1": item['tags1'],
            "tags2": item['tags2'],
            "tags5": item['tags5'],
            "tags6": item['tags6'],
            "tags8": item['tags8'],
            "brand": item['brand'],
            "department": item['department'],
            "recruiter_id": item['recruiter_id'],
            "promotion_value": item['promotion_value'],
            "salary_frequency": item['salary_frequency'],
            "salary_value": item['salary_value'],
            "salary_min_value": item['salary_min_value'],
            "salary_max_value": item['salary_max_value'],
            "salary_currency": item['salary_currency'],
            "employment_type": item['employment_type'],
            "work_hours": item['work_hours'],
            "benefits": item['benefits'],
            "hiring_organization": item['hiring_organization'],
            "source": item['source'],
            "posted_date": item['posted_date'],
            "posting_expiry_date": item['posting_expiry_date'],
            "apply_url": item['apply_url'],
            "internal": item['internal'],
            "searchable": item['searchable'],
            "applyable": item['applyable'],
            "li_easy_applyable": item['li_easy_applyable'],
            "ats_code": item['ats_code'],
            "update_date": item['update_date'],
            "create_date": item['create_date'],
            "category": item['category'],
            "location_name": item['location_name'],
            "full_location": item['full_location'],
            "short_location": item['short_location']
        })
        return item
    
    def close_spider(self, spider):
        self.client.close()
