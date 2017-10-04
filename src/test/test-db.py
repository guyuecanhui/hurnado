# coding:utf-8
__author__ = 'cheng.hu'

import hashlib
from hurnado.app.db.postgres import *


def testusers():
    delete_users("Calvin")
    insert_users(["Calvin", "Huawei123", "hiHuawei"])
    print select_users("Calvin")
    update_users(["Calvin", "guyuecanhui"])
    print select_users("Calvin")


def testpostgres():
    delete("users", "Calvin")
    insert("users", ["Calvin", hashlib.md5("Huawei123").hexdigest(), "hiHuawei"])
    print select("users", "Calvin")
    update("users", ["Calvin", "guyuecanhui"])
    print select("users", "Calvin")


def testsql():
    conn, cur = connect()
    sql = 'select * from users'
    cur.execute(sql)
    rows = cur.fetchall()
    print rows
    close(conn, cur)

if __name__ == "__main__":
    # testusers()
    # testpostgres()
    testsql()