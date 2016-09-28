'''@author: yzw
'''
#!/usr/bin/python  
# -*- coding:utf-8 -*-  

import urllib   
from urllib import request
import requests 
from bs4 import BeautifulSoup
import json
#模拟登录
login="http://yun.oppo.com/login"
UA = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0"  
header = { "User-Agent" : UA,
           "Referer": "http://yun.oppo.com/login"
           }
note_session = requests.Session()
f = note_session.get(login,headers=header)
soup = BeautifulSoup(f.content,"html.parser")
postData = { 'username': 'lgcrqyqx',
             'pwd': '',
             'password': 'dff84fc81e93ada0e81862bdc27c607e',
             }
note_session.post(login,
                  data = postData,
                  headers = header)
#匹配网址
year=input('请输入要导出笔记的年份: \n')
mon =1
for mon in range(1,13,1):
    month = "%02d" % mon
    f = note_session.get('http://note.yun.oppo.com/note?operation=1&note_month='+year+'-'+month+'&search_word=',headers=header)
    note=f.content.decode()
    note=note.replace('{','')
    note=note.replace('},','*1')#用一个不常用的字符‘*1’作为下面的将一条条信息隔开的标识
    note=note.replace('[','')
    note=note.replace(']','')
    note=note.split('*1')
    n=len(note)
    i=0
    for i in range(0,n):
        note[i]=note[i].replace('}','')
        note[i]=str('{'+note[i]+'}')
        note[i]=json.loads(note[i])
        note[i]=dict(note[i])
        try:
            date = ('show_note_updated' in note[i].keys())
            if date == False :
               date =''
            else:
               date =note[i]['show_note_updated']
               
            date1 = ('str_content' in note[i].keys())
            if date1 == False :
               date1 =''
            else:
               date1 =note[i]['str_content'] 
                  
        except(TypeError, IndexError):
           pass 
        s=date+':'+date1
        ftp = open(year+'.txt','a',encoding='utf-8') 
        ftp.write(s+'\n\n') 
        ftp.close()
        

        


