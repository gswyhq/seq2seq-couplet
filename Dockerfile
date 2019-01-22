FROM tensorflow/tensorflow:1.5.0-py3

ENV LANG C.UTF-8
ENV LANGUAGE C.UTF-8
ENV LC_ALL C.UTF-8

# RUN echo `python --version`

ENV MYDIR /couplet

WORKDIR $MYDIR

COPY . $MYDIR/

RUN pip3 install -r requirements.txt -i http://pypi.douban.com/simple --trusted-host=pypi.douban.com

#COPY docker-entrypoint.sh /usr/local/bin/

EXPOSE 5000

#ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["/bin/bash"]

# docker build -t gswyhq/couplet:latest -f Dockerfile .
# docker run --rm -it -p 5000:5000 gswyhq/couplet:latest python3 server.py

