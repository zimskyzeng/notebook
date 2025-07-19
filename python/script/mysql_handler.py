#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import os
import time
import traceback

import pymysql

logging.basicConfig(
    level=logging.WARN,
    format="[%(asctime)s] [%(levelname)s] [%(filename)s] [line:%(lineno)d] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


def enable_reconnect(func):
    def wrapper(cls, *args, **kwargs):
        try:
            # 本身pymysql.connection.ping()具备断线重连功能
            cls.connection.ping()
        except Exception as e:
            cls.connection = pymysql.connect(
                host=cls.host,
                port=cls.port,
                user=cls.user,
                password=cls.password,
                database=cls.dbname,
            )
            logging.WARN("Warning: Connection reset and reconnect succ.")
        result = func(cls, *args, **kwargs)
        return result

    return wrapper


class MySQLHandler(object):
    def __init__(self, host, port, dbname, user, password) -> None:
        self.host = host
        self.port = int(port)
        self.dbname = dbname
        self.user = user
        self.password = password
        self.connection = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.dbname,
        )

    def __del__(self) -> None:
        if not hasattr(self, "connection"):
            return
        if self.connection:
            self.connection.close()

    @enable_reconnect
    def update(self, sql):
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            self.connection.commit()
            return 0
        except Exception as e:
            logging.ERROR(traceback.format_exc())
            return 1

    @enable_reconnect
    def query(self, sql):
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
        except Exception as e:
            logging.ERROR(traceback.format_exc())
            return None


if __name__ == "__main__":
    db = MySQLHandler(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        dbname=os.getenv("DB_DBNAME"),
    )
    db.connection.ping()
    time.sleep(20)
    ret = db.query("select * from billing_detail limit 3;")
    print(ret)
