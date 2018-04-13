import pandas as pd

# 101112, 070809, 050607
years = ['131415']
# 'hate'
crime_types = ['hate']#['arrest', 'discipline', 'crime', 'vawa']
# oncampus, publicproperty, reported, residencehall
locations = ['noncampus', 'oncampus', 'publicproperty', 'reported', 'residencehall']
# biases
bias_input = ["RAC", "REL", "SEX", "GEN", "DIS", "ETH"]
bias_output = {
    "RAC": "race",
    "REL": "religion",
    "SEX": "sexual_orientation",
    "GEN": "gender",
    "DIS": "disability",
    "ETH": "ethnicity"
}

columns = {
    'arrest': ['WEAPON', 'DRUG', 'LIQUOR'],
    'institute': ['UNITID_P', 'INSTNM', 'BRANCH', 'Address', 'City', 'State',
                  'ZIP', 'sector_cd', 'men_total', 'women_total', 'Total'],
    'discipline': ['WEAPON', 'DRUG', 'LIQUOR'],
    'crime': ['MURD', 'NEG_M', 'FORCIB', 'NONFOR', 'ROBBE', 'AGG_A', 'BURGLA', 'VEHIC', 'ARSON'],
    'vawa': ['DOMEST', 'DATING', 'STALK'],
    'hate': ['MURD', 'FORCIB', 'NONFOR', 'ROBBE', 'AGG_A', 'BURGLA',
             'VEHIC', 'ARSON', 'SIM_A', 'LAR_T', 'INTIM', 'VANDAL']
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
    'hate': ['murder', 'forcible_sex', 'nonforcible_sex', 'robbery',
             'aggravated_assault', 'burglary', 'vehicle_theft', 'arson', 'simple_assault',
             'larceny', 'intimidation', 'vandalism', 'institute_id',
             'location', 'year', 'biased_by']
}

def read_excel(filepath):
    return pd.read_excel(filepath)

def sum_up_values(df, crime_type, data_year, biased_by=""):
    if crime_type == 'crime' and data_year in ['14', '15']:
        df[f'FORCIB{data_year}'] = df[f'RAPE{data_year}'] + df[f'FONDL{data_year}']
        df[f'NONFOR{data_year}'] = df[f'INCES{data_year}'] + df[f'STATR{data_year}']
    elif crime_type == 'hate' and data_year in ['14', '15']:
        if biased_by in ['GEN', 'ETH']:
            bias = 'ET' if biased_by == 'ETH' else 'GEN'
            additional_field = "GID" if biased_by == "GEN" else  "NAT"
            df[f'FORCIB_{bias}{data_year}'] = (df[f'RAPE_{bias}{data_year}']
                                                    + df[f'FOND_{bias}{data_year}']
                                                    + df[f'RAPE_{additional_field}{data_year}']
                                                    + df[f'FOND_{additional_field}{data_year}'])
            df[f'NONFOR_{bias}{data_year}'] = (df[f'INCE_{bias}{data_year}']
                                                    + df[f'STAT_{bias}{data_year}']
                                                    + df[f'INCE_{additional_field}{data_year}']
                                                    +df[f'STAT_{additional_field}{data_year}'])

        else:
            df[f'FORCIB_{biased_by}{data_year}'] = (df[f'RAPE_{biased_by}{data_year}']
                                                    + df[f'FOND_{biased_by}{data_year}'])
            df[f'NONFOR_{biased_by}{data_year}'] = (df[f'INCE_{biased_by}{data_year}']
                                                    + df[f'STAT_{biased_by}{data_year}'])


def get_crime_table(df, data_year, crime_type, location):
    sum_up_values(df, crime_type, data_year)
    data_columns = [f"{i}{data_year}" for i in columns[crime_type]]
    data_columns.append('UNITID_P')
    table = df[data_columns]
    table['location'] = location
    table['year'] = int(f"20{data_year}")
    table.columns = output_columns[crime_type]
    return table

def get_hate_table(df, data_year, crime_type, location):
    result = []
    for bias in bias_input:
        sum_up_values(df, crime_type, data_year, biased_by=bias)
        #print(f"columns after sum up{df.columns}")
        if data_year in ['14', '15'] and bias == 'ETH':
            bias = "ET"
        data_columns = [f"{i}_{bias}{data_year}" for i in columns[crime_type]]
        data_columns.append('UNITID_P')
        table = df[data_columns]
        table['location'] = location
        table['year'] = int(f"20{data_year}")
        bias = bias if bias != "ET" else "ETH"
        table['biased_by'] = bias_output[bias]
        table.columns = output_columns[crime_type]
        result.append(table)
    return pd.concat(result)

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
                filepath = f"/home/akku/Documents/dbms/project data/Crime2016EXCEL/{location}{crime_type}{year}.xls"
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
                    if crime_type == 'hate':
                        location_tables.append(get_hate_table(df, data_year, crime_type, location))
                    else:
                        location_tables.append(get_crime_table(df, data_year, crime_type, location))
                print("concatinating all the data frames")
                crime_tables.append(pd.concat(location_tables))
            crime_tables = pd.concat(crime_tables)
            crime_tables.to_csv(f'/home/akku/Documents/dbms/project data/Crime2016EXCEL/{crime_type}{year}_clean.csv', index=False)
    print("finishing code")



if __name__ == '__main__':
    main()