from backend import db
from backend.logic import  db_queries

def get_all_institute_names():
    institutes = []
    rows = db.cursor.execute(db_queries.all_institute_names).fetchall()
    # result is like list of tuples
    institutes = [i[0] for i in rows]
    print(f"total number of institutes: {len(institutes)}")
    institutes.sort()
    return institutes

def get_institute_names_like(query):
    institutes = []
    rows = db.cursor.execute(db_queries.institute_names_like.format(
        query = query
    )).fetchall()
    # result is like list of tuples
    institutes = [i[0] for i in rows]
    print(f"total number of institutes: {len(institutes)}")
    institutes.sort()
    return institutes

def get_different_crimes_count_per_campus(inst_name, year, location):
    crime_tables = ['arrest', 'disciplinary_action']#'vawa', 'criminal']
    result = []
    for table in crime_tables:
        print(db_queries.institute_crime_count.format(
                crime_table=table,
                inst_name=inst_name,
                year=year,
                location=location
            )
        )
        rows = db.cursor.execute(db_queries.institute_crime_count.format(
                crime_table=table,
                inst_name=inst_name,
                year=year,
                location=location
            )
        ).fetchall()
        branch_data = {}
        for row in rows:
            branch_data[row[1]] = row[0]
        result.append({"crime_table": table.title(), "crime_data": branch_data})
    return result
