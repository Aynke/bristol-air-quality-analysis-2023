import pandas as pd

# Define the input and output files.
file_path = 'clean.csv'
result = 'insert-100.sql'

# Define the columns to read in from the CSV file and their data types.
csv_columns = [
    'Date Time', 'NOx', 'NO2', 'NO', 'SiteID', 'PM10', 'NVPM10', 'VPM10',
    'NVPM2.5', 'PM2.5', 'VPM2.5', 'CO', 'O3', 'SO2', 'Temperature', 'RH',
    'Air Pressure', 'Location', 'geo_point_2d', 'DateStart', 'DateEnd',
    'Current', 'Instrument Type'
]
data_types = {
    'Date Time': 'str',
    'NOx': 'float',
    'NO2': 'float',
    'NO': 'float',
    'SiteID': 'int',
    'PM10': 'float',
    'NVPM10': 'float',
    'VPM10': 'float',
    'NVPM2.5': 'float',
    'PM2.5': 'float',
    'VPM2.5': 'float',
    'CO': 'float',
    'O3': 'float',
    'SO2': 'float',
    'Temperature': 'float',
    'RH': 'float',
    'Air Pressure': 'float',
    'Location': 'str',
    'geo_point_2d': 'str',
    'DateStart': 'str',
    'DateEnd': 'str',
    'Current': 'int',
    'Instrument Type': 'str'
}

# Set the number of rows to read in to 100.
num_rows = 100

# Read in the CSV file.
df = pd.read_csv(input_file, usecols=csv_columns, dtype=data_types, nrows=num_rows)

# Convert the 'Date Time' column to a datetime data type.
df['Date Time'] = pd.to_datetime(df['Date Time'])

# Generate SQL insert statements for the data.
sql = ''
for index, row in df.iterrows():
    sql += "INSERT INTO your_table_name (Date_Time, NOx, NO2, NO, SiteID, PM10, NVPM10, VPM10, NVPM2.5, PM2.5, VPM2.5, CO, O3, SO2, Temperature, RH, Air_Pressure, Location, geo_point_2d, DateStart, DateEnd, Current, Instrument_Type) VALUES ('{}', {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, '{}', '{}', '{}', '{}', {}, '{}');\n".format(row['Date Time'], row['NOx'], row['NO2'], row['NO'], row['SiteID'], row['PM10'], row['NVPM10'], row['VPM10'], row['NVPM2.5'], row['PM2.5'], row['VPM2.5'], row['CO'], row['O3'], row['SO2'], row['Temperature'], row['RH'], row['Air Pressure'], row['Location'], row['geo_point_2d'], row['DateStart'], row['DateEnd'], row['Current'], row['Instrument Type'])

# Write the SQL insert statements to the output file.
with open(results, 'w') as f:
    writer = csv.writer(f, delimiter=' ')
    for index, row in df.iterrows():
        values = list(row)
        values[0] = str(values[0])
        values[0] = values[0].replace(' ', 'T')
        values[0] = values[0] + 'Z'
        sql = f"INSERT INTO air_quality_data VALUES ('{values[0]}', {values[1]}, {values[2]}, {values[3]}, {values[4]}, {values[5]}, {values[6]}, {values[7]}, {values[8]}, {values[9]}, {values[10]}, {values[11]}, {values[12]}, {values[13]}, {values[14]}, {values[15]}, {values[16]}, '{values[17]}', '{values[18]}', '{values[19]}', '{values[20]}', {values[21]}, '{values[22]}');"
        writer.writerow([sql])

# Convert the 'Date Time' column to a datetime data type.
df['Date Time'] = pd.to_datetime(df['Date Time'])

# Generate SQL insert statements for the data.
with open(file_path) as f:
    reader = csv.DictReader(f, fieldnames=['Date Time', 'NOx', 'NO2', 'NO', 'SiteID', 'PM10', 'NVPM10', 'VPM10', 'NVPM2.5', 'PM2.5', 'VPM2.5', 'CO', 'O3', 'SO2', 'Temperature', 'RH', 'Air Pressure', 'Location', 'geo_point_2d', 'DateStart', 'DateEnd', 'Current', 'Instrument Type'])
    next(reader) # Skip the header row
    rows = [row for row in reader][:n_rows]
with open(result, 'w') as f:
    f.write(sql)




