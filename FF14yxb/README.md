# FF14[国服]觉醒篇英雄榜查询_官网数据   
## 使用说明
1.输入角色ID,服务器（按回车） 
服务器名可以缩写，无需全写也可以（服务器名的任意1-2字即可，注意别输错字）  
 ![运行实况1](https://github.com/itholl/PythonNew/blob/master/FF14yxb/%E7%A4%BA%E4%BE%8B1.png)      
 ![运行实况2](https://github.com/itholl/PythonNew/blob/master/FF14yxb/%E7%A4%BA%E4%BE%8B2.png)   
 

## 程序闪退问题  
说明：如果无法访问英雄榜页面或者服务器输入错误程序会闪退    

## 查询原理  
1.post fromdata  url：http://act.ff.sdo.com/20180525HeroList/Server/HeroList190128.ashx   

官方英雄榜查询 http://act.ff.sdo.com/20180525HeroList/index200305.html  



## 接口名称

### 1) 请求地址

>http://act.ff.sdo.com/20180525HeroList/Server/HeroList190128.ashx

### 2) 调用方式：HTTP post

### 3) 接口描述：

* 接口描述详情

### 4) 请求参数:


#### POST参数:
|字段名称       |字段说明         |类型            |必填            |备注     |
| -------------|:--------------:|:--------------:|:--------------:| ------:|
|method||string|Y|-|
|Stage||string|Y|-|
|Name||string|Y|-|
|AreaId||string|Y|-|
|GroupId||string|Y|-|



### 5) 请求返回结果:

```
{
    "Code": 0,
    "Message": "成功",
    "Attach": {
        "Level1": 20191224,
        "Level2": 20191224,
        "Level3": 20191225,
        "Level4": 20191226,
        "Fpercent": 
    },
    "Success": true
}
```


### 6) 请求返回结果参数说明:
|字段名称       |字段说明         |类型            |必填            |备注     |
| -------------|:--------------:|:--------------:|:--------------:| ------:|
|Code||string|Y|-|
|Message||string|Y|-|
|Attach||string|Y|-|
|Level1||string|Y|-|
|Level2||string|Y|-|
|Level3||string|Y|-|
|Level4||string|Y|-|
|Fpercent||string|Y|-|
|Success||string|Y|-|

