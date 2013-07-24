import wx
from db_budget import *

import matplotlib
matplotlib.use('WXAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigCanvas
import numpy as np

def GetSelectColumn(select, col):
	strList = []
	for element in select:
		strList += [ element[col] ]
	return strList


class BarFigure(wx.Panel):
	def __init__(self, parent, data):
		wx.Panel.__init__(self, parent)
		self.fig = Figure((10.0, 4.0), dpi=100)
		self.canvas = FigCanvas(parent, -1, self.fig)
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
				
class Graphs(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent)
		
		expenses = db.SelectExpensesByMonths()
		figure = BarFigure(self, expenses)
		



