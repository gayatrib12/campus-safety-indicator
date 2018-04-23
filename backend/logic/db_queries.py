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
select Coalesce(sum(a.WEAPONS),0) as sum_weapons, Coalesce(sum(a.DRUGS),0) as sum_drugs, Coalesce(sum(a.LIQUOR),0) as sum_liquor from INSTITUTE i
inner join {crime_table} a on i.ID = a.instituteid
where i.NAME = '{inst_name}' and a.LOCATION = '{location}' and a.YEAR = {year}
"""

institute_wise_crimes_arrest_all = """
select Coalesce(sum(a.DRUGS),0) as sum_drugs, Coalesce(sum(a.WEAPONS),0) as sum_weapons, Coalesce(sum(a.LIQUOR),0) as sum_liquor from INSTITUTE i
inner join {crime_table} a on i.id = a.instituteid
where i.name = '{inst_name}'
"""

institute_wise_crimes_arrest_noLoc = """
select Coalesce(sum(a.DRUGS),0) as sum_drugs, Coalesce(sum(a.WEAPONS),0) as sum_weapons, Coalesce(sum(a.LIQUOR),0) as sum_liquor from INSTITUTE i
inner join {crime_table} a on i.id = a.instituteid
where i.name = '{inst_name}' and a.year = {year}
"""

institute_wise_crimes_arrest_noYear = """
select Coalesce(sum(a.DRUGS),0) as sum_drugs, Coalesce(sum(a.WEAPONS), 0) as sum_weapons, Coalesce(sum(a.LIQUOR),0) as sum_liquor from INSTITUTE i
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
select Coalesce(sum(a.DOMESTIC_VIOLENCE),0) as DOMESTIC_VIOLENCE, Coalesce(sum(a.DATING_VIOLENCE),0) as DATING_VIOLENCE, Coalesce(sum(a.STALKING),0) as STALKING from vawa a
inner join institute i on i.id = a.instituteid
where i.name = '{inst_name}'
"""

institute_wise_crimes_vawa_noLoc = """
select Coalesce(sum(a.DOMESTIC_VIOLENCE),0) as sum_domestic, Coalesce(sum(a.DATING_VIOLENCE),0) as sum_dating, Coalesce(sum(a.STALKING),0) as sum_stalking from vawa a
inner join institute i on i.id = a.instituteid
where i.name = '{inst_name}' and a.year = {year}
"""

institute_wise_crimes_vawa_noYear = """
select Coalesce(sum(a.DOMESTIC_VIOLENCE),0) as sum_domestic, Coalesce(sum(a.DATING_VIOLENCE),0) as sum_dating, Coalesce(sum(a.STALKING),0) as sum_stalking from vawa a
inner join institute i on i.id = a.instituteid
where i.name = '{inst_name}' and a.Location = '{location}'
"""
# ------------- hate section ---------------------

institute_wise_crimes_hate = """
select Coalesce(sum(a.MURDER),0) as sum_murder, Coalesce(sum(a.FORCIBLE_SEX),0) as sum_forcible_sex, Coalesce(sum(a.NONFORCIBLE_SEX),0) as sum_nonforcible_sex, 
Coalesce(sum(a.ROBBERY),0) as sum_robbery, Coalesce(sum(a.AGGRAVATED_ASSAULTS),0) as sum_aggravated_assault,
Coalesce(sum(a.BURGLARY),0) as sum_burglary, Coalesce(sum(a.MOTOR_VEHICLE_THEFT),0) as sum_motor_vehicle_theft,
Coalesce(sum(a.ARSON),0) as sum_arson, Coalesce(sum(a.VANDALISM),0) as sum_vandalism, Coalesce(sum(a.INTIMIDATION),0) as sum_intimidation, 
Coalesce(sum(a.SIMPLE_ASSAULT),0) as sum_simple_assault, Coalesce(sum(a.LARCENY),0) as sum_larceny from hate a
inner join institute i on i.id = a.instituteid
where i.name = '{inst_name}'
and a.YEAR = {year} and a.LOCATION = '{location}'
"""

institute_wise_crimes_hate_all = """
select Coalesce(sum(a.MURDER),0) as sum_murder, Coalesce(sum(a.FORCIBLE_SEX),0) as sum_forcible_sex, Coalesce(sum(a.NONFORCIBLE_SEX),0) as sum_nonforcible_sex, 
Coalesce(sum(a.ROBBERY),0) as sum_robbery, Coalesce(sum(a.AGGRAVATED_ASSAULTS),0) as sum_aggravated_assault,
Coalesce(sum(a.BURGLARY),0) as sum_burglary, Coalesce(sum(a.MOTOR_VEHICLE_THEFT),0) as sum_motor_vehicle_theft,
Coalesce(sum(a.ARSON),0) as sum_arson, Coalesce(sum(a.VANDALISM),0) as sum_vandalism, Coalesce(sum(a.INTIMIDATION),0) as sum_intimidation, 
Coalesce(sum(a.SIMPLE_ASSAULT),0) as sum_simple_assault, Coalesce(sum(a.LARCENY),0) as sum_larceny from hate a
inner join institute i on i.id = a.instituteid
where i.name = '{inst_name}'
"""

institute_wise_crimes_hate_noLoc = """
select Coalesce(sum(a.MURDER),0) as sum_murder, Coalesce(sum(a.FORCIBLE_SEX),0) as sum_forcible_sex, Coalesce(sum(a.NONFORCIBLE_SEX),0) as sum_nonforcible_sex, 
Coalesce(sum(a.ROBBERY),0) as sum_robbery, Coalesce(sum(a.AGGRAVATED_ASSAULTS),0) as sum_aggravated_assault,
Coalesce(sum(a.BURGLARY),0) as sum_burglary, Coalesce(sum(a.MOTOR_VEHICLE_THEFT),0) as sum_motor_vehicle_theft,
Coalesce(sum(a.ARSON),0) as sum_arson, Coalesce(sum(a.VANDALISM),0) as sum_vandalism, Coalesce(sum(a.INTIMIDATION),0) as sum_intimidation, 
Coalesce(sum(a.SIMPLE_ASSAULT),0) as sum_simple_assault, Coalesce(sum(a.LARCENY),0) as sum_larceny from hate a
inner join institute i on i.id = a.instituteid
where i.name = '{inst_name}' and a.year = {year}
"""

institute_wise_crimes_hate_noYear = """
select Coalesce(sum(a.MURDER),0) as sum_murder, Coalesce(sum(a.FORCIBLE_SEX),0) as sum_forcible_sex, Coalesce(sum(a.NONFORCIBLE_SEX),0) as sum_nonforcible_sex, 
Coalesce(sum(a.ROBBERY),0) as sum_robbery, Coalesce(sum(a.AGGRAVATED_ASSAULTS),0) as sum_aggravated_assault,
Coalesce(sum(a.BURGLARY),0) as sum_burglary, Coalesce(sum(a.MOTOR_VEHICLE_THEFT),0) as sum_motor_vehicle_theft,
Coalesce(sum(a.ARSON),0) as sum_arson, Coalesce(sum(a.VANDALISM),0) as sum_vandalism, Coalesce(sum(a.INTIMIDATION),0) as sum_intimidation, 
Coalesce(sum(a.SIMPLE_ASSAULT),0) as sum_simple_assault, Coalesce(sum(a.LARCENY),0) as sum_larceny from hate a
inner join institute i on i.id = a.instituteid
where i.name = '{inst_name}' and a.location = '{location}'
"""
# ------------- criminal section ---------------------

institute_wise_crimes_criminal = """
select Coalesce(sum(a.MURDER),0) as MURDER, Coalesce(sum(a.NEGLIGENT_MANSLAUGHTER),0) as NEGLIGENT_MANSLAUGHTER, Coalesce(sum(a.FORCIBLE_SEX),0) as FORCIBLE_SEX, 
Coalesce(sum(a.NONFORCIBLE_SEX),0) as NONFORCIBLE_SEX, Coalesce(sum(a.ROBBERY),0) as ROBBERY, Coalesce(sum(a.AGGRAVATED_ASSAULTS),0) as AGGRAVATED_ASSAULTS,
Coalesce(sum(a.BURGLARY),0) as BURGLARY, Coalesce(sum(a.MOTOR_VEHICLE_THEFT),0) as MOTOR_VEHICLE_THEFT, Coalesce(sum(a.ARSON),0) as ARSON 
from criminal a
inner join institute i on i.id = a.instituteid
where i.name = '{inst_name}'
and a.year = {year} and a.location = '{location}'
"""

institute_wise_crimes_criminal_all = """
select Coalesce(sum(a.MURDER),0) as sum_murder, Coalesce(sum(a.NEGLIGENT_MANSLAUGHTER),0) as sum_negligent_manslaughter, 
Coalesce(sum(a.FORCIBLE_SEX),0) as sum_forcible_sex,  Coalesce(sum(a.NONFORCIBLE_SEX),0) as sum_nonforcible_sex, 
Coalesce(sum(a.ROBBERY),0) as sum_robbery, Coalesce(sum(a.AGGRAVATED_ASSAULTS),0) as sum_aggravated_assault,
Coalesce(sum(a.BURGLARY),0) as sum_burglary, Coalesce(sum(a.MOTOR_VEHICLE_THEFT),0) as sum_motor_vehicle_theft,
Coalesce(sum(a.ARSON),0) as sum_arson
from criminal a
inner join institute i on i.id = a.instituteid
where i.name = '{inst_name}'"""

institute_wise_crimes_criminal_noYear = """
select Coalesce(sum(a.MURDER),0) as sum_murder, Coalesce(sum(a.NEGLIGENT_MANSLAUGHTER),0) as sum_negligent_manslaughter, 
Coalesce(sum(a.FORCIBLE_SEX),0) as sum_forcible_sex,  Coalesce(sum(a.NONFORCIBLE_SEX),0) as sum_nonforcible_sex, 
Coalesce(sum(a.ROBBERY),0) as sum_robbery, Coalesce(sum(a.AGGRAVATED_ASSAULTS),0) as sum_aggravated_assault,
Coalesce(sum(a.BURGLARY),0) as sum_burglary, Coalesce(sum(a.MOTOR_VEHICLE_THEFT),0) as sum_motor_vehicle_theft,
Coalesce(sum(a.ARSON),0) as sum_arson
from criminal a
inner join institute i on i.id = a.instituteid
where i.name = '{inst_name}' and a.location = '{location}'"""

institute_wise_crimes_criminal_noLoc = """
select Coalesce(sum(a.MURDER),0) as sum_murder, Coalesce(sum(a.NEGLIGENT_MANSLAUGHTER),0) as sum_negligent_manslaughter, 
Coalesce(sum(a.FORCIBLE_SEX),0) as sum_forcible_sex,  Coalesce(sum(a.NONFORCIBLE_SEX),0) as sum_nonforcible_sex, 
Coalesce(sum(a.ROBBERY),0) as sum_robbery, Coalesce(sum(a.AGGRAVATED_ASSAULTS),0) as sum_aggravated_assault,
Coalesce(sum(a.BURGLARY),0) as sum_burglary, Coalesce(sum(a.MOTOR_VEHICLE_THEFT),0) as sum_motor_vehicle_theft,
Coalesce(sum(a.ARSON),0) as sum_arson
from criminal a
inner join institute i on i.id = a.instituteid
where i.name = '{inst_name}' and a.year = '{year}'"""

#------------------------------------------------------------------------------------

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

total_tuple_count = """
select *
from (select (
              (select count(*) from arrest)
              + (select count(*) from bias)
              + (select count(*) from criminal)
              + (select count(*) from DISCIPLINARY_ACTION)
              + (select count(*) from hate)
              + (select count(*) from institute)
              + (select count(*) from location)
              + (select count(*) from sector)
              + (select count(*) from vawa)
              ) as total_count
      from bias)
where rownum = 1
"""
