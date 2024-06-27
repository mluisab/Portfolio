from flask import Flask, render_template
app = Flask(__name__)    
    
@app.route("/")
def Homepage():
        return render_template("Homepage.html")

@app.route("/ISP_Instructions/")
def ISP_Instructions():
    return render_template("ISP_Instructions.html")
if __name__ == '__main__':
    app.run(debug=True)

@app.route("/ISP_Checklist/")
def ISP_Checklist():
    return render_template("ISP_Checklist.html")
if __name__ == '__main__':
    app.run(debug=True)

@app.route("/ISP_General/")
def ISP_General():
    return render_template("ISP_General.html")
if __name__ == '__main__':
    app.run(debug=True)

@app.route("/ISP_Availability/")
def ISP_Availability():
    return render_template("ISP_Availability.html")
if __name__ == '__main__':
    app.run(debug=True)

@app.route("/ISP_Confidentiality/")
def ISP_Confidentiality():
    return render_template("ISP_Confidentiality.html")
if __name__ == '__main__':
    app.run(debug=True)

@app.route("/ISP_Integrity/")
def ISP_Integrity():
    return render_template("ISP_Integrity.html")
if __name__ == '__main__':
    app.run(debug=True)

@app.route("/ISP_Privacy/")
def ISP_Privacy():
    return render_template("ISP_Privacy.html")
if __name__ == '__main__':
    app.run(debug=True)

@app.route("/ISP_risk_summary/")
def ISP_risk_summary():
    return render_template("ISP_risk_summary.html")
if __name__ == '__main__':
    app.run(debug=True)

@app.route("/ISP_Risk_Criteria/")
def ISP_Risk_Criteria():
    return render_template("ISP_Risk_Criteria.html")
if __name__ == '__main__':
    app.run(debug=True)

@app.route("/Approved_software/")
def Approved_software():
    return render_template("Approved_software.html")
if __name__ == '__main__':
    app.run(debug=True)

@app.route("/Contacts/")
def Contacts():
    return render_template("Contacts.html")
if __name__ == '__main__':
    app.run(debug=True)

