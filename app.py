from flask import Flask, render_template, request, jsonify
from utils import explain_code
import webbrowser
import threading

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Handle the incoming AJAX request with JSON payload
        data = request.get_json()  # Get the JSON data from the request
        code_input = data.get("code", "").strip()  # Extract the code from the JSON payload
        explanation = ""
        error = None

        if not code_input:
            error = "Please enter a Python code snippet."
        else:
            explanation = explain_code(code_input)
            if explanation.startswith("⚠️ Error:"):
                error = explanation
                explanation = ""

        return jsonify({"explanation": explanation, "error": error})  # Return as JSON response

    # For the initial GET request, render the template
    return render_template("index.html")

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")

if __name__ == "__main__":
    threading.Timer(1.5, open_browser).start()
    app.run(debug=False)
