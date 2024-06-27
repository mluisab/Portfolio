from flask import Flask, render_template
app = Flask(__name__)    
    
@app.route("/")
def homepage():
        return render_template("homepage.html")

@app.route("/Worldwide/")
def About():
    return render_template("Worldwide.html")
if __name__ == '__main__':
    app.run(debug=True)

@app.route("/Sources/")
def ISP_Instructions():
    return render_template("Sources.html")
if __name__ == '__main__':
    app.run(debug=True)
