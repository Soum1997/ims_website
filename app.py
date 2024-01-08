from flask import Flask,render_template,jsonify

app=Flask(__name__)

COURSES = [
    {
        'id':1,
        'title':'CAT',
        'fees':'Rs 45,000'
    },
    {
        'id':2,
        'title':'CLAT',
        'fees':'Rs 35,000'
    },
    {
        'id':3,
        'title':'CET',
        'fees':'Rs 55,000'
    },

]


@app.route("/")
def hello_world():
    return render_template('home.html', courses=COURSES)

@app.route("/api/courses")
def list_courses():
    return jsonify(COURSES)

if __name__== "__main__":
    app.run(host='0.0.0.0', debug=True)