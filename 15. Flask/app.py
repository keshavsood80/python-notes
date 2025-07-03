from flask import Flask
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
    return 'Welcome to this Flask course'

@app.route("/index")
def index():
    return 'Welcome to this index page'

if __name__ == "__main__": 
    app.run(debug=True)

