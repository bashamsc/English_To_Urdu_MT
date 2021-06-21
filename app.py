#importing libraries

import io
import os

import numpy as np

import json

import flask

import pandas as pd

from flask import Flask, render_template, flash, redirect, request, session, logging, url_for, jsonify, make_response

from flask_restful import Api, Resource

from flask_cors import CORS


import transformers

from transformers import MarianTokenizer, MarianMTModel

app = Flask(__name__)

api = Api(app)

Cors = CORS(app)


app.config['SECRET_KEY'] = '!9m@S-dThyIlW[pHQbN^'

#model = joblib.load('./models/MarianMTModel.pkl')

@app.route('/')
def home():

    return render_template('index.html')


@app.route('/translate-text', methods=['POST'])
def translate_text():
    
    data = request.get_json()
    #pdb.set_trace()
    text_input = data['text']
    model_name = 'Helsinki-NLP/opus-mt-en-ur'
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    translated = model.generate(**tokenizer.prepare_seq2seq_batch(text_input, return_tensors="pt"))
    tgt_text = [tokenizer.decode(t, skip_special_tokens=True) for t in translated]
    #pdb.set_trace()
    return jsonify(tgt_text)
   

if __name__ == '__main__':
    
   
    app.run(debug=False)