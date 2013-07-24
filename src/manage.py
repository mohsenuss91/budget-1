#-*- coding: utf-8 -*-

import wx
from db_budget import *

class Manage(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent)

		self.categoryTable = db.SelectCategories()

# category
		sizerCategory = wx.BoxSizer(wx.HORIZONTAL)
		self.textCategoryName = wx.TextCtrl(self, -1, "", size=(120, -1) )
		self.checkCategoryIsExpense = wx.CheckBox(self, -1, "Expense")
		self.buttonCategoryAdd = wx.Button(self, -1, "Add Category")
		self.Bind(wx.EVT_BUTTON, self.OnClickCategoryAdd, self.buttonCategoryAdd)
		sizerCategory.AddSpacer(25)
		sizerCategory.Add(self.textCategoryName)
		sizerCategory.AddSpacer(25)	
		sizerCategory.Add(self.checkCategoryIsExpense)
		sizerCategory.AddSpacer(25)		
		sizerCategory.Add(self.buttonCategoryAdd)

# subcategory
		sizerSubCategory = wx.BoxSizer(wx.HORIZONTAL)
		self.textSubCategoryName = wx.TextCtrl(self, -1, "", size=(120, -1))
		self.choiceSubCategoryCategory = wx.Choice(self, -1, choices=GetSelectNames(self.categoryTable) )
		self.buttonSubCategoryAdd = wx.Button(self, -1, "Add SubCategory")
		self.Bind(wx.EVT_BUTTON, self.OnClickSubCategoryAdd, self.buttonSubCategoryAdd)
		sizerSubCategory.AddSpacer(25)
		sizerSubCategory.Add(self.textSubCategoryName)
		sizerSubCategory.AddSpacer(10)		
		sizerSubCategory.Add(self.choiceSubCategoryCategory)
		sizerSubCategory.AddSpacer(25)
		sizerSubCategory.Add(self.buttonSubCategoryAdd)
		
# account
		sizerAccount = wx.BoxSizer(wx.HORIZONTAL)
		self.textAccountName = wx.TextCtrl(self, -1, "", size=(120, -1) )
		self.buttonAccountAdd = wx.Button(self, -1, "Add Account")
		self.Bind(wx.EVT_BUTTON, self.OnClickAccountAdd, self.buttonAccountAdd)
		sizerAccount.AddSpacer(25)
		sizerAccount.Add(self.textAccountName)
		sizerAccount.AddSpacer(25)		
		sizerAccount.Add(self.buttonAccountAdd)


		sizerMain = wx.BoxSizer(wx.VERTICAL)
		sizerMain.AddSpacer(50)
		sizerMain.Add(sizerCategory)
		sizerMain.AddSpacer(25)
		sizerMain.Add(sizerSubCategory)
		sizerMain.AddSpacer(25)
		sizerMain.Add(sizerAccount)
		self.SetSizer(sizerMain)

	def OnClickCategoryAdd(self,event):
		isExpense = 'TRUE' if self.checkCategoryIsExpense.GetValue() else 'FALSE'
		db.InsertCategory( self.textCategoryName.GetValue(), isExpense )
		self.textCategoryName.SetValue("")

	def OnClickSubCategoryAdd(self,event):
		categoryID = GetSelectIdByName(self.categoryTable, self.choiceSubCategoryCategory.GetStringSelection()) 
		db.InsertSubCategory( self.textSubCategoryName.GetValue(), categoryID)
		self.textSubCategoryName.SetValue("")
	
	def OnClickAccountAdd(self,event):
		db.InsertAccount( self.textAccountName.GetValue() )
		self.textAccountName.SetValue("")

