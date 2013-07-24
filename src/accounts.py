#-*- coding: utf-8 -*-

import wx
from db_budget import *
from useful import *

class Accounts(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent)

		columns = [["Account", 150], ["Current Balance", 150]]
		self.gridBalances = GridCtr(self, columns, db.SelectCurrentAccountBalances)
		
		self.__sizer()
		
	def __sizer(self):		
		sizerAux = wx.BoxSizer(wx.VERTICAL)
		sizerAux.AddSpacer(25)
		sizerAux.Add(self.gridBalances)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		sizer.AddSpacer(50)
		sizer.Add(sizerAux, 1, wx.ALL | wx.EXPAND)
		self.SetSizer(sizer)
