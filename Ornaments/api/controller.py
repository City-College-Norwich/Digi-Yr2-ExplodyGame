from flask import Flask, request
from model import Model

app = Flask(__name__)

model = Model()


@app.route("/")
def home():
    return model.callHomepage()


@app.route("/getNewId")
def getNewId():
    return model.getNewId()

@app.route("/getProgram")
def getProgram():
    args = request.args
    return model.getProgram(args["id"])

@app.route("/getStartTime")
def getStartTime():
    return model.getStartTime()

if __name__ == '__main__': app.run(host='0.0.0.0')