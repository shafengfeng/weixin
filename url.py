#-*-coding:utf-8-*-
__author__ = 'shafengfeng'

import os
from wx import *

settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    cookie_secret="61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o",
    debug=False
)
url_list = [
    (r"/", wx),

]