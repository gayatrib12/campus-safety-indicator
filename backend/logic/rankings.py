from backend import db
from backend.logic import  db_queries

def get_arrest_institute_ranks_for_year():
    #print(f"query: {db_queries.arrest_institute_rank.format(year=year)}")
    rows = db.cursor.execute(db_queries.arrest_institute_rank).fetchall()
    return [{"element": row[0], "rank": row[1], "count": row[2]}for row in rows]
