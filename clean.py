import pandas as pd

# Load crop.csv into a dataframe
df = pd.read_csv('crop.csv', low_memory=False)
df.shape
# Select columns SiteID and Location from the dataframe
df_new = df.loc[:, ['SiteID', 'Location']]

# Define site_location dictionary
site_location = {
    188: 'AURN Bristol Centre',
    203: 'Brislington Depot',
    206: 'Rupert Street',
    209: 'IKEA M32',
    213: 'Old Market',
    215: 'Parson Street School',
    228: 'Temple Mead Station',
    270: 'Wells Road',
    271: 'Trailer Portway P&R',
    375: 'Newfoundland Road Police Station',
    395: "Shiner's Garage",
    452: 'AURN St Pauls',
    447: 'Bath Road',
    459: 'Cheltenham Road \ Station Road',
    463: 'Fishponds Road',
    481: 'CREATE Centre Roof',
    500: 'Temple Way',
    501: 'Colston Avenue',
    672: 'Marlborough Street'
}
print(df_new.shape)

# create new column called site_location
df_new['site_location'] = df_new.apply(lambda x: site_location.get(x['SiteID']), axis=1)
#df_new.dropna(subset=['site_location'], inplace=True)

# check for mismatches
for index, row in df_new.iterrows():
    if row['site_location'] != row['Location']:
        print(f"Mismatch detected for SiteID {row['SiteID']} and {row['Location']}. Row: {row.to_dict()}")

  
df_new_copy = df_new.copy()
for index, row in df_new.iterrows():
    siteID = row['SiteID']
    location = row['Location']
    if siteID in site_location and site_location[siteID] != location:
        df_new.at[index, 'Location'] = 0
        df.loc[index, 'Location'] = 0
df=df[df['Location'] != 0]
df.shape
df.to_csv('clean.csv', index= False)              
