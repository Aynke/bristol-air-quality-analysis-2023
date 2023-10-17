import pandas as pd
import os

try:
    print(os.getcwd())

    df = pd.read_csv('air-quality-data-2003-2022.csv', delimiter=';', parse_dates=['Date Time'], low_memory=False)
    df.info()
    
    # Drop rows with Date Time before 2010-01-01
    df.drop(df[df['Date Time'] < '2010-01-01T00:00:00.00'].index, inplace=True)

    # Drop rows with missing Date Time values
    df.drop(df[df['Date Time'].isnull()].index, inplace=True)
    df.shape

    # Save the cropped data as a csv file
    df.to_csv('crop.csv', index=False)
except Exception as e:
    print('An error occurred:', e)
