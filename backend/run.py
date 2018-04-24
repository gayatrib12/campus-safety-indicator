from flask import Flask, Response, request, render_template, redirect, jsonify
from backend.logic import institute as it
from backend.logic import rankings as rk
from backend.logic import geographical as geo
from backend.logic import trends as trnds
from backend.logic import compare as comp
from backend.logic import index as ind

app = Flask('Campus Safety Indicator')

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route('/institute', methods=['GET', 'POST'])
def institute():
    result = None
    result1 = None
    store_inst_name = []
    message = 0

    years = ['--',2013, 2014, 2015]
    locations = ['--','noncampus', 'oncampus', 'reported by', 'residence hall']

    if request.method == 'GET':
        institute_data = it.get_all_institute_names()
        values_criminal = [0]
        values_hate = [0]
        values_arrest = [0]
        values_disc = [0]
        values_vawa = [0]

    else:
        message = 1
        print(request.form)
        form_data = request.form
        institute_data = [form_data['institute']]
        print(f"institute_data: {institute_data}")
#        years = [form_data['year']]
        years = '--'
        locations.remove(form_data['location'])
        locations.insert(0, form_data['location'])
        store_inst_name = form_data['institute']

        print('haha')

        print('form_data[''institute'']')
        print(form_data['institute'])

        #print('form_data[''year'']')
        #print(form_data['year'])

        print('form_data[''location'']')
        print(form_data['location'])

        #result = it.get_different_crimes_count_per_campus(form_data['institute'],form_data['year'],form_data['location'])

        #adding new methods here -
        result1 = it.get_campus_crimes(form_data['institute'],'--',form_data['location'])

        # print(result)
        # print('ur here')
        # print(result1)
        # result = [{"crime_table": "Arrest", "crime_data": {"Main campus": 10, "Old Campus": 0}}]

        labels_arrest = ["Weapons","Drug","Liquor"]
        #values_arrest = result1[3]
        values_arrest = result1[3][0]
        colors_arrest = [ "#F7464A", "#46BFBD", "#FDB45C"]

        labels_disc = ["Weapons","Drug","Liquor"]
        #values_disc = result1[3]
        values_disc = result1[4][0]
        colors_disc = [ "#19D464", "#8F19D4", "#C1D419"]

        labels_vawa = ["Domestic Violence","Dating Violence","Stalking"]
        #values_arrest = result1[3]
        values_vawa = result1[1][0]
        colors_vawa = [ "#3219D4", "#D46A19", "#D419A8"]

        labels_criminal = ["Murder","Negligent Manslaughter","Forcible Sex","Nonforcible Sex","Robbery","Aggravated Assaults","Burglary","Motor Vehicle Theft", "Arson"]
        #values_criminal = result1[0][0]
        values_criminal = result1[0][0]
        colors_criminal = [ "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA","#ABCDEF", "#DDDDDD", "#ABCABC","#F7464A", "#46BFBD"  ]

        labels_hate = ["Murder","Forcible Sex","Nonforcible Sex","Robbery","Aggravated Assaults","Burglary","Motor Vehicle Theft", "Arson", "Vandalism", "Intimidation",
                   "Simple Assault", "Larceny"]
        # print('result1[3]')
        # print(result1[0][0])
        values_hate = result1[2][0]
        colors_hate = [ "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA","#ABCDEF", "#DDDDDD", "#ABCABC", "#F7464A", "#46BFBD", "#FDB45C", "#F7464A", "#46BFBD"  ]
        #return render_template('trial.html', set=zip(values, labels, colors))

        print('haha')
        #abc = zip(values_vawa, labels_vawa, colors_vawa)
        print(f"abc :{values_vawa}")

    # return render_template("institute.html", title='Campus Data', institute_data=institute_data, locations=locations, years=years, result=result, set_arrest=zip(values_arrest, labels_arrest, colors_arrest), set_disc=zip(values_disc, labels_disc, colors_disc), set_vawa=list(values_vawa), set_criminal=zip(values_criminal, labels_criminal, colors_criminal), set_hate=zip(values_hate, labels_hate, colors_hate))
    return render_template("institute.html", title='Campus Data', message=message, institute_data=institute_data, store_inst_name=store_inst_name, locations=locations, years=years, result=result, set_arrest=list(values_arrest), set_disc=list(values_disc), set_vawa=list(values_vawa), set_criminal=list(values_criminal), set_hate=list(values_hate))


@app.route('/institutelist', methods=['GET'])
def instituteList():
    query = request.args['query']
    institute_data = it.get_institute_names_like(query)
    return jsonify(institute_data)



@app.route('/trends', methods=['GET', 'POST'])
def trends():
    result = None
    title = 'Trends'

    if request.method == 'GET':
        return render_template("trends.html", title=title)

    elif request.method == 'POST':

        print(request.form)

        #return render_template("trends.html", title=title)

        form_data = request.form

        result = []

        cat_type_input = [form_data['cat_type_input']][0]
        crime_type_input = [form_data['crime_type_input']][0]
        hate_type_input = [form_data['hate_type_input']][0]
        vawa_type_input = [form_data['vawa_type_input']][0]
        arrest_type_input = [form_data['arrest_type_input']][0]
        da_type_input = [form_data['da_type_input']][0]
        filter_input = [form_data['filter_input']][0]

        legend = ''

        cond = trnds.generateFilterString(filter_input, form_data)

        if cat_type_input == 'CRIMINAL':
            if crime_type_input == 'ALL':
                legend = 'ALL'
                result = trnds.get_all_criminal_offences_trends(cond)
            else:
                result = trnds.get_generic_trends(cat_type_input, crime_type_input, cond)
                legend = crime_type_input

        elif cat_type_input == 'HATE':
            if hate_type_input == 'ALL':
                legend = 'ALL'
                result = trnds.get_all_hate_trends(cond)
            else:
                legend = hate_type_input
                result = trnds.get_generic_trends(cat_type_input, hate_type_input, cond)

        elif cat_type_input == 'VAWA':
            if vawa_type_input == 'ALL':
                legend = 'ALL'
                result = trnds.get_all_vawa_trends(cond)
            else:
                legend = vawa_type_input
                result = trnds.get_generic_trends(cat_type_input, vawa_type_input, cond)

        elif cat_type_input == 'ARREST':
            if arrest_type_input == 'ALL':
                legend = 'ALL'
                result = trnds.get_all_arrest_trends(cond)
            else:
                legend = arrest_type_input
                result = trnds.get_generic_trends(cat_type_input, arrest_type_input, cond)

        elif cat_type_input == 'DISCIPLINARY_ACTION':
            if da_type_input == 'ALL':
                legend = 'ALL'
                result = trnds.get_all_disciplinary_action_trends(cond)
            else:
                legend = da_type_input
                result = trnds.get_generic_trends(cat_type_input, da_type_input, cond)

        print(result)
        years, counts = zip(*result)
        counts = [0 if v is None else v for v in counts]
        return jsonify(years = years, counts = counts, legend = legend, graph_title = cat_type_input)


@app.route("/compare", methods=['GET', 'POST'])
def compare():
    arrest_result = None
    disc_action_result = None
    criminal_result = None
    vawa_result = None
    hate_result = None
    inst_3_data = None
    institute_data = None
    if request.method == 'GET':
        # institute_data = it.get_all_institute_names()
        years = [2013, 2014, 2015]
        # locations = ['noncampus', 'campus', 'reported by', 'residence hall']
        # inst_3_data = list(institute_data)
        # inst_3_data.insert(0, "--None--")
        return render_template("compare.html", title='Compare Data', years = years, institute_data=institute_data)
    else:
        form_data = request.form
        institute_data = [form_data['institute1'], form_data['institute2'], form_data['institute3']]
        print(institute_data)
        if (institute_data[-1] == "--None--"):
            institute_data.pop()
        inst_count = len(institute_data)
        inst_3_data = list(institute_data) #verify this
        years = [form_data['year']]
        arrest_result = comp.get_comparison_arrest(institute_data, form_data['year'], inst_count)
        disc_action_result = comp.get_comparison_disc_action(institute_data, form_data['year'], inst_count)
        criminal_result = comp.get_comparison_criminal(institute_data, form_data['year'], inst_count)
        vawa_result = comp.get_comparison_vawa(institute_data, form_data['year'], inst_count)
        hate_result = comp.get_comparison_hate(institute_data, form_data['year'], inst_count)
        print(vawa_result)
    return render_template("compare.html", title='Compare Data', institute_data=institute_data, inst_3_data=inst_3_data,
        years=years, result=arrest_result, disc_result=disc_action_result, criminal_result=criminal_result,
        vawa_result=vawa_result, hate_result=hate_result)


@app.route('/ranking', methods=['GET', 'POST'])
def ranking():
    rank_types = ['University', 'State', 'University Category']
    trends = ['Arrest', 'Crime', 'Disciplinary', 'Hate', 'Vawa']
    categories = ['Huge', 'Large', 'Medium', 'Small']
    years = [2013, 2014, 2015]
    result = []
    year = None
    rank_type = None
    if request.method == 'POST':
        form_data = request.form
        rank_type = form_data['rank_type']
        trend_type = form_data['trend_type']
        rank_types.remove(rank_type)
        rank_types.insert(0, rank_type)
        trends.remove(trend_type)
        trends.insert(0, trend_type)
        #year = form_data['year']
        print(f"rank_type: {rank_type}")
        if rank_type == "University":
            func = getattr(rk, f"get_{trend_type.lower()}_institute_ranks")
            result = func()
        elif rank_type == 'University Category':
            print("in University category")
            category = form_data['category']
            print(f"received category: {category}")
            categories.remove(category)
            categories.insert(0, category)
            func = getattr(rk, f"get_categorize_{trend_type.lower()}_institute_ranks")
            result = func(category.lower())
        else:
            func = getattr(rk, f"get_{trend_type.lower()}_state_ranks")
            result = func()
        print(f"result of arrest rank query: {result}")
    return render_template("ranking.html", title="Ranking Stats", rank_type=rank_types, trends=trends, years=years, result=result, year_in_consideration=year, rank_element=rank_type, categories=categories)

@app.route('/geographical', methods=['GET', 'POST'])
def geographical():
    stat_type = ['Crime', 'Student Count', 'Control of University']
    crime_type = ['Arrest', 'Crime', 'Disciplinary', 'Hate', 'Vawa']
    sector_type = ['Public', 'Private non-profit', 'Private for-profit']
    color_codes = {
        'max': '#800026',
        'min': '#ffffcc'
    }
    result = False
    actual_count = {}
    min_label = max_label = ""
    if request.method == 'POST':
        print("getting post request from geograp")
        result = True
        category_type = request.form['cat_type']
        if category_type == "crime":
            category_type = request.form['crime_type_input']
            crime_type.remove(category_type.title())
            crime_type.insert(0, category_type.title())
            max_label = 'Most disturbed'
            min_label = 'Least disturbed'
            func = getattr(geo, f"get_state_{category_type}_data")
            result, actual_count = func()
        elif category_type == 'student':
            stat_type.remove('Student Count')
            stat_type.insert(0, 'Student Count')
            color_codes['max'] = '#004cd1'
            color_codes['min'] = '#d9e7fe'
            max_label = 'Most students'
            min_label = 'Least students'
            func = getattr(geo, f"get_state_{category_type}_data")
            result, actual_count = func()
        elif category_type == 'sector':
            stat_type.remove('Control of University')
            stat_type.insert(0, 'Control of University')
            color_codes['max'] = '#009302'
            color_codes['min'] = '#ddffde'
            max_label = "Most Universities"
            min_label = "Least Universities"
            sector = request.form['institute_sector']
            if sector == '1,4,7':
                sector_to_modify = 'Public'
            elif sector == '2,5,8':
                sector_to_modify = 'Private non-profit'
            else:
                sector_to_modify = 'Private for-profit'
            sector_type.remove(sector_to_modify)
            sector_type.insert(0, sector_to_modify)
            func = getattr(geo, f"get_state_{category_type}_data")
            result, actual_count = func(sector)
        print(f"result: {len(result)} {result}")
    return render_template("geographical.html", title="Geographical Stats", in_range_result=result, actual_count=actual_count, color_codes=color_codes, result=result, max_label=max_label, min_label=min_label, crime_type=crime_type, stat_type=stat_type, sector_type=sector_type)

@app.route('/tuple_count', methods=['POST'])
def tuple_count():
    data = {"total_count": ind.get_total_tuple_count()}
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
