import os
from flask import Flask, request, render_template
import train

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def my_form():
    if request.method == 'POST':
        text = request.form['text']
        processed_text = text.upper()
        return processed_text
    return render_template('template.html')



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
