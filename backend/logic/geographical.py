import math

from backend import db
from backend.logic import  db_queries

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LS': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

map_state_list = ["HI", "AK", "FL", "SC", "GA", "AL", "NC", "TN", "RI", "CT", "MA",
    "ME", "NH", "VT", "NY", "NJ", "PA", "DE", "MD", "WV", "KY", "OH",
    "MI", "WY", "MT", "ID", "WA", "DC", "TX", "CA", "AZ", "NV", "UT",
    "CO", "NM", "OR", "ND", "SD", "NE", "IA", "MS", "IN", "IL", "MN",
    "WI", "MO", "AR", "OK", "KS", "LS", "VA"]

def get_arrest_state_rank():
    rows = db.cursor.execute(db_queries.arrest_state_rank).fetchall()
    return [{"element": states[row[0]], "rank": row[1], "count": row[2]}for row in rows if states.get(row[0])]

def get_state_geographical_data():
    rows = db.cursor.execute(db_queries.arrest_state_rank).fetchall()
    # TODO:- convert crime count back to row[2]
    in_range_result = {}
    actual_count = {}
    # get min max values:
    max_count = min_count = rows[0][2]
    # added logic to get min and max to convert the range into 0,100
    for row in rows:
        if row[2] > max_count:
            max_count = row[2]
        if row[2] < min_count:
            min_count = row[2]

    new_high = 100
    new_low = 0

    for row in rows:
        if row[0] in map_state_list:
            # generating new value based on 0,100 range
            computed_value = ((row[2] - min_count) / (max_count - min_count)) * (new_high - new_low) + new_low
            in_range_result.update({row[0]: math.ceil(computed_value)})
            actual_count.update({row[0]: row[2]})

    return in_range_result, actual_count

def scale_value_in_range(max, min, value, new_range_max=100, new_range_min=0):
    pass