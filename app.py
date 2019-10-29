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
        'sample_text' : "this was a test" 
    }

    return '{0}({1})'.format(callback,data)

@app.route('/',methods=['GET'])
def generate():

    # Since Flask forks the python process to answer for requests
    # we need to do this to avoid errors with tensorflow
    tf.reset_default_graph()


    # Start tf session and load model into memory
    sess = gpt2.start_tf_sess(threads=1)
    gpt2.load_gpt2(sess)

    # Get our params from the GET request
    callback = request.args.get('callback')
    sample = request.args.get('sample')

    # If the user was to lazy to input something we just feed the model with a default
    if (not sample):
        sample = "Pikachu and Ash were"

    samples = gpt2.generate(sess,prefix =sample,return_as_list=True,length=256)


    # The model will generated a fixed amount of words
    # Let's just throw away everything that is not a complete sentence
    lst = re.split('\.',samples[0])
    # Remove last incomplete sentence (denoted by a period)
    generated_text = '.'.join(lst[:-1]) + "."

    # Our return data
    data = {
        'sample_text' : generated_text
    }


    # Garbage collect since memory doesn't grow on trees
    gc.collect()


    return '{0}({1})'.format(callback,data)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
