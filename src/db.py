#-*- coding: utf-8 -*-
import MySQLdb

def GetSelectNames(select):
	strList = []
	for element in select:
		strList += [ element[1] ]
	return strList

def GetSelectIdByName(select, name):
	for element in select:
		if element[1] == name:
			return element[0]
	return -1

def GetFetchHmRows(select):
	return len(select);

def GetFetchHmCols(select):
	return len(select[0]);


class DB:
	__conn = None
	__cursor = None

	def Connect(self, _host, _user, _passwd, _db):
		print "db.connect"
		self.__conn = MySQLdb.connect(host = _host, user = _user, passwd = _passwd, db = _db, charset = "utf8")
		self.__cursor = self.__conn.cursor()

	def Disconnect(self):
		print "db.disconnect"
		self.__cursor.close()
		self.__conn.commit()
		self.__conn.close()

	def _Query(self, strQuery):
		self.__cursor.execute(strQuery.decode("utf8"))
		self.__conn.commit()
		return True

	def _CallStoredProc(self, name, args=()):
		self.__cursor.callproc(name, args)

		ret = self.__cursor.fetchall()
		while self.__cursor.nextset() :
			self.__cursor.fetchall()
			
		self.__conn.commit()	
		return ret	


