from sqlalchemy import create_engine
import pymysql
import pandas as pd
import os

# Define the database connection parameters
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'port': 3306,
    'db': 'pollution_db'
}

file_path = os.path.abspath('clean.csv')

# Create a connection to the MySQL server
mysql_conn = pymysql.connect(
    host=db_config['host'],
    user=db_config['user'],
    password=db_config['password'],
    port=db_config['port'],
    connect_timeout=60
)

# Create a cursor object
cursor = mysql_conn.cursor()

try:
    # Create the database
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_config['db']}")

    # Create the database connection
    engine = create_engine(f"mysql+pymysql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['db']}")
    conn = engine.connect()

    # Load data into a Pandas dataframe in chunks
    station_chunks = pd.read_csv(file_path, delimiter=',', usecols=['SiteID', 'Location', 'geo_point_2d'], chunksize=50000)
    for chunk in station_chunks:
        chunk.drop_duplicates('SiteID', keep='last', inplace=True)
        chunk.to_sql(name='stations', con=conn, if_exists='append', index=False)

    # Add primary key constraint
    conn.execute("ALTER TABLE `stations` ADD PRIMARY KEY (`SiteID`)")
    # Load the readings data into a Pandas dataframe in chunks
    drop_columns = ('Location', 'geo_point_2d')
    reading_chunks = pd.read_csv(file_path, delimiter=',', low_memory=False, chunksize=10000, usecols=lambda col: col not in drop_columns)
    for chunk in reading_chunks:
        chunk.to_sql(name='readings', con=conn, if_exists='append', index=False)

    # Add primary key constraint to readings table
    conn.execute("ALTER TABLE readings ADD PRIMARY KEY(idReadings)")

    # Load the schema data into a Pandas dataframe in chunks
    schema_chunks = pd.read_csv('schema.csv', delimiter=',', encoding='utf8', low_memory=False, chunksize=10000)
    for chunk in schema_chunks:
        chunk.index += 1
        chunk.to_sql(name='schema', con=conn, if_exists='append', index=True, index_label='idschema')

    # Add primary key constraint to schema table
    conn.execute("ALTER TABLE schema ADD PRIMARY KEY(idschema)")

except Exception as e:
    print(e)
finally:
    cursor.close()
    mysql_conn.close()