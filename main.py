# encoding: utf-8
from conf.config import SERVICE_PORT
from gevent import pywsgi
from conf import *
from app import app


if __name__ == '__main__':
    server = pywsgi.WSGIServer(('0.0.0.0', SERVICE_PORT), app)
    server.serve_forever()
