from flask import Flask, render_template, url_for, request

app = Flask(__name__)

dict={}


@app.route("/", methods=["GET","POST"])
def add():
    name = request.form.get("c_name")
    mobile = request.form.get("mobile_no")
    if request.method == "POST":
        dict.update({name:mobile})
        return render_template("display.html",name=name,mobile=mobile,dict=dict)
    else:
        return render_template("add.html",name=name,mobile=mobile,dict=dict)

@app.route("/display", methods=["GET","POST"])
def display():
    name = request.form.get("c_name")
    mobile = request.form.get("mobile_no")
    return render_template("display.html",name=name,mobile=mobile,dict=dict)

@app.route("/search",methods=["GET","POST"])
def search():
    name = request.form.get("c_name")
    mobile = request.form.get("mobile_no")
    search = request.form.get("search1")
    return render_template("search.html",name=name,mobile=mobile,dict=dict,search=search)

@app.route("/back")
def back():
    return render_template("add.html")



if __name__ == "__main__":
    app.run(debug=True)
