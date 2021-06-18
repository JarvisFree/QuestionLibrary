#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    ：2021/1/13 19:33
@Author  ：维斯
@File    ：input_server.py
@Version ：1.0
@Function：题库录入服务
"""

import time
import random
from common.jar_project_util import JarProjectUtil
from model.dao.db import DB
import xlrd


class InputServer:
    def check_repeat(self, text: str):
        """
        校验数据中是否有此text信息（题目）
        :param text: 题目
        :return True/False 有/无
        """
        pass

    @staticmethod
    def add_question_by_excel(file):
        """
        添加题目到数据库中
        :param file:
        """
        start_row_data = 1  # 第n行开始 为正式数据（从0开始）
        wd = xlrd.open_workbook(file)
        st = wd.sheet_by_index(0)
        row_count = st.nrows
        col_count = st.ncols

        # 开始读取数据
        all_data = []
        for i in range(row_count):
            # row_id规则：‘TITLE’+13位时间戳+5位随机数
            row_id = 'TITLE' + str(int(round(time.time() * 1000))) + str(random.randint(0, 10000)).zfill(5)
            row_data = tuple(st.row_values(i + start_row_data))
            data = row_id + row_data
            all_data.append(data)

        # 写入数据库
        DB().add_homework_info(all_data).close()


if __name__ == '__main__':
    InputServer().add_question_by_excel(JarProjectUtil().project_root_path() + 'data/题目录入数据.xlsx')
