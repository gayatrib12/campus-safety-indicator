import pandas as pd

# 101112, 070809, 050607
years = ['131415']
# 'hate'
crime_types = ['arrest', 'discipline', 'crime', 'vawa']
# oncampus, publicproperty, reported, residencehall
locations = ['noncampus', 'oncampus', 'publicproperty', 'reported', 'residencehall']

columns = {
    'arrest': ['WEAPON', 'DRUG', 'LIQUOR'],
    'institute': ['UNITID_P', 'INSTNM', 'BRANCH', 'Address', 'City', 'State',
                  'ZIP', 'sector_cd', 'men_total', 'women_total', 'Total'],
    'discipline': ['WEAPON', 'DRUG', 'LIQUOR'],
    'crime': ['MURD', 'NEG_M', 'FORCIB', 'NONFOR', 'ROBBE', 'AGG_A', 'BURGLA', 'VEHIC', 'ARSON'],
    'vawa': ['DOMEST', 'DATING', 'STALK'],
}
output_columns = {
    'arrest': ['weapon', 'drug', 'liquor', 'institute_id', 'location', 'year'],
    'institute': ['id', 'name', 'branch', 'street_address', 'city', 'state',
                  'zip', 'sector_code', 'men_total', 'woman_total', 'total'],
    'discipline': ['weapon', 'drug', 'liquor', 'institute_id', 'location', 'year'],
    'crime': ['murder', 'negligent_manslaughter', 'forcible_sex', 'nonforcible_sex', 'robbery',
              'aggravated_assault', 'burglary', 'vehicle_theft', 'arson','institute_id',
              'location', 'year'],
    'vawa': ['domestic_violence', 'dating_violence', 'stalking', 'institute_id', 'location', 'year'],
}

def read_excel(filepath):
    return pd.read_excel(filepath)

def sum_up_values(df, crime_type, data_year):
    if crime_type == 'crime' and data_year in ['14', '15']:
        df[f'FORCIB{data_year}'] = df[f'RAPE{data_year}'] + df[f'FONDL{data_year}']
        df[f'NONFOR{data_year}'] = df[f'INCES{data_year}'] + df[f'STATR{data_year}']


def get_crime_table(df, data_year, crime_type, location):
    sum_up_values(df, crime_type, data_year)
    data_columns = [f"{i}{data_year}" for i in columns[crime_type]]
    data_columns.append('UNITID_P')
    table = df[data_columns]
    table['location'] = location
    table['year'] = int(f"20{data_year}")
    table.columns = output_columns[crime_type]
    return table

def get_institute_table(df):
    institute = df[columns['institute']]
    institute.columns = output_columns['institute']
    institute['zip'] = institute['zip'].str[:5]
    return institute

def main():
    institute_table = False
    for year in years:
        for crime_type in crime_types:
            crime_tables = []
            for location in locations:
                filepath = f"Crime2016EXCEL/{location}{crime_type}{year}.xls"
                print(f"reading file: {filepath}")
                try:
                    df = read_excel(filepath)
                except FileNotFoundError as e:
                    print('going for xlsx')
                    filepath = filepath + 'x'
                    df = read_excel(filepath)
                if institute_table:
                    print("creating institute data frame")
                    institute_table = get_institute_table(df)
                    institute_table.to_excel('Crime2016EXCEL/institute.xls', index=False)
                data_years = [year[0:2], year[2:4], year[4:6]]
                location_tables = []
                for data_year in data_years:
                    print(f"getting {crime_type} data for year: {data_year}")
                    location_tables.append(get_crime_table(df, data_year, crime_type, location))
                print("concatinating all the data frames")
                crime_tables.append(pd.concat(location_tables))
            crime_tables = pd.concat(crime_tables)
            crime_tables.to_csv(f'Crime2016EXCEL/{crime_type}{year}_clean.csv', index=False)
    print("finishing code")



if __name__ == '__main__':
    main()