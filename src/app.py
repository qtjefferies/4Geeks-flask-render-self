from flask import Flask, request, render_template
from pickle import load
import os


# Define the Flask app and set the template folder path
app = Flask(__name__, template_folder='../templates')

# Get the absolute path to the model file
model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../models/tree2_model.pkl")
with open(model_path, 'rb') as model_file:
    model = load(model_file)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Handle form submission
        val1 = float(request.form["val1"])
        val2 = float(request.form["val2"])

        data = [[val1, val2]]
        prediction = model.predict(data)[0]
       #pred_value = prediction 
    else:
        # Handle initial GET request
        prediction = None

    # Render the template with the prediction result (or None if GET request)
    return render_template("index.html", prediction=prediction)


if __name__ == "__main__":
    # Use the port provided by Render, or default to 5000
    port = int(os.environ.get("PORT", 5000))
    # Set host to 0.0.0.0 to be accessible externally
    app.run(host="0.0.0.0", port=port, debug=True)