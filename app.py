from app import app
from flask import render_template


@app.route("/")
def main():
    return render_template("index.html")

@app.route("/results")
def survery_results():
    return render_template("results.html")

if __name__ == "__main__":
    app.run(debug=True)