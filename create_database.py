import sqlite3
import pandas as pd
import data_cleaning



# Import series ID from the data_cleaning file
series_id=data_cleaning.series_id   

#Database name
database="economic_db"

#Create a database to store the data collected through
def create_database(table_name,database):
    conn=sqlite3.connect(database)
    cursor = conn.cursor()  
    # Create a database table if not existe
    cursor.execute(f"""CREATE TABLE IF NOT EXISTS {table_name}(
        date TEXT NOT NULL,
        VALUE REAL
                   )""")
    conn.commit()

# Insert Data into SQLite
def insert_into_table(df,table_name,database="economic_db"):
     conn=sqlite3.connect(database)
     cursor=conn.cursor()
     #Set the date column to date type
     df['date'] = df['date'].dt.strftime('%Y-%m-%d')
     data = list(zip(df['date'], df['value']))
    # Insert rows 
     cursor.executemany(f"INSERT INTO {table_name} (date, value) VALUES (?, ?)", data)
     conn.commit()
     conn.close()

#Insert Data into Database tables 
for name,serie in series_id.items():
    data=data_cleaning.fetch_and_clean_data(serie)
    conn=sqlite3.connect("economic_db")
    if data is not None:
            create_database(name,database)
            insert_into_table(data, name)  #  name is table name
            print("All data has been inserted into SQLite database.") 
    else:
        print("Error")



