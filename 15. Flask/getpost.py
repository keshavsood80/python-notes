# How you can integrate html files in flask framework

# Create a Seperate HTML page, i need to redirect to that HTML page
# for that we will be using render_template library 

from flask import Flask, render_template,request
# render_template will be responsible in redirecting to that particular HTML page.
'''
It creates an instance of the Flask class,
which will be your WSGI (Web Server Gateway Interface) application.
'''


# app is a WSGI 

# if __name__ == "__main__"
# ( This is a entry point of any.py file)
# from here your execution will start

# app.run() -- it means this entire flask app is going to run.

# So this is the basic skeleton we use while we are creating our web framework using Flask.
app = Flask(__name__)

@app.route("/") 
# It's a decorator
# Slash basically means becomes my home page

def welcome():
    return '<htlm><h1>Welcome to this Flask course</h1></html>'

@app.route("/index",methods = ['GET'])
def index():
    return render_template('index.html')
# It is going to template folder and find index.html
# we have to create it html file where i need to insert some information

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/form",methods = ['GET','POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name}!'
    # with the help of name variable, i'll be putting some information in that particular HTML page.
    return render_template('form.html')
    # request method will be responsible in capturing the post or get request
    # just by using request function from the browser, it will be able to capture
    # pass : if this is a post request, I should be able to capture the information inside this
    # return : if it not a post, just go and return render template
if __name__ == "__main__": 
    app.run(debug=True)

# I dont have to be worry about web development bcoz in the team
#  we will be helped by front and backend developers.
# As a data scientist, basic knowledge of html is more than fine.


