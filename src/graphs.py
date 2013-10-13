import wx
from db_budget import *

import matplotlib
matplotlib.use('WXAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigCanvas
import numpy as np

from base_form import *

def GetSelectColumn(select, col):
	strList = []
	for element in select:
		strList += [ element[col] ]
	return strList


class BarFigure(wx.Panel):
	def __init__(self, parent, data):
		wx.Panel.__init__(self, parent)
		self.fig = Figure((10.0, 4.0), dpi=100)
		self.canvas = FigCanvas(self, -1, self.fig)
		self.axes = self.fig.add_subplot(111)
		self.data = GetSelectColumn(data, 1)
		ind = np.arange(len(self.data))
		self.axes.clear()        
		self.axes.grid(True)
		self.axes.set_xticks(ind)
		self.axes.set_xticklabels( GetSelectColumn(data, 0) )
		self.axes.bar(
			left=ind, 
			height=self.data, 
			width=0.5, 
			align='center', 
			alpha=0.88,
			picker=5)

		self.canvas.draw()		
				
class Analysis(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent)
		
		self.form = AnalysisForm(self)
		expenses = db.SelectExpensesByMonths()
		self.figure = BarFigure(self, expenses)
		
		self.__sizer()
		
	def __sizer(self):
		sizerAux = wx.BoxSizer(wx.VERTICAL)
		sizerAux.AddSpacer(15)
		sizerAux.Add(self.form, 1, wx.ALL | wx.EXPAND)
		sizerAux.AddSpacer(25)
		sizerAux.Add(self.figure, 11, wx.ALL | wx.EXPAND)
		
		sizer = wx.BoxSizer(wx.HORIZONTAL)
		sizer.AddSpacer(25)
		sizer.Add(sizerAux, 1, wx.ALL | wx.EXPAND)
		self.SetSizer(sizer)
	
		
class AnalysisForm(BaseForm):
	def __init__(self, parent):
		BaseForm.__init__(self, parent, "../media/graphs.png")
		raportTypes = ((1, "Expenses by months"), (2, "Expenses by months with deprecition"), (3,"Accounts balance history"))
		self.raportField = DropdownField(self, "raport type", raportTypes)
		#self.raportField = DropdownField(self, "raport type", db.SelectAccounts())
		print db.SelectAccounts()
		
		self.AddField(self.raportField)
		



