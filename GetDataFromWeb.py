#!coding:utf-8
# Version    : 1.0
# Time       : 2020/1/20
# Author     : Hua Rong
# Environment: python2.7
# Packages   : pandas, JSON, requests

import json
import requests
import pandas as pd

def confirm(x):
    c = eval(str(x))['confirm']
    return c

def suspect(x):
    s = eval(str(x))['suspect']
    return s

def dead(x):
    d = eval(str(x))['dead']
    return d

def heal(x):
    h =  eval(str(x))['heal']
    return h

def catch_data_china():
    # url_1包含中国各省市当日实时数据(也有全球数据，但是腾讯改版后好久没更新了)
    url_1 = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
    response = requests.get(url=url_1).json()
    data_1 = json.loads(response['data'])
    return data_1

def catch_data_world():
    # url_2包含全球实时数据及历史数据、中国历史数据及每日新增数据
    url_2 = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_other'
    data_2 = json.loads(requests.get(url=url_2).json()['data'])
    return data_2

data_world = catch_data_world()
data_china = catch_data_china()

#print(data_world.keys())
#print(data_china.keys())
# dict_keys(['chinaTotal', 'chinaAdd', 'lastUpdateTime', 'areaTree', 'chinaDayList', 'chinaDayAddList'])
# 数据集包括[   "国内总量",   "国内新增",     "更新时间",      "数据明细",    "每日数据",        "每日新增"]

lastUpdateTime = data_china['lastUpdateTime']
chinaTotal = data_china['chinaTotal']
chinaAdd = data_china['chinaAdd']
print "更新时间:",lastUpdateTime
print "确诊病例:",chinaTotal['confirm']
print "疑似病例:",chinaTotal['suspect']
print "治愈病例:",chinaTotal['heal']
print "死亡病例:",chinaTotal['dead']
print "新增确诊:",chinaAdd['confirm']
print "新增疑似:",chinaAdd['suspect']
print "新增治愈:",chinaAdd['heal']
print "新增死亡:",chinaAdd['dead']

# 数据明细，数据结构比较复杂，一步一步打印出来看，先明白数据结构
areaTree = data_china['areaTree']
# 国内数据
china_data = areaTree[0]['children']
china_list = []
for a in range(len(china_data)):
    province = china_data[a]['name']
    province_list = china_data[a]['children']
    for b in range(len(province_list)):
        city = province_list[b]['name']
        total = province_list[b]['total']
        today = province_list[b]['today']
        china_dict = {}
        china_dict['province'] = province
        china_dict['city'] = city
        china_dict['total'] = total
        china_dict['today'] = today
        china_list.append(china_dict)

china_data = pd.DataFrame(china_list)
china_data.head()

# 函数映射
china_data['confirm'] = china_data['total'].map(confirm)
china_data['suspect'] = china_data['total'].map(suspect)
china_data['dead'] = china_data['total'].map(dead)
china_data['heal'] = china_data['total'].map(heal)
china_data = china_data[["province","city","confirm","suspect","dead","heal"]]
china_data.head()

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

print china_data

