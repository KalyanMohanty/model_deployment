# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 21:36:57 2022

@author: kalya_kl8c3da
"""

from flask import Flask, url_for, render_template
from flask import send_file
app2 = Flask(__name__)


@app2.route('/')
def home():
    return render_template('index.html')
@app2.route('/celebrity_face_model_h5')
def download__celebrity_face_model_h5():
    #For windows you need to use drive name [ex: F:/Example.pdf]
    path = "static/celebrity_face_model.h5"
    return send_file(path, as_attachment=True)

@app2.route('/celebrity_face_model_json')
def download__celebrity_face_model_json():
    #For windows you need to use drive name [ex: F:/Example.pdf]
    path = "static/celebrity_face_model.json"
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app2.run(port=5000,debug=True) 