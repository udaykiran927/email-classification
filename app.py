from flask import Flask,render_template,request,Response

app=Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html")
@app.route("/choice",methods=["POST","GET"])
def choice():
    return render_template("mail.html")
@app.route("/predict",methods=["POST","GET"])
def predict():
    return render_template("mail.html",msg="Unable to access your mail")


if __name__=='__main__':
    app.run(debug=True)
