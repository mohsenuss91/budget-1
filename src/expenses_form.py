#-*- coding: utf-8 -*-

import wx
from db import *
from useful import *
from base_form import *

class ExpensesForm(BaseForm):
	def __init__(self, parent):
		BaseForm.__init__(self, parent, "../media/expenses.png")

		self.dateField = DateField(self, "date", 120)
		self.nameField = EditField(self, "name", 120)
		self.valueField = MoneyField(self, "value", 80)
		self.subCategoryField = DropdownField(self, "category", db.SelectSubCategories(True))
		self.accountField = DropdownField(self, "account", db.SelectAccounts())

		self.AddField(self.dateField)
		self.AddField(self.nameField)
		self.AddField(self.valueField)
		self.AddField(self.subCategoryField)
		self.AddField(self.accountField)

	def OnClickAdd(self, event):
		name = self.nameField.GetValue()
		value = '-' + self.valueField.GetValue()
		subCategoryID = self.subCategoryField.GetValue()
		accountID = self.accountField.GetValue()
		date = self.dateField.GetValue() 
		db.InsertEntry(name, value, subCategoryID, accountID, date)
		self.ForceRefresh()
		
	def OnEditMode(self):
		entry = db.SelectEntry(self.EditRowID)
		self.dateField.SetValue(str(entry[1]))
		self.nameField.SetValue(entry[2])
		self.valueField.SetValue(str(-entry[3]))
		self.subCategoryField.SetValue(entry[4])
		self.accountField.SetValue(entry[5])

	def OnClickUpdate(self, event):
		name = self.nameField.GetValue()
		value = '-' + self.valueField.GetValue()
		subCategoryID = self.subCategoryField.GetValue()
		accountID = self.accountField.GetValue()
		date = self.dateField.GetValue() 
		db.UpdateEntry(self.EditRowID, date, name, value, subCategoryID, accountID)
		self.ForceRefresh()
