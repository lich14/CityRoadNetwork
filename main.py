# -*- coding:utf-8 -*-

import pymssql
import random

class MSSQL:
    def __init__(self,host,user,pwd,db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def __GetConnect(self):
        if not self.db:
            raise(NameError,"没有设置数据库信息")
        self.conn = pymssql.connect(host=self.host,user=self.user,password=self.pwd,database=self.db,charset="utf8")
        cur = self.conn.cursor()
        if not cur:
            raise(NameError,"连接数据库失败")
        else:
            return cur

    def ExecQuery(self,sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()

        #查询完毕后必须关闭连接
        self.conn.close()
        return resList

    def ExecNonQuery(self,sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()

ms = MSSQL(host="166.111.140.39",user="sa",pwd="lch@1234",db="tl")

def searchnext (m,n):
    if m-1==n or m+1==n or m-5==n or m+5==n:
        return[n]
    elif m>n:
        if m-5>n:
            if m%5==n%5:
                return[m-5]
            p=random.randint(1,2)
            if p==1:
                return[m-5]
            else:
                return[m-1]
        else:
            return[m-1]
    else:
        if m+5<n:
            if m%5==n%5:
                return[m+5]
            p=random.randint(1,2)
            if p==1:
                return[m+5]
            else:
                return[m+1]
        else:
            return[m+1]

#for j in range(1,5):
#    newsql="insert trafficlight values("+str(j)+",0,0)"
#    print newsql
#    ms.ExecNonQuery(newsql.encode('utf-8'))

#reslist = ms.ExecQuery("select * from lanewithcar")
#print reslist

dic={1:1,2:2,3:3,4:4,5:5,6:5,7:10,8:15,9:20,10:25,11:25,12:24,13:23,14:22,15:21,16:21,17:16,18:11,19:6,20:1}


sqlwords="insert into question(id,startRoad,endRoad,lk1,lk2,lk3,lk4,lk5,lk6,lk7,lk8,lk9)"      
for i in range(1,2000):
    m=random.randint(1,20)
    n=random.randint(1,20)
    while m==n:
        n=random.randint(1,20)

    sqlwords=sqlwords+" select "+str(i)+","+str(m)+","+str(n)+","
    isform=dic[m]
    isforn=dic[n]
    sqlwords=sqlwords+str(isform)
    p=isform
    listis=[]
    #print searchnext(10,25)[0]
    
    while p!=isforn:
        p=searchnext(p,isforn)[0]
        listis.append(p)
    print listis
    print len(listis)

    for j in range(0,len(listis)):
        sqlwords=sqlwords+","+str(listis[j])

    numleft=9-len(listis)
    if numleft>0:
        for k in range(1,numleft):
            sqlwords=sqlwords+","+str(-1)

    if i!=1999:
        sqlwords=sqlwords+" union"

print(sqlwords)
newsql="insert trafficlight values("+str(j)+",0,0)"
ms.ExecNonQuery(sqlwords)


