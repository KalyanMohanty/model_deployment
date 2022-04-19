# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 21:28:35 2022

@author: kalya_kl8c3da
"""

# import tensorflow as tf
# import keras
import os
from tensorflow.keras.models import load_model
def model_deployment():
    path = 'celebrity_face_model.h5'
    loadModel = load_model(path)
    loadModel.summary()

model_deployment()
# print(os.getcwd())


