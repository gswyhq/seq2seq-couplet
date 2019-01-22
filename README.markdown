
这是一个项目使用seq2seq模型来对对联。这个项目是用Tensorflow编写的。


**注意：如果您使用自己的数据集，则需要在vocabs文件中添加<s>并<\s>作为前两行。**

# 训练：
打开`couplet.py`并配置文件位置和`hyperparams`。然后跑去`python3 couplet.py`训练模型。
你可以在Tensorbloard看到训练损失和蓝色分数。
当您发现损失停止减少时，您可能需要重新配置`learning_rate`

如果你停止训练并想继续训练它。您可以设置`restore_model`为`True`和使用的`m.train(<epoches>, start=<start>)`，这start是你已经运行的步骤。

[训练数据](https://github.com/wb14123/couplet-dataset)

# 运行训练的模型
打开`server.py`并配置`vocab_file`和`model_dirparams`。然后运行`python3 server.py`将启动可以播放联接的Web服务。


Examples
--------
```shell
docker build -t  gswyhq:couplet -f Dockerfile .

docker run --rm -it -p 5000:5000 gswyhq/couplet python3 server.py

curl -XPOST http://127.0.0.1:5000/chat/couplet -d '{"question": "举头望明月"}' -H "Content-Type:application/json"

# 或者浏览器打开：
http://127.0.0.1:5000/chat/couplet?question=举头望明月

http://127.0.0.1:5000/chat/couplet/举头望明月
```