import psycopg2
import pymongo
import csv

class PostgreSQLDatabase:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.cur = self.conn.cursor()
            print("Connected to PostgreSQL database successfully!")
        except psycopg2.Error as e:
            print("Unable to connect to PostgreSQL database:", e)

    def fetch_data(self, query):
        self.cur.execute(query)
        column_names = [desc[0] for desc in self.cur.description]
        data = self.cur.fetchall()
        return column_names, data

    def close(self):
        self.cur.close()
        self.conn.close()
        print("PostgreSQL connection closed.")

class MongoDBDatabase:
    def __init__(self, dbname, host, port):
        self.dbname = dbname
        self.host = host
        self.port = port

    def connect(self):
        try:
            self.client = pymongo.MongoClient(host=self.host, port=self.port)
            self.db = self.client[self.dbname]
            print("Connected to MongoDB database successfully!")
        except pymongo.errors.ConnectionFailure as e:
            print("Unable to connect to MongoDB database:", e)

    def fetch_data(self, collection_name):
        collection = self.db[collection_name]
        return list(collection.find())

    def close(self):
        self.client.close()
        print("MongoDB connection closed.")

def write_to_csv(column_names, data, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(column_names)
        writer.writerows(data)

def main():
    # Connect to PostgreSQL database
    pg_db = PostgreSQLDatabase(
        dbname = 'jobs',
        user='postgres',
        password='postgres',
        host='localhost',
        port='5432'
    )

    pg_db.connect()
    column_names, pg_data = pg_db.fetch_data("SELECT * FROM raw_table")
    pg_db.close()

    #Connect to MongoDB database
    mongo_db = MongoDBDatabase(
        dbname='jobs',
        host='localhost',
        port=5433
    )
    mongo_db.connect()
    #mongo_data = mongo_db.fetch_data("raw_collection")
    mongo_db.close()

    # Write data to CSV files
    write_to_csv(column_names, pg_data, "postgresql_data.csv")
    #write_to_csv(mongo_data, "mongodb_data.csv")

if __name__ == "__main__":
    main()
