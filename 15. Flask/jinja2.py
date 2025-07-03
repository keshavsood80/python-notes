# Building URL Dynamically
# Variable Rule
# jinja2 Template Engine

from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/") 
def welcome():
    return '<htlm><h1>Welcome to this Flask course</h1></html>'

@app.route("/index",methods = ['GET'])
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/submit",methods = ['GET','POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

# Variable Rule
# we are passing a parameter at route "<int:score>"
# We are assigning a rule to a variable that you only have to give an integer
@app.route('/success/<int:score>')
def success(score):
    return "The marks you got is" + score

if __name__ == "__main__": 
    app.run(debug=True)



