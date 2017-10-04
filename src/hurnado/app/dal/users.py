# coding:utf-8
__author__ = 'cheng.hu'

import uuid
from ps import *


def select_users(username):
    username = wrap(username)
    conn, cur = connect()
    cur.execute("SELECT nickname FROM users WHERE username = " + username)
    rows = cur.fetchall()
    close(conn, cur)
    return None if not rows else rows[0][0]


def insert_users(args):
    username, password, nickname, uid = wrap([args[0], args[1], args[2], uuid.uuid1()])
    conn, cur = connect()
    sql = "INSERT INTO users (username, password, nickname, uid) \
            VALUES ({username}, {password}, {nickname}, {uid})"
    cur.execute(sql.format(username=username, password=password, nickname=nickname, uid=uid))
    close(conn, cur)


def delete_users(username):
    username = wrap(username)
    conn, cur = connect()
    cur.execute("DELETE FROM users WHERE username = " + username)
    close(conn, cur)


def update_users(args):
    username, nickname = wrap(args)
    conn, cur = connect()
    sql = "UPDATE users SET nickname = {nickname} where username = {username}"
    cur.execute(sql.format(nickname=nickname, username=username))
    close(conn, cur)


def validate_users(username):
    username = wrap(username)
    conn, cur = connect()
    cur.execute("SELECT password FROM users WHERE username = " + username)
    rows = cur.fetchall()
    close(conn, cur)
    return None if not rows else rows[0][0]
