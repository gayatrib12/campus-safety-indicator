from backend import db
from backend.logic import  db_queries

def get_all_institute_names():
    institutes = []
    rows = db.cursor.execute(db_queries.all_institute_names).fetchall()
    print ('hello')

    # result is like list of tuples
    institutes = [i[0] for i in rows]

    print ('hii')
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

        rows = db.cursor.execute(db_queries.institute_crime_count.format(
                crime_table=table,
                inst_name=inst_name,
                year=year,
                location=location
            )
        ).fetchall()
        branch_data = {}
        for row in rows:
            #print(row)
            #print(row[1])
            branch_data[row[1]] = row[0]
        result.append({"crime_table": table.title(), "crime_data": branch_data})
    return result

def get_campus_crimes(inst_name, year, location):
    crime_tables = ['arrest', 'disciplinary_action']#'vawa', 'criminal']
    resultSet = []
    crime_data = {}


    if location == '--':
        if year == '--':
            #criminal
            rows = db.cursor.execute(db_queries.institute_wise_crimes_criminal_all.format(
                inst_name=inst_name,
                year=year,
                location=location)).fetchall()

            resultSet.append(rows)

            #vawa
            rows = db.cursor.execute(db_queries.institute_wise_crimes_vawa_all.format(
                inst_name=inst_name,
                year=year,
                location=location)).fetchall()

            resultSet.append(rows)

            #hate
            rows = db.cursor.execute(db_queries.institute_wise_crimes_hate_all.format(
                inst_name=inst_name,
                year=year,
                location=location)).fetchall()

            resultSet.append(rows)

        else:
            #criminal
            rows = db.cursor.execute(db_queries.institute_wise_crimes_criminal_noLoc.format(
                inst_name=inst_name,
                year=year,
                location=location)).fetchall()

            resultSet.append(rows)

            #vawa
            rows = db.cursor.execute(db_queries.institute_wise_crimes_vawa_noLoc.format(
                inst_name=inst_name,
                year=year,
                location=location)).fetchall()

            resultSet.append(rows)

            #hate
            rows = db.cursor.execute(db_queries.institute_wise_crimes_hate_noLoc.format(
                inst_name=inst_name,
                year=year,
                location=location)).fetchall()

            resultSet.append(rows)

    elif(year == '--'):
        if(location == '--'):
            #criminal
            rows = db.cursor.execute(db_queries.institute_wise_crimes_criminal_all.format(
                inst_name=inst_name,
                year=year,
                location=location)).fetchall()

            resultSet.append(rows)

            #vawa
            rows = db.cursor.execute(db_queries.institute_wise_crimes_vawa_all.format(
                inst_name=inst_name,
                year=year,
                location=location)).fetchall()

            resultSet.append(rows)

            #hate
            rows = db.cursor.execute(db_queries.institute_wise_crimes_hate_all.format(
                inst_name=inst_name,
                year=year,
                location=location)).fetchall()

            resultSet.append(rows)
        else:
            #criminal
            rows = db.cursor.execute(db_queries.institute_wise_crimes_criminal_noYear.format(
                inst_name=inst_name,
                year=year,
                location=location)).fetchall()

            resultSet.append(rows)

            #vawa
            rows = db.cursor.execute(db_queries.institute_wise_crimes_vawa_noYear.format(
                inst_name=inst_name,
                year=year,
                location=location)).fetchall()

            resultSet.append(rows)

            #hate
            rows = db.cursor.execute(db_queries.institute_wise_crimes_hate_noYear.format(
                inst_name=inst_name,
                year=year,
                location=location)).fetchall()

            resultSet.append(rows)

    elif(year == '--' and location == '--'):
        #criminal
        rows = db.cursor.execute(db_queries.institute_wise_crimes_criminal_all.format(
            inst_name=inst_name,
            year=year,
            location=location)).fetchall()

        resultSet.append(rows)

        #vawa
        rows = db.cursor.execute(db_queries.institute_wise_crimes_vawa_all.format(
            inst_name=inst_name,
            year=year,
            location=location)).fetchall()

        resultSet.append(rows)

        #hate
        rows = db.cursor.execute(db_queries.institute_wise_crimes_hate_all.format(
            inst_name=inst_name,
            year=year,
            location=location)).fetchall()

        resultSet.append(rows)

    else:
        #criminal
        rows = db.cursor.execute(db_queries.institute_wise_crimes_criminal.format(
            inst_name=inst_name,
            year=year,
            location=location)).fetchall()

        resultSet.append(rows)

        #vawa
        rows = db.cursor.execute(db_queries.institute_wise_crimes_vawa.format(
            inst_name=inst_name,
            year=year,
            location=location)).fetchall()

        resultSet.append(rows)

        #hate
        rows = db.cursor.execute(db_queries.institute_wise_crimes_hate.format(
            inst_name=inst_name,
            year=year,
            location=location)).fetchall()

        resultSet.append(rows)


#------------- arrests/disciplinary action section -----------------
    for table in crime_tables:
        if (location == '--'):
            if (year == '--'):
                #arrests/disc
                rows = db.cursor.execute(db_queries.institute_wise_crimes_arrest_all.format(
                    inst_name=inst_name,
                    year=year,
                    crime_table=table,
                    location=location)).fetchall()

                resultSet.append(rows)
            else:
                #arrests/disc
                rows = db.cursor.execute(db_queries.institute_wise_crimes_arrest_noLoc.format(
                    inst_name=inst_name,
                    year=year,
                    crime_table=table,
                    location=location)).fetchall()

            resultSet.append(rows)

        elif(year == '--'):
            if(location == '--'):
                #arrests/disc
                rows = db.cursor.execute(db_queries.institute_wise_crimes_arrest_all.format(
                inst_name=inst_name,
                year=year,
                crime_table=table,
                location=location)).fetchall()

                resultSet.append(rows)

            else:
                #arrests/disc
                rows = db.cursor.execute(db_queries.institute_wise_crimes_arrest_noYear.format(
                inst_name=inst_name,
                year=year,
                crime_table=table,
                location=location)).fetchall()

                resultSet.append(rows)

        elif(year == '--' and location == '--'):
            #arrests/disc
            rows = db.cursor.execute(db_queries.institute_wise_crimes_arrest_all.format(
                inst_name=inst_name,
                year=year,
                crime_table=table,
                location=location)).fetchall()

            resultSet.append(rows)

        else:
            #arrests/disc
            rows = db.cursor.execute(db_queries.institute_wise_crimes_arrest.format(
                inst_name=inst_name,
                year=year,
                crime_table=table,
                location=location)).fetchall()

            resultSet.append(rows)


    #print(row[1])
    #crime_data[row[1]] = row[0]
    #resultSet.append({"crime_table": table.title(), "crime_data": crime_data})
    print('in resultSet')
    print(resultSet)

    return resultSet
