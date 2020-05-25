from psycopg2 import connect, extensions, sql
import pandas as pd
import os

# declare a new PostgreSQL connection object
DATABASE_URL = os.environ['DATABASE_URL']
conn = connect(DATABASE_URL)

cursor = conn.cursor()

query = """
        INSERT INTO rent_house (city, mq, rooms, baths, price, image, link) 
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

df_rents = pd.read_csv("rents.csv")

for index, row in df_rents.iterrows():

    cursor.execute(query, (row["city"], row["mq"], row["rooms"], row["baths"],
                           row["price"], row["image"], row["link"]))

conn.commit()
cursor.close()
conn.close()
