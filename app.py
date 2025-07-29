from flask import Flask, render_template, request
from text_analysis import analyze_text  # Ensure filename is correct

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    output = None
    if request.method == "POST":
        user_input = request.form["user_input"]
        output = analyze_text(user_input)  # This must return a dict
        # print("DEBUG OUTPUT:", output)     # See logs in terminal
    return render_template("index.html", output=output)

if __name__ == "__main__":
    app.run(debug=True)
