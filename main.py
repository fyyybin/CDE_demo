# -*- coding: UTF-8 -*-
"""
时间2020-12-14 19：00
"""
import pandas as pd
import os
import json
from openpyxl import Workbook, load_workbook

def No_fill(t):
    if t == None:
        return '暂无'
    else:
        return t
def main():
    filePath = "D:\\Git\\CDE_demo\\data3\\"
    file_list = os.listdir(filePath)
    print(file_list)
    for file in file_list:
        path = "D:\\Git\\CDE_demo\\data3\\" + file
        wb = load_workbook(path, data_only=True)
        ws = wb[wb.sheetnames[0]]

        rows = ws.max_row#总行数
        columns = ws.max_column#总列数
        print(file)


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

        for i in range(22, rows):
            if ws.cell(row=i, column=1).value == '1、试验目的':
                documents['试验目的'] = ws.cell(row=i+1, column=1).value.replace(' ', '')
            elif ws.cell(row=i, column=1).value == '试验分类':
                documents['试验分类'] = No_fill(ws.cell(row=i, column=2).value)
            elif ws.cell(row=i, column=1).value == '试验分期':
                documents['试验分期'] = No_fill(ws.cell(row=i, column=2).value)
            elif ws.cell(row=i, column=1).value == '设计类型':
                documents['设计类型'] = No_fill(ws.cell(row=i, column=2).value)
            elif ws.cell(row=i, column=1).value == '随机法':
                documents['随机法'] = No_fill(ws.cell(row=i, column=2).value)
            elif ws.cell(row=i, column=1).value == '盲法':
                documents['盲法'] = No_fill(ws.cell(row=i, column=2).value)
            elif ws.cell(row=i, column=1).value == '试验范围':
                documents['试验范围'] = No_fill(ws.cell(row=i, column=2).value)
                key_1 = i #受试者开始的标签
            if ws.cell(row=i, column=1).value == '4、试验分组':
                key_2 = i+1  # 受试者结束的标签
            if ws.cell(row=i, column=1).value == '5、终点指标':
                key_3 = i+1  # 试验分组结束的标签
        mess_man = {}
        state =  []
        #下面是受试者信息字典(key_1, key_2)
        for i in range(key_1, key_2):
            if ws.cell(row=i, column=1).value == '年龄':
                mess_man['年龄'] = ws.cell(row=i+1, column=1).value.replace(' ', '')
            elif ws.cell(row=i, column=1).value == '性别':
                mess_man['性别'] = ws.cell(row=i+1, column=2).value.replace(' ', '')
            elif ws.cell(row=i, column=1).value == '健康受试者':
                mess_man['健康受试者'] = ws.cell(row=i + 1, column=2).value.replace(' ', '')
            if ws.cell(row=i, column=1).value == '入选标准':
                for j in range(i, key_2):
                    state.append(ws.cell(row=j, column=2).value.replace(' ', ''))
                    if ws.cell(row=j+1, column=1).value == '排除标准':
                        mess_man['入选标准'] = state
                        state = []
                        break
            elif ws.cell(row=i, column=1).value == '排除标准':
                for j in range(i, key_2):
                    state.append(ws.cell(row=j, column=2).value.replace('\xa0', ''))
                    if ws.cell(row=j+1, column=1).value == '4、试验分组':
                        mess_man['排除标准'] = state
                        state = []
                        documents['受试者信息'] = mess_man
                        break
        #下面是试验分组(key_2-1， key_3)
        mess = {}
        mess_number, mess_test = {}, {}
        for i in range(key_2-1, key_3):
            if ws.cell(row=i, column=2).value == '序号':
                n_1 = i
                for j in range(n_1, key_3):
                    if ws.cell(row=j, column=2).value == '序号':
                        n_2 = i+1

        for x in range(n_1-1, n_2):
            if ws.cell(row=x, column=2).value != '序号':
                mess_test['名称'] = ws.cell(row=x, column=4).value.replace('中文通用名', '').replace('：','')
                mess_test['用法'] = ws.cell(row=x, column=5).value.replace('用法用量：', '')
                mess_number[ws.cell(row=x, column=2).value] = mess_test
        mess['试验药'] = mess_test

        for x in range(n_2, key_3-1):
            if ws.cell(row=x, column=2).value != '序号':
                mess_test['名称'] = ws.cell(row=x, column=4).value.replace('中文通用名', '').replace('：','')
                mess_test['用法'] = ws.cell(row=x, column=5).value.replace('用法用量：', '')
                mess_number[ws.cell(row=x, column=2).value] = mess_test
        mess['对照药'] = mess_test
        documents['试验分组'] = mess

        print('-----------------------------------------------------------')
        savefile(documents)

def savefile(dic):
    with open('1.json', 'w', encoding='utf-8') as f:
        json_str = json.dumps(dic, indent=4, ensure_ascii=False)
        f.write(json_str)

main()