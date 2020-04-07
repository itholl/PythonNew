import requests
import json
print("FF14[国服]觉醒篇英雄榜查询_官网数据   -by：Big Taro")
url = 'http://act.ff.sdo.com/20180525HeroList/Server/HeroList190128.ashx'
'''
鸟区AreaId：1
莫古力AreaId：6
猫区AreaId：7

'''
name = input('>>>请输入角色ID:')
areaid = input('>>>请输入服务器:')
print('查询信息：',name,'-',areaid)
#------------------鸟区start-------------------
ser = areaid in '红玉海'
if ser:
    daqu = 1
    serverid = 27

ser = areaid in '神意之地'
if ser:
    daqu = 1
    serverid = 23

ser = areaid in '拉诺西亚'
if ser:
    daqu = 1
    serverid = 3

ser = areaid in '幻影群岛'
if ser:
    daqu = 1
    serverid = 5

ser = areaid in '萌芽池'
if ser:
    daqu = 1
    serverid = 25

ser = areaid in '宇宙和音'
if ser:
    daqu = 1
    serverid = 28

ser = areaid in '沃仙曦染'
if ser:
    daqu = 1
    serverid = 29

ser = areaid in '晨曦王座'
if ser:
    daqu = 1
    serverid = 30
# ------------------鸟区end-------------------

# ------------------莫古力start-------------------
ser = areaid in '白银乡'
if ser:
    daqu = 6
    serverid = 3

ser = areaid in '白金幻象'
if ser:
    daqu = 6
    serverid = 4

ser = areaid in '神拳痕'
if ser:
    daqu = 6
    serverid = 2

ser = areaid in '潮风亭'
if ser:
    daqu = 6
    serverid = 1

ser = areaid in '旅人栈桥'
if ser:
    daqu = 6
    serverid = 5

ser = areaid in '拂晓之间'
if ser:
    daqu = 6
    serverid = 6

ser = areaid in '龙巢神殿'
if ser:
    daqu = 6
    serverid = 7

ser = areaid in '梦羽宝境'
if ser:
    daqu = 6
    serverid = 8
# ------------------莫古力end-------------------

# ------------------猫区start-------------------
ser = areaid in '紫水栈桥'
if ser:
    daqu = 7
    serverid = 1

ser = areaid in '延夏'
if ser:
    daqu = 7
    serverid = 2

ser = areaid in '静语庄园'
if ser:
    daqu = 7
    serverid = 3

ser = areaid in '摩杜纳'
if ser:
    daqu = 7
    serverid = 4

ser = areaid in '海猫茶屋'
if ser:
    daqu = 7
    serverid = 5

ser = areaid in '柔风海湾'
if ser:
    daqu = 7
    serverid = 6

ser = areaid in '琥珀原'
if ser:
    daqu = 7
    serverid = 7
# ------------------猫区end-------------------
data = {'method': 'queryhreodata','Stage': '2','Name': name,'AreaId': daqu,'GroupId': serverid}
res = requests.post(url=url,data=data)
A=json.loads(res.text)
th=(A["Attach"]) #提取中括号内嵌套数据
for key,value in th.items(): #字典分离 key，value
 print('%s => %s' % (key,value))
oer = 'null' in res.text
if oer:
    print("未查询到数据，请注意角色服务器填写正确 或 该角色未通关")
else:
    print(name,':',areaid,'->完成了零式希望乐园觉醒之章的所有挑战')

input('按任意键退出程序')