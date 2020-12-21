# coding:utf-8
import rdflib
import json
import re
def create_rdf(dic):
    g = rdflib.Graph()
    for _list in dic:
        namespace = 'http://www.w3.org/'
        #namespace = ''
        # 实体
        number = rdflib.URIRef(namespace + _list['登记号'])

        # 关系
        rel_medicine_name = rdflib.URIRef(namespace + '药物名称')
        rel_medicine_type = rdflib.URIRef(namespace + '药物类型')
        rel_indication = rdflib.URIRef(namespace + '适应症')
        rel_majoy = rdflib.URIRef(namespace + '试验专业题目')
        rel_popular = rdflib.URIRef(namespace + '试验通俗题目')
        rel_contact_name = rdflib.URIRef(namespace + '联系人姓名')
        rel_contact_phone = rdflib.URIRef(namespace + '联系人座机')
        rel_address = rdflib.URIRef(namespace + '联系人邮政地址')
        rel_Postcode = rdflib.URIRef(namespace + '联系人邮编')
        rel_objective = rdflib.URIRef(namespace + '试验目的')

        namespace2 = namespace + '试验设计/'
        rel_Design = rdflib.URIRef(namespace + '试验设计')
        rel_Design1 = rdflib.URIRef(namespace2 + '试验分类')
        rel_Design2 = rdflib.URIRef(namespace2 + '试验分期')
        rel_Design3 = rdflib.URIRef(namespace2 + '设计类型')
        rel_Design4 = rdflib.URIRef(namespace2 + '盲法')
        rel_Design5 = rdflib.URIRef(namespace2 + '试验范围')

        namespace3 = namespace + '受试者信息/'
        rel_Subject_information = rdflib.URIRef(namespace3)
        rel_age = rdflib.URIRef(namespace3 + '年龄')
        rel_sex = rdflib.URIRef(namespace3 + '性别')
        rel_health = rdflib.URIRef(namespace3 + '健康受试者')
        rel_Inclusion_Criteria = rdflib.URIRef(namespace3 + '入选标准')
        rel_Exclusion_Criteria = rdflib.URIRef(namespace3 + '排除标准')

        rel_experimental_design = rdflib.URIRef(namespace + '试验分组')

        rel_Main_time = rdflib.URIRef(namespace + '主要终点指标及评价时间')
        rel_Secondary_time = rdflib.URIRef(namespace + '次要终点指标及评价时间')
        rel_safe = rdflib.URIRef(namespace + '数据安全监查委员会')
        rel_safe_buy = rdflib.URIRef(namespace + '为受试者购买试验伤害保险')
        rel_man_1 = rdflib.URIRef(namespace + '目标入组人数')
        rel_man_2 = rdflib.URIRef(namespace + '已入组人数')
        rel_man_3 = rdflib.URIRef(namespace + '实际入组总人数')
        rel_firstday_1 = rdflib.URIRef(namespace + '第一例受试者签署知情同意书日期')
        rel_firstday_2 = rdflib.URIRef(namespace + '第一例受试者入组日期')
        rel_firstday_3 = rdflib.URIRef(namespace + '试验完成日期')


        # 属性
        att_medicine_name = rdflib.URIRef(namespace + _list['药物名称'])
        att_medicine_type = rdflib.URIRef(namespace + _list['药物类型'])
        att_indication = rdflib.URIRef(namespace + _list['适应症'])
        att_majoy = rdflib.URIRef(namespace + _list['试验专业题目'])
        att_popular = rdflib.URIRef(namespace + _list['试验通俗题目'])
        att_contact_name = rdflib.URIRef(namespace + _list['联系人姓名'].replace(' ', '_'))
        if type(_list['联系人座机']) != type(_list['登记号']):
            att_contact_phone = rdflib.URIRef(namespace + str(_list['联系人座机']))
        else:
            att_contact_phone = rdflib.URIRef(namespace + _list['联系人座机'].replace('  ', ','))
        att_address = rdflib.URIRef(namespace + _list['联系人邮政地址'].replace(' ', ''))
        att_Postcode = rdflib.URIRef(namespace + str(_list['联系人邮编']))
        att_objective = rdflib.URIRef(namespace + _list['试验目的'].replace('<', '小于').replace('>', '大于'))

        att_Design = rdflib.URIRef(namespace + '试验设计')
        att_Design1 = rdflib.URIRef(namespace2 + _list['试验设计']['试验分类'].replace(' ', ''))
        att_Design2 = rdflib.URIRef(namespace2 + _list['试验设计']['试验分期'])
        att_Design3 = rdflib.URIRef(namespace2 + _list['试验设计']['设计类型'])
        att_Design4 = rdflib.URIRef(namespace2 + _list['试验设计']['盲法'])
        att_Design5 = rdflib.URIRef(namespace2 + _list['试验设计']['试验范围'])

        att_Subject_information = rdflib.URIRef(namespace + '受试者信息')
        att_age = rdflib.URIRef(namespace3 + _list['受试者信息']['年龄'])
        att_sex = rdflib.URIRef(namespace3 + _list['受试者信息']['性别'])
        att_health = rdflib.URIRef(namespace3 + _list['受试者信息']['健康受试者'])
        p = ''
        for doc in _list['受试者信息']['入选标准']:
            p += doc.replace('。。', '。')
        att_Inclusion_Criteria = rdflib.URIRef(namespace3 + p)
        p = ''
        for doc in _list['受试者信息']['排除标准']:
            p += doc.replace('。。', '。')
        att_Exclusion_Criteria = rdflib.URIRef(namespace3 + p)

        att_experimental_design = rdflib.URIRef(namespace + str(_list['试验分组']).replace('{', '[').replace('}', ']').replace(' ', ''))
        att_Main_time = rdflib.URIRef(namespace + str(_list['终点指标']['主要终点指标及评价时间']).replace('{', '[').replace('}', ']').replace(' ', '').replace('<', '(').replace('>', ')'))
        att_Secondary_time = rdflib.URIRef(namespace + str(_list['终点指标']['次要终点指标及评价时间']).replace('{', '[').replace('}', ']').replace(' ', '').replace('<', '(').replace('>', ')'))

        att_safe = rdflib.URIRef(namespace + _list['数据安全监查委员会（DMC）'])
        att_safe_buy = rdflib.URIRef(namespace + _list['为受试者购买试验伤害保险'])
        att_man_1 = rdflib.URIRef(namespace + _list['试验状态']['试验人数']['目标入组人数'].replace(' ', ''))
        att_man_2 = rdflib.URIRef(namespace + _list['试验状态']['试验人数']['已入组人数'].replace(' ', ''))
        att_man_3 = rdflib.URIRef(namespace + _list['试验状态']['试验人数']['实际入组总人数'].replace(' ', ''))
        att_firstday_1 = rdflib.URIRef(namespace + _list['试验状态']['受试者招募及试验完成日期']['第一例受试者签署知情同意书日期'])
        att_firstday_2 = rdflib.URIRef(namespace + _list['试验状态']['受试者招募及试验完成日期']['第一例受试者入组日期'])
        att_firstday_3 = rdflib.URIRef(namespace + _list['试验状态']['受试者招募及试验完成日期']['试验完成日期'])


        g.add((number, rel_medicine_name, att_medicine_name)) # 药物名称
        g.add((number, rel_medicine_type, att_medicine_type)) # 药物类型
        g.add((number, rel_indication, att_indication)) # 适应症
        g.add((number, rel_majoy, att_majoy)) # 试验专业题目
        g.add((number, rel_popular, att_popular)) # 试验通俗题目
        g.add((number, rel_contact_name, att_contact_name)) # 联系人姓名
        g.add((number, rel_contact_phone, att_contact_phone)) # 联系人座机
        g.add((number, rel_address, att_address)) # 联系人邮政地址
        g.add((number, rel_Postcode, att_Postcode)) # 联系人邮编
        g.add((number, rel_objective, att_objective)) # 试验目的
        # 试验设计
        g.add((number, rdflib.URIRef(namespace + '设计实验'), att_Design))
        g.add((rel_Design, rel_Design1, att_Design1))
        g.add((rel_Design, rel_Design2, att_Design2))
        g.add((rel_Design, rel_Design3, att_Design3))
        g.add((rel_Design, rel_Design4, att_Design4))
        g.add((rel_Design, rel_Design5, att_Design5))
        # 受试者信息
        g.add((number, rdflib.URIRef(namespace + '筛选标准'), att_Subject_information))
        g.add((rel_Subject_information, rel_age, att_age))
        g.add((rel_Subject_information, rel_sex, att_sex))
        g.add((rel_Subject_information, rel_health, att_health))
        g.add((rel_Subject_information, rel_Inclusion_Criteria, att_Inclusion_Criteria))
        g.add((rel_Subject_information, rel_Exclusion_Criteria, att_Exclusion_Criteria))

        g.add((number, rel_experimental_design, att_experimental_design)) # 试验分组
        g.add((number, rel_Main_time, att_Main_time))  # 主要终点指标及评价时间
        g.add((number, rel_Secondary_time, att_Secondary_time))  # 次要终点指标及评价时间
        g.add((number, rel_safe, att_safe))  # 数据安全监查委员会
        g.add((number, rel_safe_buy, att_safe_buy))  # 为受试者购买试验伤害保险
        g.add((number, rel_man_1, att_man_1))  # 目标入组人数
        g.add((number, rel_man_2, att_man_2))  # 已入组人数
        g.add((number, rel_man_3, att_man_3))  # 实际入组总人数
        g.add((number, rel_firstday_1, att_firstday_1))  # 第一例受试者签署知情同意书日期
        g.add((number, rel_firstday_2, att_firstday_2))  # 第一例受试者入组日期
        g.add((number, rel_firstday_3, att_firstday_3))  # 试验完成日期


        g.serialize("graph.rdf")

def xcd():
    g = rdflib.Graph()
    g.add((rdflib.URIRef('{}'), rdflib.URIRef('(）'), rdflib.URIRef('≤')))
    g.serialize("graph1.rdf", format='n3')

def loadfile():
    with open('1.json', encoding='UTF-8') as f:
        json_str = json.load(f)
        return json_str

if __name__ == "__main__":
    dic = loadfile()
    create_rdf(dic)
    #xcd()
