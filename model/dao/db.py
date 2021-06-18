#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    ：2021/1/14 17:23
@Author  ：维斯
@File    ：db.py
@Version ：1.0
@Function：数据库相关操作
"""

from typing import List
from common.jar_project_util import JarProjectUtil
import sqlite3


class DB:
    def __init__(self):
        self.conn = sqlite3.connect(JarProjectUtil().project_root_path() + 'data/db.db')
        self.cur = self.conn.cursor()

    def create_db(self):
        create_sql = [
            # 创建学科基本信息表
            'CREATE TABLE subject_info(subject_id TEXT, subject_name TEXT)',
            # 创建题目类型基本信息表
            'CREATE TABLE homework_type_info(homework_type_id TEXT, homework_type_name TEXT)',
            # 创建题目基本信息表
            'CREATE TABLE homework_info(id TEXT,subject_id TEXT,homework_type_id TEXT,homework_tile TEXT,true_an TEXT,all_an TEXT)'
        ]
        for i in create_sql:
            self.cur.execute(i)
        return self

    def add_subject_info(self, data: list):
        # 每个数据2个
        for i in data:
            if len(i) != 2:
                raise Exception()
        sql = 'INSERT INTO subject_info values(?,?)'
        self.cur.executemany(sql, data)
        self.conn.commit()
        return self

    def add_homework_type_info(self, data: list):
        # 每个数据2个
        for i in data:
            if len(i) != 2:
                raise Exception()
        sql = 'INSERT INTO homework_type_info values(?,?)'
        self.cur.executemany(sql, data)
        self.conn.commit()
        return self

    def add_homework_info(self, data: list):
        # 每个数据6个
        for i in data:
            if len(i) != 2:
                raise Exception()
        sql = 'INSERT INTO homework_info values(?,?,?,?,?,?)'
        self.cur.executemany(sql, data)
        self.conn.commit()
        return self

    def close(self):
        self.cur.close()
        self.conn.close()


if __name__ == '__main__':
    # DB().create_db()
    subject_info_list = [('a1', 'a2')]
    DB().add_subject_info(subject_info_list)
