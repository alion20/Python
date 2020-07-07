
import requests
import urllib
from bs4 import BeautifulSoup
import pandas as pd


#第1種抓Table方法
web2  = requests.get('https://wiki.ubuntu.com/Releases')
soup = BeautifulSoup( web2.text ,'html.parser')
table = soup.find_all('table')[1]


#第2種抓Table方法
"""
html = urllib.request.urlopen("https://wiki.ubuntu.com/Releases").read()
soup2 = BeautifulSoup(html, 'html.parser')
table2 = soup2.find_all('table')[1]
"""


#---------------------------table---------------------------
#   <tbody>
#   tr1  td td ... td     
#   tr2  td td ... td
#    .      .     .   ...  .
#    .      .     .   ...  .
#    .      .     .   ...  .
#   trX td td ... td
#   </tbody>
#-------------------------------------------------------------



columes = list()
rows = list()
columeTotal = []
rowTotal = []


tr1 = table.find('tr')
#---------------------------取得第一個tr資料---------------------------
#   <tbody>
#   tr1  td td ... td     <---------------- tr1 find this row
#   tr2  td td ... td
#    .      .     .   ...  .
#    .      .     .   ...  .
#    .      .     .   ...  .
#   trX td td ... td
#   </tbody>
#---------------------------------------------------------------------------




for tr1td in tr1.find_all('td') :
    c =  [tr1td.text.replace('\n', '').replace('\xa0', '') ]
    columeTotal = columeTotal + c

columns = columeTotal






trs = table.find_all('tr')[1:]
#---------------------------get rest tr's data---------------------------
#   tr1  td td ... td
#   tr2  td td ... td     < 把tr2到trX的資料存到trs
#    .      .     .   ...  .      
#    .      .     .   ...  .        
#    .      .     .   ...  .        
#   trX td td ... td      <
#-----------------------------------------------------------------------------



for trR in trs: 
#---------------------------get rest tr's data---------------------------
#   tr2  td td ... td     <---------------- 用for回圈 依序拿出tr，第一個for回圈拿這個
#    .      .     .   ...  .       <---------------- 第二個for回圈拿這個
#    .      .     .   ...  .       <---------------- 第三個for回圈拿這個
#    .      .     .   ...  .       <---------------- 
#   trX td td ... td      <---------------- 第X個for回圈拿這個
#-----------------------------------------------------------------------------



    for trRtd in trR.find_all('td') :
#  ---------------------------------------------------------------
#   trX  td td td ... td      <----------------用for回圈 依序從trX裡面依序拿出th 跟 td
#            ^   ^  ^    ^  ^
#  ---------------------------------------------------------------

        r=  [trRtd.text.replace('\n', '').replace('\xa0', '') ]
        rowTotal = rowTotal + r
    rows.append( rowTotal)
    rowTotal = []






df = pd.DataFrame(data=rows, columns=columns)
#df.to_excel('table4UbuntuPlanB.xls')
#print(df.head()) # just print the fisrt 5 rows of data
print(df)





"""
#------------------------------clean the data---------------------
#  把 <td style="background-color...... 這種table資料過濾成我們要的資料
#
#
#
#
aaa = tr1.find('td')  # 原本第1行第1列的資料
bbb = [aaa.text.replace('\n', '').replace('\xa0', '') ] # 過濾
print ('aaa is >> ' , aaa)
print ('bbb is >> ' , bbb)
#------------------------------clean the data---------------------
"""
