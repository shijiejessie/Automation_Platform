# coding=gb2312
from utils.LogUtil import my_log
import pymysql
#创建封装类,#初始化数据，连接数据库，光标对象
class Mysql:
    def __init__(self,host,user,password,database,charset,port):
        self.log = my_log()
        self.conn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            charset=charset,
            port=port
        )

        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

#创建查询、执行方法
    def fetchone(self,sql):
        #单个查询
        self.cursor.execute(sql)
        return self.cursor.fetchone()
    def fetchall(self,sql):
        #多个查询
        self.cursor.execute(sql)
        return  self.cursor.fetchall()
    def exec(self,sql):
        try:
            if self.conn and self.cursor:
                self.cursor.execute(sql)
                self.conn.commit()
        except Exception as ex:
            self.conn.rollback()
            self.log.error("Mysql执行失败")
            self.log.error(ex)
            return False
        return True
#关闭对象
    def __del__(self):
        self.cursor.close()
        self.conn.close()
        #关闭数据库连接对象


if __name__ == "__main__":
    mysql= Mysql(host="192.168.185.72",user="root",password="P@ssYSKLw0rd@298",database="sdn",charset="utf8",port=33060)
    #打印单行
    res=mysql.fetchone("select * from device limit 5")
    #打印全部数据
    res2=mysql.fetchall("select * from device limit 5")
    print(res)
    print(res2)

