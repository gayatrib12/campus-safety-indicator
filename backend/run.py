from flask import Flask, Response, request, render_template, redirect
from backend.logic import institute as it

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
