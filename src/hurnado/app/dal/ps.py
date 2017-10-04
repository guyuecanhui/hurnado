# coding:utf-8
__author__ = 'cheng.hu'

import psycopg2


def connect():
    conn = psycopg2.connect(database="CalvinHu",
                            host="127.0.0.1",
                            port="5432")
    return conn, conn.cursor()


def close(conn, cur):
    conn.commit()
    cur.close()
    conn.close()


def wrap(arr):
    if type(arr) == list:
        return ["'"+str(a)+"'" for a in arr]
    return "'"+str(arr)+"'"
