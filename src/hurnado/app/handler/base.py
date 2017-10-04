# coding:utf-8
__author__ = 'cheng.hu'

import tornado.web

import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class BaseHandler(tornado.web.RequestHandler):
    '''
    基本处理类
    '''
    def get_current_user(self):
        return self.get_secure_cookie("user")


    def get(self):
        self.render("404.html")


class TestHandler(BaseHandler):
    '''
    处理测试页
    '''
    @tornado.web.authenticated
    def get(self):
        name = tornado.escape.xhtml_escape(self.current_user)
        lst = [name, "www.huawei.com", "guyuecanhui@gmail.com"]
        self.render("test.html", info=lst)
