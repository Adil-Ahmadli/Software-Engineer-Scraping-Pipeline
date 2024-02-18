## Usage
Run `docker compose up` in the highest directory. It will build Scrapy service with dockerfile, and pull Mongo, Redis and PostgreSQL images. It will run these containers. I did not define volumes, so databases are not persistent.

Running Scrapy container first time can take some time as it downloads a lot of dependencies.(my laptop took 40 mins).


Most of the time Scrapy service access PostgreSQL service before it is open to accepting connections. TO solve it, I made Scrapy dependent on PostgreSQL and did add wait_for_postgres.sh script file, to make sure it is Scrapy Service tries until it is sure PostgreSQL is up. Otherwise Scrapy tries once and exits as it can not find anybody on localhost:5432. Problem is that although PostgreSQL is up after some point, the command `pg_isready -h localhost -p 5432 -U postgres` in the shell script always fails and logs. When I call it from terminal it can access database. Most probably it host name/ip address issue: to get access to db from Scrapy service there is different host name/ip address, which I could not find.
Because of the above problem we can not see how system works on docker compose fully.

But after docker compose is up, when i run scrapy code in my terminal eveything is okay. It gets info froom JSON file, runs pipelines to put it into db. I can access db with `psql`, can see `jobs` database, `raw_table` table and its records.

Query.py connects to PostgreSQL, gets whole table and puts it into CSV file.

Altough I have pipeline for MongoDB as i could not connect to its service properly i could not test it.



