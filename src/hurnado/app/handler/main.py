# coding:utf-8
__author__ = 'cheng.hu'

import tornado.web
import sys
from base import BaseHandler
from hurnado.app.db.postgres import select

reload(sys)
sys.setdefaultencoding('utf-8')


class IndexHandler(BaseHandler):
    '''
    处理首页
    '''

    @tornado.web.authenticated
    def get(self):
        name = tornado.escape.xhtml_escape(self.current_user)
        nickname = select('users', name)
        inner = self.render_string("main/dashboard.htm")
        main = self.render_string("main.html",
                                  nickname=nickname,
                                  nickname_logo='img/avatars/' + nickname[0].upper() + '.png',
                                  inner_html=inner)
        main = main.replace("accordion-toggle b_F79999", "accordion-toggle b_F79999 active")
        self.write(main)


class AnalyticsHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        name = tornado.escape.xhtml_escape(self.current_user)
        nickname = select('users', name)
        inner = self.render_string("main/analytics.htm")
        main = self.render_string("main.html",
                                  nickname=nickname,
                                  nickname_logo='img/avatars/' + nickname[0].upper() + '.png',
                                  inner_html=inner)
        main = main.replace("accordion-toggle b_C1F8A9", "accordion-toggle b_C1F8A9 active")
        self.write(main)


class UsersHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        name = tornado.escape.xhtml_escape(self.current_user)
        nickname = select('users', name)
        inner = self.render_string("main/users.htm")
        main = self.render_string("main.html",
                                  nickname=nickname,
                                  nickname_logo='img/avatars/' + nickname[0].upper() + '.png',
                                  inner_html=inner)
        main = main.replace("accordion-toggle b_F5C294", "accordion-toggle b_F5C294 active")
        self.write(main)


class TasksHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        name = tornado.escape.xhtml_escape(self.current_user)
        nickname = select('users', name)
        inner = self.render_string("main/tasks.htm")
        main = self.render_string("main.html",
                                  nickname=nickname,
                                  nickname_logo='img/avatars/' + nickname[0].upper() + '.png',
                                  inner_html=inner)
        main = main.replace("accordion-toggle b_F6F1A2", "accordion-toggle b_F6F1A2 active")
        self.write(main)


class ButtonsHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        name = tornado.escape.xhtml_escape(self.current_user)
        nickname = select('users', name)
        inner = self.render_string("main/buttons.htm")
        main = self.render_string("main.html",
                                  nickname=nickname,
                                  nickname_logo='img/avatars/' + nickname[0].upper() + '.png',
                                  inner_html=inner)
        main = main.replace('" href="buttons', ' active" href="buttons')\
                   .replace("b_C3F7A7 collapsed", "b_C3F7A7") \
                   .replace('collapse1" class="accordion-body collapse', 'collapse1" class="accordion-body in collapse')
        self.write(main)


class FeaturesHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        name = tornado.escape.xhtml_escape(self.current_user)
        nickname = select('users', name)
        inner = self.render_string("main/features.htm")
        main = self.render_string("main.html",
                                  nickname=nickname,
                                  nickname_logo='img/avatars/' + nickname[0].upper() + '.png',
                                  inner_html=inner)
        main = main.replace('" href="features', ' active" href="features')\
                   .replace("b_C3F7A7 collapsed", "b_C3F7A7") \
                   .replace('collapse1" class="accordion-body collapse', 'collapse1" class="accordion-body in collapse')
        self.write(main)


class FormsHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        name = tornado.escape.xhtml_escape(self.current_user)
        nickname = select('users', name)
        inner = self.render_string("main/forms.htm")
        main = self.render_string("main.html",
                                  nickname=nickname,
                                  nickname_logo='img/avatars/' + nickname[0].upper() + '.png',
                                  inner_html=inner)
        main = main.replace('" href="forms', ' active" href="forms')\
                   .replace("b_C3F7A7 collapsed", "b_C3F7A7") \
                   .replace('collapse1" class="accordion-body collapse', 'collapse1" class="accordion-body in collapse')
        self.write(main)


class TicketsHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        name = tornado.escape.xhtml_escape(self.current_user)
        nickname = select('users', name)
        inner = self.render_string("main/tickets.htm")
        main = self.render_string("main.html",
                                  nickname=nickname,
                                  nickname_logo='img/avatars/' + nickname[0].upper() + '.png',
                                  inner_html=inner)
        main = main.replace('" href="tickets', ' active" href="tickets')
        self.write(main)


class TablesHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        name = tornado.escape.xhtml_escape(self.current_user)
        nickname = select('users', name)
        inner = self.render_string("main/tables.htm")
        main = self.render_string("main.html",
                                  nickname=nickname,
                                  nickname_logo='img/avatars/' + nickname[0].upper() + '.png',
                                  inner_html=inner)
        main = main.replace('" href="tables', ' active" href="tables')\
                   .replace("b_C3F7A7 collapsed", "b_C3F7A7") \
                   .replace('collapse1" class="accordion-body collapse', 'collapse1" class="accordion-body in collapse')
        self.write(main)


class CalendarHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        name = tornado.escape.xhtml_escape(self.current_user)
        nickname = select('users', name)
        inner = self.render_string("main/calendar.htm")
        main = self.render_string("main.html",
                                  nickname=nickname,
                                  nickname_logo='img/avatars/' + nickname[0].upper() + '.png',
                                  inner_html=inner)
        main = main.replace('" href="calendar', ' active" href="calendar')\
                   .replace("b_9FDDF6 collapsed", "b_9FDDF6")\
                   .replace('collapse2" class="accordion-body collapse', 'collapse2" class="accordion-body in collapse')
        self.write(main)


class GalleryHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        name = tornado.escape.xhtml_escape(self.current_user)
        nickname = select('users', name)
        inner = self.render_string("main/gallery.htm")
        main = self.render_string("main.html",
                                  nickname=nickname,
                                  nickname_logo='img/avatars/' + nickname[0].upper() + '.png',
                                  inner_html=inner)
        main = main.replace('" href="gallery', ' active" href="gallery')\
                   .replace("b_9FDDF6 collapsed", "b_9FDDF6")\
                   .replace('collapse2" class="accordion-body collapse', 'collapse2" class="accordion-body in collapse')
        self.write(main)


class NotificationsHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        name = tornado.escape.xhtml_escape(self.current_user)
        nickname = select('users', name)
        inner = self.render_string("main/notifications.htm")
        main = self.render_string("main.html",
                                  nickname=nickname,
                                  nickname_logo='img/avatars/' + nickname[0].upper() + '.png',
                                  inner_html=inner)
        main = main.replace('" href="notifications', ' active" href="notifications')\
                   .replace("b_9FDDF6 collapsed", "b_9FDDF6")\
                   .replace('collapse2" class="accordion-body collapse', 'collapse2" class="accordion-body in collapse')
        self.write(main)
