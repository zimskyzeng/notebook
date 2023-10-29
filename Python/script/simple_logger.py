#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

logging.basicConfig(
    # 设定打印日志的级别
    level=logging.INFO,
    # 日志消息格式，level=日志级别 format=日志格式 asctime=对应下面的datefmt filename=日志文件路径
    format="[%(asctime)s] [%(levelname)s] [%(filename)s] [line:%(lineno)d] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    # 开启文件日志，需启用filename字段
    # filename="1.log",
    # 设置文件写入模式，需启用filename字段，a=追加 w=覆盖
    # filemode="a",
)

if __name__ == "__main__":
    logging.error("error")
    logging.info("info")
