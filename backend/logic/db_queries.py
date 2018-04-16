all_institute_names = "select distinct(name) from institute"

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
select a.DOMESTIC_VIOLENCE, a.DATING_VIOLENCE, a.STALKING from vawa a
inner join institute i on i.id = a.instituteid
where a.Location = '{location}' and i.name = '{inst_name}' and a.year = {year}
"""

institute_wise_crimes_vawa_all = """
select a.DOMESTIC_VIOLENCE, a.DATING_VIOLENCE, a.STALKING from vawa a
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
select a.MURDER, a.NEGLIGENT_MANSLAUGHTER, a.FORCIBLE_SEX, a.NONFORCIBLE_SEX, a.ROBBERY, a.AGGRAVATED_ASSAULTS,
a.BURGLARY, a.MOTOR_VEHICLE_THEFT, a.ARSON from criminal a
inner join institute i on i.id = a.instituteid
where i.name = '{inst_name}'
and a.year = {year} and a.location = '{location}'"""

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





