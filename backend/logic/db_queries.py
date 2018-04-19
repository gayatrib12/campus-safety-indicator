all_institute_names = "select distinct(name) from institute"

institute_crime_count = """select WEAPONS + DRUGS + LIQUOR, branch
                            from {crime_table}, (
                                select *
                                from institute
                                where name = '{inst_name}'
                            ) inst
                            where {crime_table}.instituteid = inst.id and year = {year}
                                and location = '{location}'"""

arrest_institute_rank = """select *
from (select name, rank() over (order by arrest_count desc), arrest_count
        from (select institute.NAME, SUM(weapons + drugs + liquor) as arrest_count
                from arrest,institute where arrest.INSTITUTEID = institute.ID
                group by institute.name
            )
    )
where rownum <= 50"""

arrest_state_rank = """select state, rank() over (order by arrest_count desc), arrest_count
        from (select institute.STATE, SUM(weapons + drugs + liquor) as arrest_count
                from arrest,institute where arrest.INSTITUTEID = institute.ID and state is not null
                group by institute.STATE
            )"""

