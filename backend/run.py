from flask import Flask, Response, request, render_template, redirect, jsonify
from backend.logic import institute as it
from backend.logic import rankings as rk
from backend.logic import geographical as geo

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
    return render_template("geographical.html", result=result, max_count=max_count)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
