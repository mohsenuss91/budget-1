from db import *

class DB_Budget(DB):

#insert

 	def InsertCategory(self, name, isExpense):
		return self.Query("INSERT INTO Category SET name = '%s', " % name + "isExpense =%s" % isExpense)

	def InsertAccount(self, name):
		return self._Query("INSERT INTO Account SET name = '%s'" % name)

	def InsertSubCategory(self, name, categoryID):
		return self._Query("INSERT INTO SubCategory SET name = '%s', " % name + "categoryId = %s" % categoryID) 

	def InsertEntry(self, name, value, subCategoryID, accountID, date):
		return self._Query("INSERT INTO Entry SET name ='%s', " % name + "value = %s, " % value + "subCategoryID = %s, " % subCategoryID + "accountID = %s, " % accountID + "operationDate = '%s'" % date)

	def InsertTransfer(self, name, value, fromAccountID, toAccountID, date):
		return self._CallStoredProc('INSERT_TRANSFER', (date, name, value, fromAccountID, toAccountID) )

# select

	def SelectCategories(self):
		return self._CallStoredProc('SELECT_CATEGORIES')

	def SelectAccounts(self):
		return self._CallStoredProc('SELECT_ACCOUNTS')

	def SelectSubCategories(self, isExpense):
		return self._CallStoredProc('SELECT_SUBCATEGORIES', (isExpense, ))  

	def SelectExpenses(self):
		return self._CallStoredProc("SELECT_EXPENSES")

	def SelectIncomes(self):
		return self._CallStoredProc("SELECT_INCOMES")

 	def SelectCurrentAccountBalances(self):
		return self._CallStoredProc("SELECT_CURRENT_ACCOUNT_BALANCES")
		
 	def SelectTransfers(self):
		return self._CallStoredProc("SELECT_TRANSFERS")
		
	def SelectEntry(self, entryID):
		return self._CallStoredProc("SELECT_ENTRY", (entryID, ))[0]
	
	def SelectTransfer(self, transferID):
		return self._CallStoredProc("SELECT_TRANSFER", (transferID, ))[0]	
		
 	def SelectExpensesByMonths(self):
		return self._CallStoredProc("SELECT_EXPENSES_BY_MONTHS")		

# update
		
	def UpdateEntry(self, entryID, date, name, value, subCategoryID, accountID):
		return self._CallStoredProc('UPDATE_ENTRY', (entryID, date, name, value, subCategoryID, accountID) )

	def UpdateTransfer(self, entryID, date, name, value, fromAccountID, toAccountID):
		return self._CallStoredProc('UPDATE_TRANSFER', (entryID, date, name, value, fromAccountID, toAccountID) )	

db = DB_Budget()
