from app import app

@app.route("/")
def main():
    return "Hello Railway"


        
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)