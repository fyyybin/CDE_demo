# -*- coding: UTF-8 -*-
"""
时间2020-12-14 19：00
"""
import pandas as pd
import os
import xlrd
from openpyxl import Workbook, load_workbook

def No_fill(t):
    if t == None:
        return '暂无'
    else:
        return t
filePath = 'D:\\demo\\NEW demo\\CDE_demo\\data\\'
file_list = os.listdir(filePath)
print(file_list)
for file in file_list:
    path = 'D:\\demo\\NEW demo\\CDE_demo\\data\\' + file
    wb = load_workbook(path, data_only=True)
    ws = wb[wb.sheetnames[0]]
    documents = {}
    documents['登记号'] = ws['B1'].value.replace(' ','')
    documents['药物名称'] = ws['B7'].value.replace(' ','')
    documents['药物类型'] = No_fill(ws['B8'].value)
    documents['适应症'] = ws['B10'].value.replace(' ','')
    documents['试验专业题目'] = ws['B11'].value.replace(' ','')
    documents['试验通俗题目'] = ws['B12'].value.replace(' ','')

    documents['联系人姓名'] = No_fill(ws['B19'].value)
    documents['联系人座机'] = No_fill(ws['D19'].value)
    documents['联系人手机'] = No_fill(ws['B20'].value)
    documents['联系人Email'] = No_fill(ws['D20'].value)
    documents['联系人邮政地址'] = No_fill(ws['B21'].value)
    documents['联系人邮编'] = No_fill(ws['D21'].value)

    print(documents)

    print('-------------------------------------------')