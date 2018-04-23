from flask import Flask, Response, request, render_template, redirect, jsonify
from backend.logic import institute as it
from backend.logic import rankings as rk
from backend.logic import geographical as geo
from backend.logic import trends
from backend.logic import compare as comp

app = Flask('Campus Safety Indicator')

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route('/institute', methods=['GET', 'POST'])
def institute():
    result = None
    result1 = None
    if request.method == 'GET':
        institute_data = it.get_all_institute_names()
        years = [2013, 2014, 2015, '--']
        locations = ['noncampus', 'oncampus', 'reported by', 'residence hall', '--']
        values_criminal = [0]
        labels_criminal = []
        colors_criminal = []
        values_hate = [0]
        labels_hate = []
        colors_hate = []
        labels_arrest = []
        values_arrest = [0]
        colors_arrest = []
        labels_disc = []
        values_disc = [0]
        colors_disc = []
        set_vawa = []
        labels_vawa = []
        values_vawa = [0]
        colors_vawa = []

    else:
        print(request.form)
        form_data = request.form
        institute_data = [form_data['institute']]
        print(f"institute_data: {institute_data}")
        years = [form_data['year']]
        locations = [form_data['location']]

        print('haha')

        print('form_data[''institute'']')
        print(form_data['institute'])

        print('form_data[''year'']')
        print(form_data['year'])

        print('form_data[''location'']')
        print(form_data['location'])

        result = it.get_different_crimes_count_per_campus(form_data['institute'],form_data['year'],form_data['location'])

        #adding new methods here -
        result1 = it.get_campus_crimes(form_data['institute'],form_data['year'],form_data['location'])

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
    return render_template("institute.html", title='Campus Data', institute_data=institute_data, locations=locations, years=years, result=result, set_arrest=list(values_arrest), set_disc=list(values_disc), set_vawa=list(values_vawa), set_criminal=list(values_criminal), set_hate=list(values_hate))


@app.route('/institutelist', methods=['GET'])
def instituteList():
    query = request.args['query']
    institute_data = it.get_institute_names_like(query)
    return jsonify(institute_data)



@app.route('/trends', methods=['GET', 'POST'])
def getTrends():
    result = None
    title = 'Trends'

    if request.method == 'GET':
        #institute_data = it.get_all_institute_names()
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

        cond = trends.generateFilterString(filter_input,form_data)

        if cat_type_input == 'CRIMINAL':
            if crime_type_input == 'ALL':
                legend = 'ALL'
                result = trends.get_all_criminal_offences_trends(cond)
            else:
                result = trends.get_generic_trends(cat_type_input, crime_type_input, cond)
                legend = crime_type_input

        elif cat_type_input == 'HATE':
            if hate_type_input == 'ALL':
                legend = 'ALL'
                result = trends.get_all_hate_trends(cond)
            else:
                legend = hate_type_input
                result = trends.get_generic_trends(cat_type_input, hate_type_input, cond)

        elif cat_type_input == 'VAWA':
            if vawa_type_input == 'ALL':
                legend = 'ALL'
                result = trends.get_all_vawa_trends(cond)
            else:
                legend = vawa_type_input
                result = trends.get_generic_trends(cat_type_input, vawa_type_input, cond)

        elif cat_type_input == 'ARREST':
            if arrest_type_input == 'ALL':
                legend = 'ALL'
                result = trends.get_all_arrest_trends(cond)
            else:
                legend = arrest_type_input
                result = trends.get_generic_trends(cat_type_input, arrest_type_input, cond)

        elif cat_type_input == 'DISCIPLINARY_ACTION':
            if da_type_input == 'ALL':
                legend = 'ALL'
                result = trends.get_all_disciplinary_action_trends(cond)
            else:
                legend = da_type_input
                result = trends.get_generic_trends(cat_type_input, da_type_input, cond)

        print(result)
        years, counts = zip(*result)
        counts = [0 if v is None else v for v in counts]
        return jsonify(years = years, counts = counts, legend = legend, graph_title = cat_type_input)
        #return render_template("trends.html", title=title, years = years, counts = counts,
         #                  result = result, legend = legend, graph_title = cat_type_input)


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
    rank_types = ['University', 'State']
    trends = ['All_Crimes', 'Arrest', 'Crime', 'Disciplinary', 'Hate', 'Vawa']
    years = [2013, 2014, 2015]
    result = []
    year = None
    rank_type = None
    if request.method == 'POST':
        form_data = request.form
        rank_type = form_data['rank_type']
        trend_type = form_data['trend_type']
        #year = form_data['year']
        print(f"rank_type: {rank_type}")
        if rank_type == "University":
            result = rk.get_arrest_institute_ranks_for_year()
        else:
            result = geo.get_arrest_state_rank()
        print(f"result of arrest rank query: {result}")
    return render_template("ranking.html", title="Ranking Stats", rank_type=rank_types, trends=trends, years=years, result=result, year_in_consideration=year, rank_element=rank_type)

@app.route('/geographical', methods=['GET', 'POST'])
def geographical():
    result, max_count = geo.get_state_geographical_data()
    print(f"result: {len(result)} max_count: {max_count}, {result}")
    return render_template("geographical.html", title="Geographical Stats", result=result, max_count=max_count)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
