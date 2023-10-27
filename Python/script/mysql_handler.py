#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql
import traceback


def enable_reconnect(func):
    def wrapper(cls, *args, **kwargs):
        try:
            cls.connection.ping()
        except Exception as e:
            cls.connection = pymysql.connect(
                host=cls.host, port=cls.port, user=cls.user, password=cls.password, database=cls.dbname
            )
        result = func(cls, *args, **kwargs)
        return result

    return wrapper


class MySQLHandler(object):
    def __init__(self, host, port, dbname, user, password) -> None:
        self.host = host
        self.port = port
        self.dbname = dbname
        self.user = user
        self.password = password
        self.conntion = pymysql.connect(
            host=self.host, port=self.port, user=self.user, password=self.password, database=self.dbname
        )

    def __del__(self) -> None:
        if not hasattr(self, "connection"):
            return
        if self.conntion:
            self.conntion.close()

    @enable_reconnect
    def update(self, sql):
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            self.conntion.commit()
            return 0
        except Exception as e:
            print(traceback.format_exc())
            return 1

    @enable_reconnect
    def query(self, sql):
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
        except Exception as e:
            print(traceback.format_exc())
            return None
