#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/1/3

"""
    desc:pass
"""
from cgi import parse_qs, escape
import json
from handler import GuessIdiom

def application(environ, start_response):


    method = environ.get('REQUEST_METHOD', 'HEAD')
    if method == "HEAD":
        response_headers = [('Content-Type', 'application/json'),
                                ('Content-Length', str(len("")))]
        start_response('200 OK', response_headers)
        return ""
    else:
        try:
            request_body_size = int(environ.get('CONTENT_LENGTH', 0))
        except(ValueError):
            request_body_size = 0
        request_body = environ['wsgi.input'].read(request_body_size).decode('utf-8')
        print('request_body = %s\n' % request_body)
        if not request_body:
            return ['未获取到请求数据']

        bot = GuessIdiom(request_body)
        #添加错误回调方法
        bot.set_callback(callback)

        #验证签名enableVerifyRequestSign  disableVerifyRequestSign 关闭验证签名
        # bot.initCertificate(environ).enableVerifyRequestSign()
        # bot.initCertificate(environ).disableVerifyRequestSign()

        body_str = bot.run()

        body = body_str.encode('utf-8')

        response_headers = [('Content-Type', 'application/json'),
                            ('Content-Length', str(len(body)))]
        status = '200 OK'

        start_response(status, response_headers)

        return [body]


def callback(data):
    print(data)


# from handler import GuessIdiom
#
# def application(method, data):
#
#     if method == "HEAD":
#         response_headers = [('Content-Type', 'application/json'),
#                                 ('Content-Length', str(len("")))]
#         # start_response('200 OK', response_headers)
#         return "", '200 OK', response_headers
#     else:
#         request_body = data
#         print('request_body = %s\n' % request_body)
#         if not request_body:
#             return ['未获取到请求数据']
#
#         bot = GuessIdiom(request_body)
#         #添加错误回调方法
#         bot.set_callback(callback)
#
#         #验证签名enableVerifyRequestSign  disableVerifyRequestSign 关闭验证签名
#         # bot.initCertificate(environ).enableVerifyRequestSign()
#         # bot.initCertificate(environ).disableVerifyRequestSign()
#
#         body_str = bot.run()
#
#         body = body_str.encode('utf-8')
#
#         response_headers = [('Content-Type', 'application/json'),
#                             ('Content-Length', str(len(body)))]
#         status = '200 OK'
#
#         return [body], status, response_headers
#
#
# def callback(data):
#     print(data)
