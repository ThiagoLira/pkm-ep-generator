from flask_cors import CORS
from flask import Flask,jsonify,request
import tensorflow as tf
import gpt_2_simple as gpt2
import gc
import re


app = Flask(__name__)
CORS(app)
app.debug = True





@app.route('/mock')
def mock_generate():
    callback = request.args.get('callback')

    data = {
        'sample_text' : "woewe oweo wewoewoewoeowew we  \n eweiweuwiiwiwiwiwiwiwi \n " 
    }

    return '{0}({1})'.format(callback,data)

@app.route('/',methods=['GET'])
def generate():

     
    sess = gpt2.start_tf_sess(threads=1)
    gpt2.load_gpt2(sess)

    callback = request.args.get('callback')
    sample = request.args.get('sample')

    if (not sample):
        sample = "Pikachu and Ash were"

    
    samples = gpt2.generate(sess,prefix =sample,return_as_list=True,length=256)


    lst = re.split('\.',samples[0])
   # remove last incomplete sentence (denoted by a period)
    generated_text = '.'.join(lst[:-1]) + "."

    data = {
        'sample_text' : generated_text
    }



    gc.collect()


    return '{0}({1})'.format(callback,data)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
