from flask import Flask,render_template,request
import pickle
import numpy as np


app = Flask(__name__)
model = pickle.load(open("startups.pkl","rb"))

@app.route("/")
def start():
    return render_template('index.html')


@app.route('/login',methods=['POST'])

def login():
    p = request.form['we']
    q = request.form['cl']
    r = request.form['deg']
    s = request.form['ug'] 
    t = request.form['pg']
    u = request.form['age']
    
    

    t= [[float(p),float(q),float(r),float(s),float(t),float(u)]]
    output = model.predict(t)
    print(output)

    return render_template("index.html",y="PREDICTED ANNUAL SALARY: "+str((output[0]))+" LPA")

if __name__ == '__main__' :
    app.run(port = 5000,debug=True)