from flask import Flask, render_template

app = Flask(__name__)

@app.route("/index")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/ministries")
def ministries():
    return render_template("ministries.html")

@app.route("/youth")
def youth():
    return render_template("youth.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/sermons")
def sermons():
    return render_template("sermons.html")

@app.route("/sunday school")
def sundayschool():
    return render_template("sunday school.html")

@app.route("/kingdom men")
def kingdommen():
    return render_template("kingdom men.html")

@app.route("/youth ministry")
def youthministry():
    return render_template("youth ministry.html")

@app.route("/women ministry")
def womenministry():
    return render_template("women ministry.html")

if __name__ == "__main__":
    app.run(debug=True)
