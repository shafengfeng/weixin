#-*-coding:utf-8-*-
__author__ = 'shafengfeng'

from tornado import web
import json,urllib2,traceback,urllib
# from wechat_sdk import WechatBasic
# from wechat_sdk import messages
import xml.etree.ElementTree as ET
import time
import commands

class TulingAutoReply(object):
    def __init__(self,key='bec5c93dc087dcc863003b33bd1d781d',url='http://www.tuling123.com/openapi/api'):
        self.key=key
        self.url=url

    def replay(self,unicode_str):
        body = {'key':self.key,'info':unicode_str}
        data = urllib.urlencode(body)
        r = urllib2.urlopen(url=self.url,data=data)
        resp = r.read()
        if resp is None or len(resp) == 0:
            return None
        try:
            js = json.loads(resp)
            if js['code'] == 100000:
                return js['text'].replace(' ', '')
            elif js['code'] == 200000:
                return js['url']
            else:
                return None
        except Exception:
            traceback.print_exc()
            return None



# wechat = WechatBasic(token='wexfin',appid='wx3278e6e82b164619',appsecret='a6c6facf57c22f9c79305b56a8e82c27')


class wx(web.RequestHandler):

    # def wx_proc_msg(self, body):
    #     try:
    #         wechat.parse_data(body)
    #     except :
    #         print 'Invalid Body Text'
    #         return
    #     if isinstance(wechat.message,messages.TextMessage): # 消息为文本消息
    #         content = wechat.message.content
    #         reply = auto_reply.reply(content)
    #         if reply is not None:
    #             return wechat.response_text(content=reply)
    #         else:
    #             return wechat.response_text(content=u"不知道你说的什么")
    #     return wechat.response_text(content=u'知道了')

    def get(self):    ########验证时用
        signature = self.get_argument('signature')
        timestamp = self.get_argument('timestamp')
        nonce = self.get_argument('nonce')
        echostr = self.get_argument('echostr')
        self.write(echostr)


    def post(self, *args, **kwargs):
        body = self.request.body
        data = ET.fromstring(body)
        tousername = data.find('ToUserName').text
        fromusername = data.find('FromUserName').text
        createtime = data.find('CreateTime').text
        msgtype = data.find('MsgType').text
        content = data.find('Content').text
        msgid = data.find('MsgId').text
        print("context:",content)
        print(type(content).__name__)
        result = TulingAutoReply().replay(content.encode('utf-8'))


        textTpl = """<xml>
            <ToUserName><![CDATA[%s]]></ToUserName>
            <FromUserName><![CDATA[%s]]></FromUserName>
            <CreateTime>%s</CreateTime>
            <MsgType><![CDATA[%s]]></MsgType>
            <Content><![CDATA[%s]]></Content>
            </xml>"""
        out = textTpl % (fromusername, tousername, str(int(time.time())), msgtype, result)
        self.write(out)