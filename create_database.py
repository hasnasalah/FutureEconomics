import sqlite3
import pandas as pd
import data_cleaning



# import series id from the data_cleaning file
series_id=data_cleaning.series_id   
#database name
database="economic_db"
#create a database to store teh data collected throgh api
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
     df['date'] = df['date'].dt.strftime('%Y-%m-%d')
     for index in range(len(df)):
        date = df.iloc[index]['date']
        value = df.iloc[index]['value']
        cursor.execute(f"INSERT INTO {table_name} (date, value) VALUES (?, ?)", (date, value))
        conn.commit()
     conn.close()

#Insert Data into Database tables 
for name,serie in series_id.items():
    data=data_cleaning.fetch_and_clean_data(serie)
    conn=sqlite3.connect("economic_db")
    if data is not None:
            create_database(name.replace(" ","_"),database)
            insert_into_table(data, name.replace(" ", "_").lower())  # use indicator name as table name
            print("All data has been inserted into SQLite database.") 
    else:
        print("Error")



