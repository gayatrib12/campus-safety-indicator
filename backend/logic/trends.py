from backend import db
from backend.logic import db_queries


def get_generic_trends(cat, subcat, cond):
    print(db_queries.generic_year_group.format(
        sub_cat_type = subcat,
        cat_type = cat,
        filter_str = cond
        )
    )
    rows = db.cursor.execute(db_queries.generic_year_group.format(
        sub_cat_type = subcat,
        cat_type = cat,
        filter_str = cond
    )
    ).fetchall()
    return rows

def get_all_criminal_offences_trends(cond):
    print(db_queries.all_criminal_offences_year_group.format(
        filter_str=cond
    ))
    rows = db.cursor.execute(db_queries.all_criminal_offences_year_group.format(
        filter_str=cond
    )).fetchall()
    return rows

def get_all_hate_trends(cond):
    print(db_queries.all_hate_offences_year_group.format(
        filter_str=cond
    ))
    rows = db.cursor.execute(db_queries.all_hate_offences_year_group.format(
        filter_str=cond
    )).fetchall()
    return rows

def get_all_vawa_trends(cond):
    print(db_queries.all_vawa_offences_year_group.format(
        filter_str=cond
    ))
    rows = db.cursor.execute(db_queries.all_vawa_offences_year_group.format(
        filter_str=cond
    )).fetchall()
    return rows

def get_all_arrest_trends(cond):
    print(db_queries.all_criminal_offences_year_group.format(
        filter_str=cond
    ))
    rows = db.cursor.execute(db_queries.all_criminal_offences_year_group.format(
        filter_str=cond
    )).fetchall()
    return rows

def get_all_disciplinary_action_trends(cond):
    print(db_queries.all_da_year_group.format(
        filter_str=cond
    ))
    rows = db.cursor.execute(db_queries.all_da_year_group.format(
        filter_str=cond
    )).fetchall()
    return rows

def generateFilterString(filter_input, form_data):
    cond = ' where '
    if filter_input == '0':
        return ''

    elif filter_input == 'SECTOR':
        sectorlist = form_data.getlist(filter_input.lower())
        cond += "S.ID in ('"
        for item in sectorlist:
            cond += item+"','"
        cond = cond[:-2] + ") "
        return cond

    elif filter_input == 'LEVEL':
        levellist = form_data.getlist(filter_input.lower())
        sectorlist = []
        for item in levellist:
            sectorlist += item.split(",")
        cond += "S.ID in ('"
        for item in sectorlist:
            cond += item+"','"
        cond = cond[:-2] + ") "
        return cond

    elif filter_input == 'CONTROL':
        controllist = form_data.getlist(filter_input.lower())
        sectorlist = []
        for item in controllist:
            sectorlist += item.split(",")
        cond += "S.ID in ('"
        for item in sectorlist:
            cond += item+"','"
        cond = cond[:-2] + ") "
        return cond

    elif filter_input == 'LOCATION':
        sectorlist = form_data.getlist(filter_input.lower())
        cond += "C.LOCATION in ('"
        for item in sectorlist:
            cond += item+"','"
        cond = cond[:-2] + ") "
        return cond

    elif filter_input == 'STATE':
        if [form_data['state_input']][0] == 'ALL':
            return ''
        else:
            return cond + filter_input + " = '" + [form_data['state_input']][0]+"'"

    elif filter_input == 'INSTITUTE':
        if [form_data['institute_input']][0] == 'ALL':
            return ''
        else:
            return cond + "I.NAME" + " = '" + [form_data['institute_input']][0]+"'"

