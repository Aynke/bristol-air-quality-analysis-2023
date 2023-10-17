from sqlalchemy import create_engine
import pandas as pd
import os

# Define the database connection parameters
host = 'localhost'
user = 'root'
password = ''
port = 3306
database = 'mydatabase'

# Create the database connection
engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")

file_path = os.path.abspath('clean.csv')

# Load data into a Pandas dataframe
stations_table = pd.read_csv(file_path, delimiter=',', usecols=['SiteID', 'Location', 'geo_point_2d'])
stations_table = stations_table.drop_duplicates('SiteID', keep='last')

# Load the readings data into a Pandas dataframe
readings = pd.read_csv(file_path, delimiter=',', low_memory=False)
readings['Date Time'] = pd.to_datetime(readings['Date Time'].str[:-6], format='%Y-%m-%d %H:%M:%S')
readings[['DateStart', 'DateEnd']] = pd.to_datetime(readings[['DateStart', 'DateEnd']], format='%Y-%m-%d %H:%M:%S')
readings.index += 1
