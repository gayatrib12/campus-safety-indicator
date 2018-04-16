all_institute_names = "select distinct(name) from institute"

institute_names_like = "select distinct(name) from institute where lower(name) like '%' || lower('{query}') || '%'"

institute_crime_count = """select WEAPONS + DRUGS + LIQUOR, branch
                            from {crime_table}, (
                                select *
                                from institute
                                where name = '{inst_name}'
                            ) inst
                            where {crime_table}.instituteid = inst.id and year = {year}
                                and location = '{location}'"""

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

