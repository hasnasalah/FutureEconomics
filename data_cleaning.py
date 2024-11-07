import pandas as pd
import requests
import sqlite3

# Assign the API key
fred_key = 'ecf39d17668932f2ba0bb24587a01919'

# Define the FRED API endpoint
base_url = 'https://api.stlouisfed.org/fred/series/observations'
series_id={
    'gdp':'GDP',
    'iflation rate':'CPIAUCSL',
    'unemployment rate':'UNRATE',
    'governement spending':'FGEXPND'
}

# Method to get data for any series (e.g., GDP or Unemployment Rate)
def fetch_and_clean_data(series_id):
    parameters = {
        'series_id': series_id,  # Use the actual series_id passed to the function
        'api_key': fred_key,
        'file_type': 'json',  # Data format
        'frequency': 'a',  # Frequency (a = Annual)
        'start_date': '1970-01-01',
        'end_date': '2023-12-31'
    }
    # Making a request to FRED API
    response = requests.get(base_url, params=parameters)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        # Check if 'observations' is in the response data
        if 'observations' in data:
            # Creating DataFrame from JSON data
            df = pd.DataFrame(data['observations'])
            df['date'] = pd.to_datetime(df['date'])  # Converting to datetime
            df['value'] = pd.to_numeric(df['value'], errors='coerce')  # Ensuring values are numeric
            df = df.drop(columns=['realtime_start', 'realtime_end'])  # Dropping irrelevant columns
            
            return df
        else:
            print(f"Error: No 'observations' found in the API response for {series_id}.")
            return None
    else:
        print("Error: Unable to fetch data for",series_id,"Status code:", response.status_code)
        return None
def fetch_data(serie):
    for s in serie:
        data=fetch_and_clean_data(s)
    return data
    
#Fetching data for GDP
gdp_series_id = 'GDP'  # GDP series ID
gdp_df = fetch_and_clean_data(gdp_series_id)

#Fetching data for Inflation Rate
inflation_series_id = 'CPIAUCSL'  # Inflation Rate series ID
inflation_df = fetch_and_clean_data(inflation_series_id)

#Fetching data for Governement Spending Rate
gs_series_id = 'GFDEBTN'  # Governement Spending series ID
gs_df = fetch_and_clean_data(inflation_series_id)

#Fetching data for unemployment Rate
unemployment_series_id = 'UNRATE'  # Unemployment Rate series ID
unemployment_df = fetch_and_clean_data(unemployment_series_id)

# Displaying the first few rows of the cleaned data if available
if gdp_df is not None:
    print("GDP Data:")
    print(gdp_df.head())

if inflation_df is not None:
    print("Inflation Rate Data:")
    print(inflation_df.head())
if gs_df is not None:
    print("Governement Spending Data:")
    print(gs_df.head())

if unemployment_df is not None:
    print("Unemployment Rate Data:")
    print(unemployment_df.head())