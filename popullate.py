import pandas as pd
import numpy as np
import pymysql as pm

#saving the cleaned csv file into a dataframe
my_file = pd.read_csv('clean.csv', header = 0, low_memory=False)
print(my_file)

my_schema_file = pd.read_csv('schema.csv', header = 0, low_memory=False)
print(my_schema_file)
# I then went on to convert the columns which had dates to the have the right data type
my_file['Date Time'] = my_file['Date Time'].astype('datetime64[ns]')
my_file['DateStart'] = my_file['DateStart'].astype('datetime64[ns]')
my_file['DateEnd'] = my_file['DateEnd'].astype('datetime64[ns]')

#renaming columns with spaces in them
my_file = my_file.rename(columns={'Date Time': 'Datetime', 'Air Pressure': 'Airpressure',
'Instrument Type': 'Instrumenttype','NVPM2.5': 'NVPM25',
 'PM2.5': 'PM25','VPM2.5': 'VPM25'})

for col in my_file.columns:
    print('column', col,':', type(my_file[col][0]))

#replacing the nan values in my dataframe
my_file.fillna(0, inplace=True)
my_schema_file.fillna('NULL', inplace=True)


for row in my_file.head(n = 2).itertuples():
  print(row)

#creating a connection to mysql
mydb_connector = pm.connect(
  host="localhost",
  user="root",
  password=None
)

#creating the cursor
mycursor = mydb_connector.cursor()

#execute cursor to create database
mycursor.execute("CREATE DATABASE IF NOT EXISTS `pollutions-db2`")

mydb_connector.close()

#creating a connection to database
mydb_connector = pm.connect(
    host="localhost", 
    user="root", 
    password=None, 
    database="pollutions-db2"
)

mycursor = mydb_connector.cursor()

#create the table for stations
mycursor.execute("""CREATE TABLE IF NOT EXISTS `stations` (`stationId` INT NOT NULL, `location` VARCHAR(45) NOT NULL, 
`geo_point` VARCHAR(45) NOT NULL, PRIMARY KEY (`stationId`))""")

#create the table for readings
mycursor.execute("""CREATE TABLE IF NOT EXISTS `readings`(
  `readingID` INT NOT NULL AUTO_INCREMENT,
  `datetime` DATETIME,
  `temperature` REAL,
  `nox` FLOAT,
  `no2` FLOAT,
  `no` FLOAT,
  `pm10` FLOAT,
  `nvpm10` FLOAT,
  `vpm10` FLOAT,
  `nvpm2.5` FLOAT,
  `pm2.5` FLOAT,
  `vpm2.5` FLOAT,
  `o3` FLOAT,
  `co` FLOAT,
  `so2` FLOAT,
  `airpressure` FLOAT,
  `datestart` DATETIME,
  `dateend` DATETIME,
  `rh` INT NOT NULL,
  `current` TEXT(10) NOT NULL,
  `instrumenttype` VARCHAR(45),
  `stationId-fk` INT NOT NULL, 
  PRIMARY KEY (`readingID`))
  """)

#create the table for readings
mycursor.execute("""CREATE TABLE IF NOT EXISTS `schema`(
  `measure` VARCHAR(64) NOT NULL,
  `description` VARCHAR(64) NOT NULL,
  `unit` VARCHAR(32) NOT NULL,
  PRIMARY KEY (`measure`))""")

#insert into schema table from csv
for row in my_schema_file.itertuples():
    mycursor.execute("INSERT IGNORE INTO `schema`(`measure`,`description`,`unit` ) values(%s, %s, %s)", 
    (row.measure, row.description, row.unit))

    mydb_connector.commit()

#insert into station table from csv
for row in my_file.itertuples():
    mycursor.execute("INSERT IGNORE INTO `stations`(`location`,`geo_point`,`stationId`) values(%s, %s, %s)", (row.Location, row.geo_point_2d, row.SiteID))

    mydb_connector.commit()


#insert into readings table from csv
for row in my_file.itertuples():
  
  sql = """INSERT INTO `readings`(`datetime`,`temperature`,`nox`,`no2`,`no`,`pm10`,`nvpm10`,`vpm10`,
  `nvpm2.5`,`pm2.5`,`vpm2.5`,`o3`,`co`,`so2`,`airpressure`,`datestart`,`dateend`,`rh`,`current`,
  `instrumenttype`,`stationId-fk`) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""" 

  val = (row.Datetime, row.Temperature, row.NOx, row.NO2, row.NO, row.PM10, row.NVPM10, row.VPM10, row.NVPM25, 
  row.PM25, row.VPM25, row.O3, row.CO, row.SO2, row.Airpressure, row.DateStart, row.DateEnd, row.RH,
  row.Current, row.Instrumenttype, row.SiteID)

  mycursor.execute(sql,val)
  mydb_connector.commit()

