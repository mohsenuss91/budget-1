#-*- coding: utf-8 -*-

import wx
from db_budget import *
from useful import GridCtr
from transfer_form import TransferForm

class Transfer(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent)

		self.form = TransferForm(self)
		columns = [["date", 120], ["name", 120], ["value", 90], ["acc. from", 90], ["acc. to", 90], ["", 45, "editButton"]]
		self.grid = GridCtr(self, columns, db.SelectTransfers)
		self.form.SubscribeForRefresh(self.grid)		
		self.grid.AtachForm(self.form)
		self.__sizer()
		
	def __sizer(self):
		sizerAux = wx.BoxSizer(wx.VERTICAL)
		sizerAux.AddSpacer(15)
		sizerAux.Add(self.form, 1, wx.ALL | wx.EXPAND)
		sizerAux.AddSpacer(25)
		sizerAux.Add(self.grid, 11, wx.ALL | wx.EXPAND)
		
		sizer = wx.BoxSizer(wx.HORIZONTAL)
		sizer.AddSpacer(25)
		sizer.Add(sizerAux, 1, wx.ALL | wx.EXPAND)
		self.SetSizer(sizer)
