import os
from flask import Flask, request, render_template, send_file
import requests
from io import BytesIO
# Import model and predict_trial from train.py
from train import panel_model,dmg_model, predict_trial, download_image
from commons.constants import PWD
import shutil
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def my_form():
    static_image_path_panel = None    # Initialize image_path
    static_image_path_dmg=None
    input_image_url = None  # Initialize input_image_url
    if request.method == 'POST':
        input_image_url = request.form['text']  # Assuming the input name is 'text'
        response = requests.get(input_image_url)
        input_filename = "input_image.jpg"
        panel_filename = "panel_image.jpg"
        dmg_filename = "damage_image.jpg"
        local_file_path = os.path.join(PWD, 'helloflask', 'test_output', 'input_image', input_filename)
        if response.status_code == 200:
            download_image(input_image_url, local_file_path)
            predict_trial(local_file_path, panel_model,dmg_model)
            generated_image_path_panel = os.path.join('test_output', 'panel', 'predict', input_filename)
            generated_image_path_dmg = os.path.join('test_output', 'dmg', 'predict', input_filename)
            static_image_path_panel = os.path.join( 'static', panel_filename)
            static_image_path_dmg = os.path.join( 'static', dmg_filename)
            os.makedirs(os.path.dirname(static_image_path_panel), exist_ok=True)
            os.makedirs(os.path.dirname(static_image_path_dmg), exist_ok=True)
            shutil.copy(generated_image_path_panel, static_image_path_panel)
            shutil.copy(generated_image_path_dmg, static_image_path_dmg)
            static_image_path_panel = "panel_image.jpg"  # Corrected path for web access
            static_image_path_dmg = "damage_image.jpg"  # Corrected path for web access
        else:
            return "Failed to fetch image", 400
    return render_template('template.html', input_image_url=input_image_url
                           , panel_image_path=static_image_path_panel, damage_image_path=static_image_path_dmg)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
