from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("<name>")
def index(name=None):
  if name==None:
    return "Hello No one"
  else:
    return "Hello {}!".format(name)

  
