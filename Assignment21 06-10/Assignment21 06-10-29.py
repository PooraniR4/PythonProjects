from flask import Flask,render_template
app=Flask(__name__)                     #create
@app.route('/')
def msg():
    return render_template("Assignment21.html")

if __name__ == "__main__":
    app.run(debug="true",port=5098)
