# coding=gb2312
from utils.LogUtil import my_log
import pymysql
#������װ��,#��ʼ�����ݣ��������ݿ⣬������
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

#������ѯ��ִ�з���
    def fetchone(self,sql):
        #������ѯ
        self.cursor.execute(sql)
        return self.cursor.fetchone()
    def fetchall(self,sql):
        #�����ѯ
        self.cursor.execute(sql)
        return  self.cursor.fetchall()
    def exec(self,sql):
        try:
            if self.conn and self.cursor:
                self.cursor.execute(sql)
                self.conn.commit()
        except Exception as ex:
            self.conn.rollback()
            self.log.error("Mysqlִ��ʧ��")
            self.log.error(ex)
            return False
        return True
#�رն���
    def __del__(self):
        self.cursor.close()
        self.conn.close()
        #�ر����ݿ����Ӷ���


if __name__ == "__main__":
    mysql= Mysql(host="192.168.185.72",user="root",password="P@ssYSKLw0rd@298",database="sdn",charset="utf8",port=33060)
    #��ӡ����
    res=mysql.fetchone("select * from device limit 5")
    #��ӡȫ������
    res2=mysql.fetchall("select * from device limit 5")
    print(res)
    print(res2)

