from flask import Flask, Response, request, render_template, redirect
from backend.logic import institute as it

app = Flask('Campus Safety Indicator')

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/chart")
def chart():
    labels = ["January","February","March","April","May","June","July","August"]
    values = [10,9,8,7,6,4,7,8]
    colors = [ "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA","#ABCDEF", "#DDDDDD", "#ABCABC"  ]
    return render_template('trial.html', set=zip(values, labels, colors))



@app.route('/institute', methods=['GET', 'POST'])
def institute():
    result = None
    result1 = None
    if request.method == 'GET':
        institute_data = it.get_all_institute_names()
        years = [2013, 2014, 2015, '--']
        locations = ['noncampus', 'oncampus', 'reported by', 'residence hall', '--']
        values_criminal = []
        labels_criminal = []
        colors_criminal = []
        values_hate = []
        labels_hate = []
        colors_hate = []
        labels_arrest = []
        values_arrest = []
        colors_arrest = []
        labels_disc = []
        values_disc = []
        colors_disc = []
        labels_vawa = []
        values_vawa = []
        colors_vawa = []

    else:
        print(request.form)
        form_data = request.form
        institute_data = [form_data['institute']]
        print(f"institute_data: {institute_data}")
        years = [form_data['year']]
        locations = [form_data['location']]
        result = it.get_different_crimes_count_per_campus(form_data['institute'],form_data['year'],form_data['location'])

        #adding new methods here -
        result1 = it.get_campus_crimes(form_data['institute'],form_data['year'],form_data['location'])

        print(result)
        print('ur here')
        print(result1)
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
        colors_criminal = [ "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA","#ABCDEF", "#DDDDDD", "#ABCABC"  ]

        labels_hate = ["Murder","Forcible Sex","Nonforcible Sex","Robbery","Aggravated Assaults","Burglary","Motor Vehicle Theft", "Arson", "Vandalism", "Intimidation",
                   "Simple Assault", "Larceny"]
        print('result1[3]')
        print(result1[0][0])
        values_hate = result1[2][0]
        colors_hate = [ "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA","#ABCDEF", "#DDDDDD", "#ABCABC", "#F7464A", "#46BFBD", "#FDB45C", "#F7464A", "#46BFBD"  ]
        #return render_template('trial.html', set=zip(values, labels, colors))

    return render_template("institute.html", title='Campus Data', institute_data=institute_data, locations=locations, years=years, result=result, set_arrest=zip(values_arrest, labels_arrest, colors_arrest), set_disc=zip(values_disc, labels_disc, colors_disc), set_vawa=zip(values_vawa, labels_vawa, colors_vawa), set_criminal=zip(values_criminal, labels_criminal, colors_criminal), set_hate=zip(values_hate, labels_hate, colors_hate))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
