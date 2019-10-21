from flask_cors import CORS
from flask import Flask,jsonify,request
import tensorflow as tf
import gpt_2_simple as gpt2
import gc
import re


app = Flask(__name__)
CORS(app)




# @app.before_first_request
# def before_first_request_func():
    # generate_count = 0
# 
    # sess = gpt2.start_tf_sess(threads=1)
    # gpt2.load_gpt2(sess)

    # graph = tf.get_default_graph()


@app.route('/mock')
def mock_generate():
    callback = request.args.get('callback')

    data = {
        'sample_text' : "woewe oweo wewoewoewoeowew we  \n eweiweuwiiwiwiwiwiwiwi \n " 
    }

    return '{0}({1})'.format(callback,data)

@app.route('/',methods=['GET'])
def generate():

    # global generate_count
    # global sess
    # global graph

    generate_count = 0

    sess = gpt2.start_tf_sess(threads=1)
    gpt2.load_gpt2(sess)

    graph = tf.get_default_graph()


    callback = request.args.get('callback')
    sample = request.args.get('sample')

    if (not sample):
        sample = "Pikachu and Ash"


    with graph.as_default():
        samples = gpt2.generate(sess,prefix =sample,return_as_list=True,length=256)


        lst = re.split('\.',samples[0])
       # remove last incomplete sentence (denoted by a period)
        generated_text = '.'.join(lst[:-1]) + "."

        data = {
            'sample_text' : generated_text
        }



        generate_count += 1

        if generate_count == 8:
            # Reload model to prevent Graph/Session from going OOM
            tf.reset_default_graph()
            sess.close()
            sess = gpt2.start_tf_sess(threads=1)
            gpt2.load_gpt2(sess)
            graph = tf.get_default_graph()
            generate_count = 0

        gc.collect()


        return '{0}({1})'.format(callback,data)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
