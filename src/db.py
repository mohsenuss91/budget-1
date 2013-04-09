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

	def Connect(self):
		print "db.connect"
		self.__conn = MySQLdb.connect(host = "localhost", user = "budget", passwd = "budget", db = "budget", charset = "utf8")
		self.__cursor = self.__conn.cursor()

	def Disconnect(self):
		print "db.disconnect"
		self.__cursor.close()
		self.__conn.commit()
		self.__conn.close()

	def __Query(self, strQuery):
		self.__cursor.execute(strQuery.decode("utf8"))
		self.__conn.commit()
		return True

		
	def __CallStoredProc(self, name, args=()):
		self.__cursor.callproc(name, args)

		ret = self.__cursor.fetchall()
		while self.__cursor.nextset() :
			self.__cursor.fetchall()
			
		self.__conn.commit()	
		return ret

				
#	def __CallStoredProcedure(self, name, params=''):	
#		strQuery = 'CALL ' + name + '(' + params + ')';
#		print strQuery
#		self.__cursor.execute(strQuery.decode("utf8"))
#		ret = self.__cursor.fetchall()
#		while self.__cursor.nextset() :
#			self.__cursor.fetchall()
#		return ret

#insert

 	def InsertCategory(self, name, isExpense):
		return self.__Query("INSERT INTO Category SET name = '%s', " % name + "isExpense =%s" % isExpense)

	def InsertAccount(self, name):
		return self.__Query("INSERT INTO Account SET name = '%s'" % name)

	def InsertSubCategory(self, name, categoryID):
		return self.__Query("INSERT INTO SubCategory SET name = '%s', " % name + "categoryId = %s" % categoryID) 

	def InsertEntry(self, name, value, subCategoryID, accountID, date):
		return self.__Query("INSERT INTO Entry SET name ='%s', " % name + "value = %s, " % value + "subCategoryID = %s, " % subCategoryID + "accountID = %s, " % accountID + "operationDate = '%s'" % date)

	def InsertTransfer(self, name, value, fromAccountID, toAccountID, date):
		return self.__Query("INSERT INTO Transfer SET name ='%s', " % name + "value = %s, " % value + "fromAccountID = %s, " % fromAccountID + "toAccountID = %s, " % toAccountID + "operationDate = '%s'" % date)

# select

	def SelectCategories(self):
		return self.__CallStoredProc('SELECT_CATEGORIES')

	def SelectAccounts(self):
		return self.__CallStoredProc('SELECT_ACCOUNTS')

	def SelectSubCategories(self, isExpense):
		return self.__CallStoredProc('SELECT_SUBCATEGORIES', (isExpense, ))  

	def SelectExpenses(self):
		return self.__CallStoredProc("SELECT_EXPENSES")

	def SelectIncomes(self):
		return self.__CallStoredProc("SELECT_INCOMES")

 	def SelectCurrentAccountBalances(self):
		return self.__CallStoredProc("SELECT_CURRENT_ACCOUNT_BALANCES")
		
 	def SelectTransfers(self):
		return self.__CallStoredProc("SELECT_TRANSFERS")
		
	def SelectEntry(self, entryID):
		return self.__CallStoredProc("SELECT_ENTRY", (entryID, ))[0]
	
	def SelectTransfer(self, transferID):
		return self.__CallStoredProc("SELECT_TRANSFER", (transferID, ))[0]	
		
 	def SelectExpensesByMonths(self):
		return self.__CallStoredProc("SELECT_EXPENSES_BY_MONTHS")		

# update
		
	def UpdateEntry(self, entryID, date, name, value, subCategoryID, accountID):
		return self.__CallStoredProc('UPDATE_ENTRY', (entryID, date, name, value, subCategoryID, accountID) )

	def UpdateTransfer(self, entryID, date, name, value, fromAccoutID, toAccountID):
		return self.__CallStoredProc('UPDATE_TRANSFER', (entryID, date, name, value, fromAccoutID, toAccountID) )			

db = DB()
