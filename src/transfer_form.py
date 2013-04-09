#-*- coding: utf-8 -*-

import wx
from db import *
from useful import *
from base_form import *

class TransferForm(BaseForm):
	def __init__(self, parent):
		BaseForm.__init__(self, parent)

		accountTable = db.SelectAccounts()	
		accountTable = (("NULL", u"--- none ---"), ) + accountTable
		self.dateField = DateField(self, "date", 120)
		self.nameField = EditField(self, "name", 120)
		self.valueField = MoneyField(self, "value", 80)
		self.fromAccountField = DropdownField(self, "From Account", accountTable)
		self.toAccountField = DropdownField(self, "To Account", accountTable)

		self.AddField(self.dateField)
		self.AddField(self.nameField)
		self.AddField(self.valueField)
		self.AddField(self.fromAccountField)
		self.AddField(self.toAccountField)

	def OnClickAdd(self, event):
		name = self.nameField.GetValue()
		value = self.valueField.GetValue()
		fromAccountID = self.fromAccountField.GetValue()
		toAccountID = self.toAccountField.GetValue()
		date = self.dateField.GetValue() 
		
		db.InsertTransfer(name, value, fromAccountID, toAccountID, date)
		self.ForceRefresh()
		
	def OnEditMode(self):
		transfer = db.SelectTransfer(self.EditRowID)
		self.dateField.SetValue(str(transfer[1]))
		self.nameField.SetValue(transfer[2])
		self.valueField.SetValue(str(transfer[3]))
		self.fromAccountField.SetValue(transfer[4])
		self.toAccountField.SetValue(transfer[5])
	
	def OnClickUpdate(self, event):
		name = self.nameField.GetValue()
		value = self.valueField.GetValue()
		fromAccountID = self.fromAccountField.GetValue()
		toAccountID = self.toAccountField.GetValue()
		date = self.dateField.GetValue() 
		
		db.UpdateTransfer(self.EditRowID, date, name, value, fromAccountID, toAccountID)
		self.ForceRefresh()	
