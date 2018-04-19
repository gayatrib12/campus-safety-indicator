all_institute_names = "select distinct(name) from institute"

institute_crime_count = """select WEAPONS + DRUGS + LIQUOR, branch
                            from {crime_table}, (
                                select *
                                from institute
                                where name = '{inst_name}'
                            ) inst
                            where {crime_table}.instituteid = inst.id and year = {year}
                                and location = '{location}'"""

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