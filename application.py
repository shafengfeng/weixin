#-*-coding:utf-8-*-
__author__ = 'shafengfeng'

from tornado import web,httpserver,ioloop
from url import settings,url_list


application = web.Application(url_list,**settings)


if __name__ == '__main__':
    http_server = httpserver.HTTPServer(application)
    http_server.listen(80)
    ioloop.IOLoop.instance().start()

    # #多
    # http_server = httpserver.HTTPServer(application)
    # http_server.bind(9000)
    # http_server.start(num_processes=2)
    # ioloop.IOLoop.instance().start()