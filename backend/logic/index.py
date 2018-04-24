import math

from backend import db
from backend.logic import  db_queries

def get_total_tuple_count():
    print(db_queries.total_tuple_count)
    rows = db.cursor.execute(db_queries.total_tuple_count).fetchall()
    count = str(rows[0][0])
    return parse_count(count)

def parse_count(count):
    digits = len(count)
    if digits <= 3:
        return count
    commas = math.floor(digits / 3)
    l = list(count)
    comma_positions = []
    for i in range(commas):
        digits -= 3
        comma_positions.append(digits)
    for i in comma_positions:
        l.insert(i, ',')
    return "".join(l)
