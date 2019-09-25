from flask import Flask     # imports Flask class from the                                # 'flask' module.

app = Flask(__name__)       # 'app' is the object
app.config['DEBUG'] = True  # created by the constructor
                            # Flask. '_name_' is a variable
@app.route("/")             # controlled by Python that 
def index():                # tells code what module its in
  return "Hello World"      # 'app.config' - DEBUG                                      # configuration enabled.                                    # helpful when dev Flask apps 
                            # 'app.route' creates a mapping
app.run()                   # between path, root or "/" and
                            # fxn we're going to define
                            # def index(): define index, 
                            # fxn of zero variables
                            # return - fxn returns string    # literal
                            # app.run() - pass control to the # Flask object. run fxn loops     # forever, so put it last.
                            # acts as web server, ready for 
                            # requests/ responses over network
                            # connection
# server up and running, GET / HTTP/1.1, with response code of 200,