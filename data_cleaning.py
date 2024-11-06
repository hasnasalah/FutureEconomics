 
 # get data from FRED API 
 
import pandas as pd
import requests


# assign the api key 
fred_key='ecf39d17668932f2ba0bb24587a01919'

# Define the FRED API endpoint
base_url = 'https://api.stlouisfed.org/fred/'
# get the GDP 
# API endpoint for GDP data
obs_endpoint = 'series/observations'

 # assign parametres 
parameters={
    'series_id': 'GDP',  # Series ID for U.S. GDP
    'api_key': fred_key,
    'file_type': 'json',  # Data format
    'frequency': 'A',  # Frequency (A = Annual)
    'start_date': '1970-01-01',  # Start date
    'end_date': '2023-12-31'  # End date
}
#making a request to FRED API
response=requests.get(base_url+obs_endpoint,params=parameters)
# Checking if the request was successful
data = response.json()
# Creating DataFrame from JSON data
df = pd.DataFrame(data['observations'])
df['date'] = pd.to_datetime(df['date'])  # Converting to datetime
df['value'] = pd.to_numeric(df['value'])  # Ensuring values are numeric
# Displaying the first few rows of the data
print(df.head())

 