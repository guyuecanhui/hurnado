# coding:utf-8
__author__ = 'cheng.hu'

import hurnado.app.handler.account as account
import hurnado.app.handler.main as main
import hurnado.app.handler.base as base


url = [
    (r'/index', main.IndexHandler),                 # 首页
    (r'/analytics', main.AnalyticsHandler),         # 数据分析页面
    (r'/buttons', main.ButtonsHandler),             # 任务统计页面
    (r'/calendar', main.CalendarHandler),           # 任务统计页面
    (r'/features', main.FeaturesHandler),           # 任务统计页面
    (r'/forms', main.FormsHandler),                 # 任务统计页面
    (r'/gallery', main.GalleryHandler),             # 任务统计页面
    (r'/notifications', main.NotificationsHandler), # 通知页面
    (r'/tables', main.TablesHandler),               # 表格页面
    (r'/tasks', main.TasksHandler),                 # 任务统计页面
    (r'/tickets', main.TicketsHandler),             # 投票页面
    (r'/users', main.UsersHandler),                 # 用户统计页面

    (r'/login', account.LoginHandler),              # 登录页面
    (r'/logout', account.LogoutHandler),            # 登出处理
    (r'/register', account.RegisterHandler),        # 注册页面
    (r'/setting', account.SettingHandler),          # 用户设置页面

    (r'/test', base.TestHandler),  # 测试页面
    ('.*', base.BaseHandler),                       # 默认页面
]
