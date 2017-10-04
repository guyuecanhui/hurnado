# coding:utf-8
__author__ = 'cheng.hu'

import hashlib
import sys
from base import BaseHandler
from hurnado.app.db.postgres import validate, insert

reload(sys)
sys.setdefaultencoding('utf-8')


def wrap(txt):
    return '<strong class="text-danger">' + txt + '</strong>'


class LoginHandler(BaseHandler):
    def get(self):
        self.render("login.html", status="")

    def post(self):
        username = self.get_argument("username")
        pwd = validate('users', username)
        if not pwd:
            self.render("login.html", status=wrap("username not exist"))
        else:
            password = self.get_argument("password")
            password = hashlib.md5(password).hexdigest()
            if password != pwd:
                self.render("login.html", status=wrap("wrong password"))
            else:
                self.set_secure_cookie("user", self.get_argument("username"))
                self.redirect("/index")


class RegisterHandler(BaseHandler):
    def get(self):
        self.render("register.html", status="")

    def post(self):
        username = self.get_argument("username")
        pwd = validate('users', username)
        if not pwd:
            password = self.get_argument("password")
            password = hashlib.md5(password).hexdigest()
            nickname = self.get_argument("nickname")
            insert('users', [username, password, nickname])
            self.set_secure_cookie("user", self.get_argument("username"))
            self.redirect("/index")
        else:
            self.render("register.html", status=wrap("username existed"))


class LogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie("user")
        self.redirect("/login")


class SettingHandler(BaseHandler):
    def get(self):
        self.write("set ni mei")