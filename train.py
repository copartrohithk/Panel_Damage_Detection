import numpy as np
import pandas as pd

from ultralytics import YOLO
import torch

# Load a model
# model = YOLO("yolov8n.yaml")  # build a new model from scratch

# Use the model
# model.train(data="config.yaml", epochs=1,device="mps")  # train the model

model = YOLO('/Users/rokokkula/Documents/Panel_Damage_Detection/models/panel_best.pt')
dmg_model = YOLO('/Users/rokokkula/Documents/Panel_Damage_Detection/models/dmg_best.pt')


def predict(link):
    model.predict(link,
                  save=True, conf=0.9, project="test_output/panel")
    dmg_model.predict(link,
                      save=True, conf=0.1, project="test_output/dmg")

def output():
    x="/Users/rokokkula/Documents/Panel_Damage_Detection/test_output/dmg/predict/8fceef3db9824c4ba19ead5814eb7eb1_ful.jpg"
    y="/Users/rokokkula/Documents/Panel_Damage_Detection/test_output/panel/predict/8fceef3db9824c4ba19ead5814eb7eb1_ful.jpg"
    return x,y
