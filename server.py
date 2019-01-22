
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from model import Model
from gevent.pywsgi import WSGIServer
import logging

app = Flask(__name__)
CORS(app)

vocab_file = './couplet/vocabs'
model_dir = './models/tf-lib/output_couplet'

m = Model(
        None, None, None, None, vocab_file,
        num_units=1024, layers=4, dropout=0.2,
        batch_size=32, learning_rate=0.0001,
        output_dir=model_dir,
        restore_model=True, init_train=False, init_infer=True)


@app.route('/chat/couplet/<in_str>')
def chat_couplet(in_str):
    try:
        assert len(in_str) != 0, '输入的句子长度不能为空！'
        assert len(in_str) <= 50, '您的输入太长了'
        output = m.infer(' '.join(in_str))
        output = ''.join(output.split(' '))
        print('上联：%s；下联：%s' % (in_str, output))
        return jsonify({"上联": in_str, "下联": output, 'code': 0})
    except Exception as e:
        print('系统错误，{}'.format(e))
        ret = {
            "code": 1,
            "msg": str(e)
        }
        return jsonify(ret)

@app.route('/chat/couplet', methods=['GET', 'POST'])
def chat_couplet2():
    try:
        if request.method == 'POST':
            content_type = request.headers.get('Content-Type', '')
            assert content_type.lower() == 'application/json', 'POST请求时，`Content-Type`应该为：`application/json`, 不应该为：`{}`'.format(content_type)
            question = request.json.get('question', '')
        else:
            question = request.args.get('question', '')

        assert len(question) != 0, '输入的句子长度不能为空！'
        assert len(question) <= 50, '您的输入太长了'
        output = m.infer(' '.join(question))
        output = ''.join(output.split(' '))
        answer = output
        return jsonify({"上联": question, "下联": answer, 'code': 0})
    except Exception as e:
        print('系统错误： {}'.format(e))
        result = {
            "code": 1,
            "msg": str(e)
        }
        return jsonify(result)

app.config['JSON_AS_ASCII'] = False
http_server = WSGIServer(('', 5000), app)
http_server.serve_forever()
