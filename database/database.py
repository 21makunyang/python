import pymysql


#连接MySQL(底层用socket链接)
conn = pymysql.connect(host='localhost',user='root',passwd='mky',charset="utf8")
#游标
cursor = conn.cursor()


#查看数据库
#发送指令
cursor.execute("show databases")
#获取命令结果
result = cursor.fetchall()
print(result)


#创建数据库
#发送指令
cursor.execute("create database db3 default charset utf8 collate utf8_general_ci")
conn.commit()

#删除数据库
cursor.execute("drop database db3")
conn.commit()

#进入数据库，查看表
cursor.execute("use mysql")
cursor.execute("show tables")
result = cursor.fetchall()
print(result)

#关闭连接
cursor.close()
conn.close()