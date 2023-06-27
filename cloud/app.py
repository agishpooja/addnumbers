from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/", methods=['POST','GET'])

def calculate():
    calc=''
    if request.method=='POST' and 'num1' in request.form and 'num2' in request.form:
       num1=float(request.form.get('num1'))
       num2=float(request.form.get('num2'))
       calc=num1+num2
    return render_template("index.html",calc=calc)