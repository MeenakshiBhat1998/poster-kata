"""
The ETL class is responsible for extracting data from the source database, transforming it as per the business requirements, 
and loading it into the destination data warehouse (dw) database. 

"""

import random
import asyncio

from faker import Faker
from loguru import logger
from datetime import datetime

from app.common import get_db_connection
from app.starships import fetch_all_starships

fake = Faker()

class ETL:
    def __init__(self):
        pass

    def load_source_data(self):
        """
        Generates and inserts fake data into the source database.

        This method connects to the PostgreSQL database, generates 100 records of fake data
        for the source table, and inserts them into the database. The generated data includes
        poster content, quantity, price, email, sales representative, and promo code.
        """

        conn = get_db_connection()
        cur = conn.cursor()

        # Generate and insert data
        logger.info("Generating data for source table")
        for _ in range(100):  # Generate 100 records
            poster_content = random.choice(['Millennium Falcon', 'X-Wing', 'TIE Fighter'])
            quantity = random.randint(1, 10)
            price = round(random.uniform(10.0, 400.0), 2)
            email = fake.email()
            sales_rep = fake.name()
            promo_code = fake.lexify(text='??????')
        
            cur.execute(
                "INSERT INTO source (poster_content, quantity, price, email, sales_rep, promo_code) VALUES (%s, %s, %s, %s, %s, %s)",
                (poster_content, quantity, price, email, sales_rep, promo_code)
            )

        # Commit changes and close connection
        logger.info("Data loaded successfully to source table")
        conn.commit()
        cur.close() 
        conn.close()

    def transform_load_dw_data(self):
        """
        Transforms and loads data into the dw database.

        This method connects to the PostgreSQL database, retrieves data from the source table,
        fetches additional starship data from the SWAPI API, and inserts the transformed data
        into the dw table. The transformation includes matching poster content with starship names,
        and adding film name, release date, and starship class to the data.
        """
        conn = get_db_connection()
        cur = conn.cursor()
        logger.info("Data loaded successfully to dw table")

        cur.execute("SELECT poster_content, quantity, price, sales_rep, promo_code FROM source")
        rows = cur.fetchall()

        starships = asyncio.run(fetch_all_starships())
        
        for starship in starships:
            for row in rows:
                if row[0] == starship['name']:
                    release_date = datetime.strptime(starship['release_date'], '%Y-%m-%d').date()
                    cur.execute(
                        "INSERT INTO dw (poster_content, quantity, price, sales_rep, promo_code, starship_name, film_name, release_date, starship_class) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                        (row[0], row[1], row[2], row[3], row[4], starship['name'], starship['film_name'], release_date, starship['starship_class'])
                    )

        logger.info("Data loaded successfully to dw table")
        conn.commit()
        cur.close()
        conn.close()
