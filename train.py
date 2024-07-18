import numpy as np
import pandas as pd
from commons.constants import GCS_BUCKET
from ultralytics import YOLO
from commons.constants import PWD
import torch
import os
import shutil
import requests

panel_model = YOLO('/Users/rokokkula/Documents/Panel_Damage_Detection/models/panel_best.pt')
dmg_model = YOLO('/Users/rokokkula/Documents/Panel_Damage_Detection/models/dmg_best.pt')


def predict(link):
    model.predict(link,
                  save=True, conf=0.9, project="test_output/panel")
    dmg_model.predict(link,
                      save=True, conf=0.1, project="test_output/dmg")


def download_image(image_url, local_file_path):
    # Send a GET request to the image URL
    response = requests.get(image_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Open a local file in binary write mode
        with open(local_file_path, 'wb') as file:
            # Write the content of the response to the file
            file.write(response.content)
        print(f"Image successfully downloaded to {local_file_path}")
    else:
        print("Failed to download image")


def predict_trial(link, panel_model, dmg_model):
    predict_dir_path_panel = f'{PWD}/helloflask/test_output/panel'
    predict_dir_path_dmg = f'{PWD}/helloflask/test_output/dmg'

    # Check if the predict directory exists
    if os.path.exists(predict_dir_path_panel):
        shutil.rmtree(predict_dir_path_panel)
    if os.path.exists(predict_dir_path_dmg):
        shutil.rmtree(predict_dir_path_dmg)

    # Proceed with the prediction
    panel_model.predict(link, save=True, conf=0.3, project="test_output/panel")
    dmg_model.predict(link, save=True, conf=0.3, project="test_output/dmg")

