from flask import Flask, request, render_template_string, jsonify, redirect , url_for
import json

app = Flask(__name__)

html_form = ""

with open('index.html', 'r') as html_file:
    for each_line in html_file.readlines():
        html_form += str(each_line)

# Function to format JSON
def format_json(input_data):
    try:
        data = json.loads(input_data)
        formatted_json = json.dumps(data, indent=4)
        return formatted_json
    except json.JSONDecodeError as e:
        return f"Error: {str(e)}"

# Route for the homepage
@app.route("/", methods=["GET"])
def index():
    return render_template_string(html_form)

# Route to handle JSON formatting
@app.route("/format", methods=["POST"])
def format():
    input_type = request.form.get("input_type")
    if input_type == "text": 
        json_text = request.form.get("json_text")
    else:
        json_file = request.files.get("json_file")
        json_text = json_file.read().decode("utf-8")

    original_json = json_text[:]
    formatted_json = format_json(json_text)
    return render_template_string(html_form, original_json=original_json, formatted_json=formatted_json)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
