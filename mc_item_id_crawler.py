print("正在載入套件...")

from sys import modules
import urllib.request as req
import bs4
from googletrans import Translator
import lxml
import os
import pandas as pd

name1list=[]
id1list=[]
printlist=[]
print("開始連接...")
url="https://minecraft.fandom.com/zh/wiki/%E5%9F%BA%E5%B2%A9%E7%89%88%E6%95%B0%E6%8D%AE%E5%80%BC?variant=zh-tw"
table = pd.read_html(url)
print("連結成功...")
# print(table)

def get_item_id_and_name(get_table):
    id1 = (table[get_table])
    id1_name= id1['方塊']
    id1_id= id1['命名空間ID']
    for name in id1_name:
        try:
            name=name[:name.index(" ")]
            name1list.append(name)
        except:
            name1list.append(name)
    for id in id1_id:
        try:
            id1list.append(id)
        except:
            id1list.append(id)
    for getstring in range(len(name1list)):
        printlist.append("item."+ id1list[getstring] + ".name=" + name1list[getstring]+"(" +id1list[getstring]+")")

# get_item_id_and_name(6)
# print(printlist)

def get_block_id_and_name(get_table):
    id1 = (table[get_table])
    id1_name= id1['方塊']
    id1_id= id1['命名空間ID']
    for name in id1_name:
        try:
            name=name[:name.index(" ")]
            name1list.append(name)
        except:
            name1list.append(name)
    for id in id1_id:
        try:
            id1list.append(id)
        except:
            id1list.append(id)
    for getstring in range(len(name1list)):
        try:
            if get_table <= 5:
                printlist.append("tile."+ id1list[getstring] + ".name=" + name1list[getstring]+"(" +id1list[getstring]+")")
            else:
                printlist.append("item."+ id1list[getstring] + ".name=" + name1list[getstring]+"(" +id1list[getstring]+")")
        except:
            print("擷取錯誤")

for get in range(10):
    print("擷取整筆資料..."+str(get+1))
    get_block_id_and_name(get+1)

# for get in range(5):
#     print("擷取整筆資料..."+str(get+6))
#     get_item_id_and_name(get+6)

flie_write=""

for list in printlist:
    flie_write+=(list+"\n")

print(flie_write)

flie = open("zh_TW.lang","x",encoding="utf-8")
flie.write(flie_write)
flie.close()

# for i in range(count-1):
#     getData("https://mcpedl.com/category/mods/page/"+ str(i+2) + "/")