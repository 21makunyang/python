# db_context.py
import threading
from unittest import result
import pymysql
from dbutils.pooled_db import PooledDB

POOL = PooledDB(
	creator=pymysql, #使用链接数据库的模块
	maxconnections=50, #连接池允许的最大连接数，0和None表示不限制链接数
	mincached=2, #初始化时，连接池中至少创建的空闲的链接，0表示不创建
	maxcached=3, #连接池中最多闲置的链接，0和None表示不限制
	blocking=True,#链接池中如果没有可用链接，是否阻塞等待，True，等待：False，不等待然后报错
	setsession=[], #开始会话前执行的命令列表，如：["set datestyle to ...","set time zone..."]
	ping=0,
	#ping MySQL服务器，检查是否服务可用
	#如：0 = None = never,1 = default = whenever it is requested,
	#2 = when a cursor is created,4 = when a query is excuted ,7 = always
	host='127.0.0.1',
	port=3306,
	user='root',
	password='mky',
	database='homework',
	charset='utf8'
)

class Connect(object):
	def __init__(self):
		self.conn = conn =POOL.connection()
		self.cursor = conn.cursor(pymysql.cursors.DictCursor)

	def __enter__(self):
		return self

	def __exit__(self,exc_type,exc_val,exc_tb):
		self.cursor.close()
		self.conn.close()

	def exec(self,sql,**kwargs):
		self.cursor.excute(sql,kwargs)
		self.conn.commit()

	def fetch_one(self,sql,**kwargs):
		self.cursor.execute(sql,kwargs)
		result = self.cursor.fetchone()
		return result

	def fetch_all(self,sql,**kwargs):
		self.cursor.excute(sql,kwargs)
		result = self.cursor.fetchall()
		return result