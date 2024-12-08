import pandas as pd
import requests
import sqlite3
import numpy as np
import os
from dotenv import find_dotenv, load_dotenv

path=find_dotenv("Key.env")
load_dotenv(path)
fred_key=os.getenv('fred_key')
base_url=os.getenv('base_url')
series_id={
    'gdp':'GDP',
    'inflation':'CPIAUCSL',
    'unemployment':'UNRATE',
    'governement_spending':'FGEXPND'
}

# Method to get data for series (Inflation, GDP, GDP, Governement spending and Unemployment Rate)
def fetch_and_clean_data(series_id):
    parameters = {
        'series_id': series_id,  # Use the actual series_id passed to the function
        'api_key': fred_key,
        'file_type': 'json',  # Data format
        'frequency': 'a',  # Frequency (a = Annual)
        'start_date': '1970-01-01',
        'end_date': '2023-12-31'
    }
    # Get a request to FRED API
    response = requests.get(base_url, params=parameters)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        # Check if 'observations' is in the response data
        if 'observations' in data:
            # Creating DataFrame from JSON data
            df = pd.DataFrame(data['observations'])
            df['date'] = pd.to_datetime(df['date'])  # Converting to datetime
            df['value'] = pd.to_numeric(df['value'], errors='coerce')  # Convert values to numeric
            df = df.drop(columns=['realtime_start', 'realtime_end'])  # Drop unneeded data
            
            return df
        else:
            print("Error: No 'observations' found in the API response for ",series_id,".")
            return None
    else:
        print("Error: Unable to fetch data for",series_id,"Status code:", response.status_code)
        return None

def get_interest_rate():
    # Load the CSV file and skip metadata rows
    interest_rate = pd.read_csv("API_FR.INR.RINR_DS2_en_csv_v2_119/API_FR.INR.RINR_DS2_en_csv_v2_119.csv", skiprows=4)
    
    # Transform the DataFrame into long format
    df_filtered = interest_rate.melt(id_vars=['Country Name'], var_name='Year', value_name='Interest Rate')
    
    # Convert 'Year' to numeric, replacing non-numeric and missing values
    df_filtered['Year'] = pd.to_numeric(df_filtered['Year'], errors='coerce')
    df_filtered['Interest Rate'] = pd.to_numeric(df_filtered['Interest Rate'], errors='coerce')
    
    # Replace invalid values with NaN
    df_filtered.replace(to_replace=['-INF', 'INF', 'NA'], value=np.nan, inplace=True)
    
    # Drop rows with NaN values
    df_filtered.dropna(inplace=True)
  

    
    # Filter for the last 20 years
    df_filtered = df_filtered[df_filtered['Year']>2002]

    return df_filtered

    
def main():
    #print Data to test if fetched correctly
    # print(get_interest_rate().head())
    g=get_interest_rate()
    print(g[['Year', 'Interest Rate']].drop_duplicates())
    for name,serie in series_id.items():
        data=fetch_and_clean_data(serie)
        if data is not None:
          print(name, "data:")
        #   print(data.head())
        else:
            print("data is none")
if __name__=="__main__":
    main()
    
        