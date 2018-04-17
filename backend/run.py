from flask import Flask, Response, request, render_template, redirect
from backend.logic import institute as it
from backend.logic import compare as comp

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
        print("institute_data: {institute_data}")
        years = [form_data['year']]
        locations = [form_data['location']]
        result = it.get_different_crimes_count_per_campus(form_data['institute'],
                                                          form_data['year'],
                                                          form_data['location'])
        print(result)
        # result = [{"crime_table": "Arrest", "crime_data": {"Main campus": 10, "Old Campus": 0}}]
    return render_template("institute.html", title='Campus Data', institute_data=institute_data, locations=locations, years=years, result=result)

@app.route("/compare", methods=['GET', 'POST'])
def compare():
    arrest_result = None
    disc_action_result = None
    criminal_result = None
    vawa_result = None
    hate_result = None
    inst_3_data = None
    if request.method == 'GET':
        institute_data = it.get_all_institute_names()
        years = [2013, 2014, 2015]
        locations = ['noncampus', 'campus', 'reported by', 'residence hall']
        inst_3_data = list(institute_data)
        inst_3_data.insert(0, "--None--")
    else:
        form_data = request.form
        institute_data = [form_data['institute1'], form_data['institute2'], form_data['institute3']]
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
