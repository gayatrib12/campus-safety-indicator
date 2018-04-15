from flask import Flask, Response, request, render_template, redirect, jsonify
from backend.logic import institute as it
from backend.logic import trends

app = Flask('Campus Safety Indicator')

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route('/institute', methods=['GET', 'POST'])
def institute():
    result = None
    if request.method == 'GET':
        institute_data = it.get_all_institute_names()
        years = [2013, 2014, 2015]
        locations = ['noncampus', 'campus', 'reported by', 'residence hall']
    else:
        print(request.form)
        form_data = request.form
        institute_data = [form_data['institute']]
        print(f"institute_data: {institute_data}")
        years = [form_data['year']]
        locations = [form_data['location']]
        result = it.get_different_crimes_count_per_campus(form_data['institute'],
                                                          form_data['year'],
                                                          form_data['location'])
        print(result)
        # result = [{"crime_table": "Arrest", "crime_data": {"Main campus": 10, "Old Campus": 0}}]
    return render_template("institute.html", title='Campus Data', institute_data=institute_data, locations=locations, years=years, result=result)

@app.route('/trends', methods=['GET', 'POST'])
def getTrends():
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
