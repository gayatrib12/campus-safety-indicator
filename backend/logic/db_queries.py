all_institute_names = "select distinct(name) from institute"

institute_names_like = "select distinct(name) from institute where lower(name) like '%' || lower('{query}') || '%'"

institute_crime_count = """select WEAPONS + DRUGS + LIQUOR, branch
                            from {crime_table}, (
                                select *
                                from institute
                                where name = '{inst_name}'
                            ) inst
                            where {crime_table}.instituteid = inst.id      
                            """

# ------------- arrests section ---------------------

institute_wise_crimes_arrest = """
select sum(a.WEAPONS) as sum_weapons, sum(a.DRUGS) as sum_drugs, sum(a.LIQUOR) as sum_liquor from INSTITUTE i
inner join {crime_table} a on i.ID = a.instituteid
where i.NAME = '{inst_name}' and a.LOCATION = '{location}' and a.YEAR = {year}
"""

institute_wise_crimes_arrest_all = """
select sum(a.DRUGS) as sum_drugs, sum(a.WEAPONS) as sum_weapons, sum(a.LIQUOR) as sum_liquor from INSTITUTE i
inner join {crime_table} a on i.id = a.instituteid
where i.name = '{inst_name}'
"""

institute_wise_crimes_arrest_noLoc = """
select sum(a.DRUGS) as sum_drugs, sum(a.WEAPONS) as sum_weapons, sum(a.LIQUOR) as sum_liquor from INSTITUTE i
inner join {crime_table} a on i.id = a.instituteid
where i.name = '{inst_name}' and a.year = {year}
"""

institute_wise_crimes_arrest_noYear = """
select sum(a.DRUGS) as sum_drugs, sum(a.WEAPONS) as sum_weapons, sum(a.LIQUOR) as sum_liquor from INSTITUTE i
inner join {crime_table} a on i.id = a.instituteid
where i.name = '{inst_name}' and a.location = '{location}'
"""

# ------------- vawa section ---------------------
institute_wise_crimes_vawa = """
select Coalesce(sum(a.DOMESTIC_VIOLENCE),0) as DOMESTIC_VIOLENCE, Coalesce(sum(a.DATING_VIOLENCE),0) as DATING_VIOLENCE, Coalesce(sum(a.STALKING),0) as STALKING from vawa a
inner join institute i on i.id = a.instituteid
where a.Location = '{location}' and i.name = '{inst_name}' and a.year = {year}
"""

institute_wise_crimes_vawa_all = """
select sum(a.DOMESTIC_VIOLENCE) as DOMESTIC_VIOLENCE, sum(a.DATING_VIOLENCE) as DATING_VIOLENCE, sum(a.STALKING) as STALKING from vawa a
inner join institute i on i.id = a.instituteid
where i.name = '{inst_name}'
"""

institute_wise_crimes_vawa_noLoc = """
select sum(a.DOMESTIC_VIOLENCE) as sum_domestic, sum(a.DATING_VIOLENCE) as sum_dating, sum(a.STALKING) as sum_stalking from vawa a
inner join institute i on i.id = a.instituteid
where i.name = '{inst_name}' and a.year = {year}
"""

institute_wise_crimes_vawa_noYear = """
select sum(a.DOMESTIC_VIOLENCE) as sum_domestic, sum(a.DATING_VIOLENCE) as sum_dating, sum(a.STALKING) as sum_stalking from vawa a
inner join institute i on i.id = a.instituteid
where i.name = '{inst_name}' and a.Location = '{location}'
"""

# ------------- hate section ---------------------

institute_wise_crimes_hate = """
select sum(a.MURDER) as sum_murder, sum(a.FORCIBLE_SEX) as sum_forcible_sex, sum(a.NONFORCIBLE_SEX) as sum_nonforcible_sex, 
sum(a.ROBBERY) as sum_robbery, sum(a.AGGRAVATED_ASSAULTS) as sum_aggravated_assault,
sum(a.BURGLARY) as sum_burglary, sum(a.MOTOR_VEHICLE_THEFT) as sum_motor_vehicle_theft,
sum(a.ARSON) as sum_arson, sum(a.VANDALISM) as sum_vandalism, sum(a.INTIMIDATION) as sum_intimidation, 
sum(a.SIMPLE_ASSAULT) as sum_simple_assault, sum(a.LARCENY) as sum_larceny from hate a
inner join institute i on i.id = a.instituteid
where i.name = '{inst_name}'
and a.YEAR = {year} and a.LOCATION = '{location}'
"""

institute_wise_crimes_hate_all = """
select sum(a.MURDER) as sum_murder, sum(a.FORCIBLE_SEX) as sum_forcible_sex, sum(a.NONFORCIBLE_SEX) as sum_nonforcible_sex, 
sum(a.ROBBERY) as sum_robbery, sum(a.AGGRAVATED_ASSAULTS) as sum_aggravated_assault,
sum(a.BURGLARY) as sum_burglary, sum(a.MOTOR_VEHICLE_THEFT) as sum_motor_vehicle_theft,
sum(a.ARSON) as sum_arson, sum(a.VANDALISM) as sum_vandalism, sum(a.INTIMIDATION) as sum_intimidation, 
sum(a.SIMPLE_ASSAULT) as sum_simple_assault, sum(a.LARCENY) as sum_larceny from hate a
inner join institute i on i.id = a.instituteid
where i.name = '{inst_name}'
"""

institute_wise_crimes_hate_noLoc = """
select sum(a.MURDER) as sum_murder, sum(a.FORCIBLE_SEX) as sum_forcible_sex, sum(a.NONFORCIBLE_SEX) as sum_nonforcible_sex, 
sum(a.ROBBERY) as sum_robbery, sum(a.AGGRAVATED_ASSAULTS) as sum_aggravated_assault,
sum(a.BURGLARY) as sum_burglary, sum(a.MOTOR_VEHICLE_THEFT) as sum_motor_vehicle_theft,
sum(a.ARSON) as sum_arson, sum(a.VANDALISM) as sum_vandalism, sum(a.INTIMIDATION) as sum_intimidation, 
sum(a.SIMPLE_ASSAULT) as sum_simple_assault, sum(a.LARCENY) as sum_larceny from hate a
inner join institute i on i.id = a.instituteid
where i.name = '{inst_name}' and a.year = {year}
"""

institute_wise_crimes_hate_noYear = """
select sum(a.MURDER) as sum_murder, sum(a.FORCIBLE_SEX) as sum_forcible_sex, sum(a.NONFORCIBLE_SEX) as sum_nonforcible_sex, 
sum(a.ROBBERY) as sum_robbery, sum(a.AGGRAVATED_ASSAULTS) as sum_aggravated_assault,
sum(a.BURGLARY) as sum_burglary, sum(a.MOTOR_VEHICLE_THEFT) as sum_motor_vehicle_theft,
sum(a.ARSON) as sum_arson, sum(a.VANDALISM) as sum_vandalism, sum(a.INTIMIDATION) as sum_intimidation, 
sum(a.SIMPLE_ASSAULT) as sum_simple_assault, sum(a.LARCENY) as sum_larceny from hate a
inner join institute i on i.id = a.instituteid
where i.name = '{inst_name}' and a.location = '{location}'
"""

# ------------- criminal section ---------------------
institute_wise_crimes_criminal = """
select sum(a.MURDER) as MURDER, sum(a.NEGLIGENT_MANSLAUGHTER) as NEGLIGENT_MANSLAUGHTER, sum(a.FORCIBLE_SEX) as FORCIBLE_SEX, sum(a.NONFORCIBLE_SEX) as NONFORCIBLE_SEX, 
sum(a.ROBBERY) as ROBBERY, sum(a.AGGRAVATED_ASSAULTS) as AGGRAVATED_ASSAULTS,
sum(a.BURGLARY) as BURGLARY, sum(a.MOTOR_VEHICLE_THEFT) as MOTOR_VEHICLE_THEFT, sum(a.ARSON) as ARSON from criminal a
inner join institute i on i.id = a.instituteid
where i.name = '{inst_name}'
and a.year = {year} and a.location = '{location}'
"""

institute_wise_crimes_criminal_all = """
select sum(a.MURDER) as sum_murder, sum(a.NEGLIGENT_MANSLAUGHTER) as sum_negligent_manslaughter, 
sum(a.FORCIBLE_SEX) as sum_forcible_sex,  sum(a.NONFORCIBLE_SEX) as sum_nonforcible_sex, 
sum(a.ROBBERY) as sum_robbery, sum(a.AGGRAVATED_ASSAULTS) as sum_aggravated_assault,
sum(a.BURGLARY) as sum_burglary, sum(a.MOTOR_VEHICLE_THEFT) as sum_motor_vehicle_theft,
sum(a.ARSON) as sum_arson
from criminal a
inner join institute i on i.id = a.instituteid
where i.name = '{inst_name}'"""

institute_wise_crimes_criminal_noYear = """
select sum(a.MURDER) as sum_murder, sum(a.NEGLIGENT_MANSLAUGHTER) as sum_negligent_manslaughter, 
sum(a.FORCIBLE_SEX) as sum_forcible_sex,  sum(a.NONFORCIBLE_SEX) as sum_nonforcible_sex, 
sum(a.ROBBERY) as sum_robbery, sum(a.AGGRAVATED_ASSAULTS) as sum_aggravated_assault,
sum(a.BURGLARY) as sum_burglary, sum(a.MOTOR_VEHICLE_THEFT) as sum_motor_vehicle_theft,
sum(a.ARSON) as sum_arson
from criminal a
inner join institute i on i.id = a.instituteid
where i.name = '{inst_name}' and a.location = '{location}'"""

institute_wise_crimes_criminal_noLoc = """
select sum(a.MURDER) as sum_murder, sum(a.NEGLIGENT_MANSLAUGHTER) as sum_negligent_manslaughter, 
sum(a.FORCIBLE_SEX) as sum_forcible_sex,  sum(a.NONFORCIBLE_SEX) as sum_nonforcible_sex, 
sum(a.ROBBERY) as sum_robbery, sum(a.AGGRAVATED_ASSAULTS) as sum_aggravated_assault,
sum(a.BURGLARY) as sum_burglary, sum(a.MOTOR_VEHICLE_THEFT) as sum_motor_vehicle_theft,
sum(a.ARSON) as sum_arson
from criminal a
inner join institute i on i.id = a.instituteid
where i.name = '{inst_name}' and a.year = '{year}'"""

all_criminal_offences_year_group = "select YEAR, SUM(CRIMINAL_OFFENCES) from " \
                                   "(select year, (MURDER + NEGLIGENT_MANSLAUGHTER + FORCIBLE_SEX+NONFORCIBLE_SEX+" \
                                   "ROBBERY+AGGRAVATED_ASSAULTS+BURGLARY+MOTOR_VEHICLE_THEFT+ARSON) " \
                                   "as CRIMINAL_OFFENCES from CRIMINAL C JOIN INSTITUTE I on C.INSTITUTEID = I.ID " \
                                   "JOIN SECTOR S on I.SECTORID = S.ID {filter_str}) group by  YEAR"

all_hate_offences_year_group = "select YEAR, SUM(CRIMINAL_OFFENCES) from " \
                                   "(select year, (MURDER + FORCIBLE_SEX+NONFORCIBLE_SEX+" \
                                   "ROBBERY+AGGRAVATED_ASSAULTS+BURGLARY+MOTOR_VEHICLE_THEFT+ARSON+VANDALISM+INTIMIDATION+" \
                                   "SIMPLE_ASSAULT+LARCENY) " \
                                   "as CRIMINAL_OFFENCES from HATE C JOIN INSTITUTE I on C.INSTITUTEID = I.ID " \
                                   "JOIN SECTOR S on I.SECTORID = S.ID {filter_str}) group by  YEAR"

all_vawa_offences_year_group = "select YEAR, SUM(CRIMINAL_OFFENCES) from " \
                                   "(select year, (DOMESTIC_VIOLENCE+DATING_VIOLENCE+STALKING) " \
                                   "as CRIMINAL_OFFENCES from VAWA C JOIN INSTITUTE I on C.INSTITUTEID = I.ID " \
                                   "JOIN SECTOR S on I.SECTORID = S.ID {filter_str}) group by  YEAR"

all_arrests_year_group = "select YEAR, SUM(CRIMINAL_OFFENCES) from " \
                                   "(select year, (WEAPONS+DRUGS+LIQUOR) " \
                                   "as CRIMINAL_OFFENCES from ARREST C JOIN INSTITUTE I on C.INSTITUTEID = I.ID " \
                                   "JOIN SECTOR S on I.SECTORID = S.ID {filter_str}) group by  YEAR"

all_da_year_group = "select YEAR, SUM(CRIMINAL_OFFENCES) from " \
                                   "(select year, (WEAPONS+DRUGS+LIQUOR) " \
                                   "as CRIMINAL_OFFENCES from DISCIPLINARY_ACTION C JOIN INSTITUTE I on C.INSTITUTEID = I.ID " \
                                   "JOIN SECTOR S on I.SECTORID = S.ID {filter_str}) group by  YEAR"

generic_year_group = "select year,sum({sub_cat_type}) from" \
                     "(select * from {cat_type} C JOIN INSTITUTE I on C.INSTITUTEID = I.ID " \
                     "JOIN SECTOR S on I.SECTORID = S.ID" \
                     "{filter_str}) group by YEAR"


compare_university_arrest = """select sum(WEAPONS), sum(DRUGS), sum(LIQUOR) 
						from arrest, (select ID from institute where name = '{inst_name}') inst 
						where arrest.INSTITUTEID = inst.ID and arrest.year = {year}"""

compare_university_disc_action = """select sum(WEAPONS), sum(DRUGS), sum(LIQUOR) 
						from disciplinary_action, (select ID from institute where name = '{inst_name}') inst 
						where disciplinary_action.INSTITUTEID = inst.ID and disciplinary_action.year = {year}"""

compare_university_criminal = """select sum(MURDER), sum(NEGLIGENT_MANSLAUGHTER), sum(FORCIBLE_SEX),
							 sum(NONFORCIBLE_SEX), sum(ROBBERY), sum(AGGRAVATED_ASSAULTS),
							 sum(BURGLARY), sum(MOTOR_VEHICLE_THEFT), sum(ARSON)
						from criminal, (select ID from institute where name = '{inst_name}') inst 
						where criminal.INSTITUTEID = inst.ID and criminal.year = {year}"""

compare_university_vawa = """select sum(DOMESTIC_VIOLENCE), sum(DATING_VIOLENCE), sum(STALKING) 
						from vawa, (select ID from institute where name = '{inst_name}') inst 
						where vawa.INSTITUTEID = inst.ID and vawa.year = {year}"""

compare_university_hate = """select sum(MURDER), sum(VANDALISM), sum(FORCIBLE_SEX),
							 sum(NONFORCIBLE_SEX), sum(ROBBERY), sum(AGGRAVATED_ASSAULTS),
							 sum(BURGLARY), sum(MOTOR_VEHICLE_THEFT), sum(ARSON),
							 sum(INTIMIDATION), sum(SIMPLE_ASSAULT), sum(LARCENY)
						from hate, (select ID from institute where name = '{inst_name}') inst 
						where hate.INSTITUTEID = inst.ID and hate.year = {year}"""

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

