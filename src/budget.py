#-*- coding: utf-8 -*-
import wx
from db_budget import *
from expenses import Expenses
from manage import Manage
from accounts import Accounts
from income import Income
from transfer import Transfer
from graphs import Analysis
#from sandpit import Sandpit



class MainWindow(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, -1, "Budget ver. 1.0", size=(1100, 650))
		self.Centre(wx.BOTH)
		panel = wx.Panel(self, -1)
		
		notebook = wx.Notebook(panel)
		notebook.AddPage(Expenses(notebook), "Expenses")
		notebook.AddPage(Income(notebook), "Income")
		notebook.AddPage(Transfer(notebook), "Transfer")
		notebook.AddPage(Accounts(notebook), "Accounts")
		notebook.AddPage(Analysis(notebook), "Analysis")
		notebook.AddPage(Manage(notebook), "Manage")
		
		sizer = wx.BoxSizer()
		sizer.Add(notebook, 1, wx.EXPAND)
		panel.SetSizer(sizer)


if __name__ == '__main__':
	db.Connect("localhost", "budget", "budget", "budgetDev")
	app = wx.PySimpleApp()
	frame = MainWindow()
	frame.Show(True)
	app.MainLoop()
	db.Disconnect()
