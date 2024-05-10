from app import app
from flask import render_template, request, jsonify
from app.services.validate_input import check_age


@app.route("/")
def main():
    return render_template("index.html")

@app.route("/results")
def survery_results():
    return render_template("results.html")

@app.route("/compute_age", methods=["POST"])
def get_age():
    if request.method == "POST":
        data = request.json
        birth_date = data["date"]
        if birth_date:
            age = check_age(birth_date)
            return jsonify({"age": age})
        else:
            return jsonify({"error": "Date not provided"}),


        

if __name__ == "__main__":
    app.run(debug=True)