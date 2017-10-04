# coding:utf-8
__author__ = 'cheng.hu'

from hurnado.app.dal.users import *
from hurnado.app.common.logger import logger


def select(table, args):
    try:
        rows = globals()['select_' + table](args)
    except:
        logger.info("select from table " + table + " failed", exc_info=True)
        return None
    else:
        logger.info("select from table " + table + " successful")
        return rows


def validate(table, args):
    try:
        rows = globals()['validate_' + table](args)
    except:
        logger.info("validate table " + table + " failed", exc_info=True)
        return None
    else:
        logger.info("validate table " + table + " successful")
        return rows


def update(table, args):
    try:
        globals()['update_' + table](args)
    except:
        logger.info("update table " + table + " failed", exc_info=True)
    else:
        logger.info("update table " + table + " successful")


def insert(table, args):
    try:
        globals()['insert_' + table](args)
    except:
        logger.info("insert into table " + table + " failed", exc_info=True)
    else:
        logger.info("insert into table " + table + " successful")


def delete(table, args):
    try:
        globals()['delete_' + table](args)
    except:
        logger.info("delete table " + table + " failed", exc_info=True)
    else:
        logger.info("delete table " + table + " successful")