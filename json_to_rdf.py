# coding:utf-8
import rdflib
import json

def create_rdf(dic):
    g = rdflib.Graph()
    for _list in dic:
        # 实体
        number = rdflib.URIRef(_list['登记号'])


        # 关系
        rel_medicine_name = rdflib.URIRef('药物名称')
        rel_medicine_type = rdflib.URIRef('药物类型')
        rel_indication = rdflib.URIRef('适应症')
        rel_majoy = rdflib.URIRef('试验专业题目')
        rel_popular = rdflib.URIRef('试验通俗题目')
        rel_contact_name = rdflib.URIRef('联系人姓名')
        rel_contact_phone = rdflib.URIRef('联系人座机')
        rel_address = rdflib.URIRef('联系人邮政地址')


        # 属性
        att_medicine_name = rdflib.URIRef(_list['药物名称'])
        att_medicine_type = rdflib.URIRef(_list['药物类型'])
        att_indication = rdflib.URIRef(_list['适应症'])
        att_majoy = rdflib.URIRef(_list['试验专业题目'])
        att_popular = rdflib.URIRef(_list['试验通俗题目'])
        att_contact_name = rdflib.URIRef(_list['联系人姓名'])
        att_contact_phone = rdflib.URIRef(str(_list['联系人座机']))
        att_address = rdflib.URIRef(_list['联系人邮政地址'])




        g.add((number, rel_medicine_name, att_medicine_name))
        g.add((number, rel_medicine_type, att_medicine_type))
        g.add((number, rel_indication, att_indication))
        g.add((number, rel_majoy, att_majoy))
        g.add((number, rel_popular, att_popular))
        g.add((number, rel_contact_name, att_contact_name))
        g.add((number, rel_contact_phone, att_contact_phone))
        g.add((number, rel_address, att_address))







        g.serialize("graph.rdf", format='n3')


def loadfile():
    with open('1.json',encoding='UTF-8') as f:
        json_str = json.load(f)
        return json_str

if __name__ == "__main__":
    dic = loadfile()
    create_rdf(dic)
