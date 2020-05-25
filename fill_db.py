from psycopg2 import connect, extensions, sql
import pandas as pd

# declare a new PostgreSQL connection object
conn = connect(
    dbname="rent",
    user="antonio",
    host="localhost",
    password="antonio"
)

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
