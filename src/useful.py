#-*- coding: utf-8 -*-
import wx
import wx.grid
from db_budget import *
from base_fields import *

class GridDb(wx.grid.PyGridTableBase):
	def __init__(self, columns, data):
		wx.grid.PyGridTableBase.__init__(self)
		self.columns = columns
		self.data = data

	def GetNumberRows(self):
		return GetFetchHmRows(self.data)

	def GetNumberCols(self):
		return len(self.columns)

	def IsEmptyCell(self, row, col):
		return False

	def GetTypeName(self, row, col):
		return None

	def GetValue(self, row, col):
		if len(self.columns[col]) > 2 and self.columns[col][2] == "editButton":
			return ""
		else :
			return str(self.data[row][col+1])

	def SetValue(self, row, col, value):
		pass

	def GetColLabelValue(self, col):
		return self.columns[col][0]

	def GetRowLabelValue(self, row):
		return self.data[row][0]



class EditCellRender(wx.grid.PyGridCellRenderer):
	def __init__(self):
		wx.grid.PyGridCellRenderer.__init__(self)
		
		
	def Draw(self, grid, attr, dc, rect, row, col, isSelected):
		hAlign, vAlign = attr.GetAlignment()
		img = wx.Image("../media/edit.png", wx.BITMAP_TYPE_ANY)
		bitmap = img.ConvertToBitmap()
		w = img.GetWidth()
		h = img.GetHeight()

		dc.DrawBitmap(bitmap, rect.x + (rect.Width-w)/2, rect.y+ (rect.Height-h)/2, False)
				
class GridCtr(wx.Panel):
	def __init__(self, parent, columns, selectFun):
		wx.Panel.__init__(self, parent)
		
		self.selectFun = selectFun

		#sort
		sortChoiceList = ["ID (default)"]
		for col in columns:
			if(len(col) < 3):
				sortChoiceList += [col[0]]
		self.choiceSort = wx.Choice(self, -1, choices=sortChoiceList )
		self.Bind(wx.EVT_CHOICE, self.ChangeSort, self.choiceSort)

		self.checkAsc = wx.CheckBox(self, -1, "ascending")
		self.Bind(wx.EVT_CHECKBOX, self.ChangeSort, self.checkAsc)
		
		self.filterEdit =  wx.TextCtrl(self, -1, "", size=(180, -1))

		sizerSort = wx.BoxSizer(wx.HORIZONTAL)
		sizerSort.Add(self.choiceSort)
		sizerSort.AddSpacer(10)
		sizerSort.Add(self.checkAsc)
		for idx in range(5):
			sizerSort.AddSpacer(10)
		sizerSort.Add(self.filterEdit)

		self.table = GridDb(columns, self.selectFun())
		self.grid = wx.grid.Grid(self)
		self.editCol = -1
		self.editMode = False

		self.grid.SetTable(self.table, True)
		for idx in range(len(columns)):
			self.grid.SetColSize(idx, columns[idx][1])
			if len(columns[idx]) > 2 :
				if columns[idx][2] == "boolean":
					self.grid.SetColFormatBool(idx)
				elif columns[idx][2] == "editButton":
					self.SetEditCol(idx)
		
		self.grid.EnableEditing(False)
		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(sizerSort)
		sizer.AddSpacer(5)
		sizer.Add(self.grid, 1,  wx.EXPAND)
		self.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.LeftMouseButtonClick, self.grid)

		self.SetSizer(sizer)

				
	def ForceRefresh(self):
		self.table.data = self.selectFun()
		self.DoSort()
		self.grid.ForceRefresh()

	def LeftMouseButtonClick(self, event):
		col = event.GetCol()
		if col == self.editCol : 
			self.EditRow(event.GetRow())

	def AtachForm(self, form):
		self.form = form
		
	def EditRow(self, row):
		if self.editMode == False:
			self.editMode = True
			attr = wx.grid.GridCellAttr()
			attr.SetBackgroundColour(wx.Colour(154,205,50))
			self.grid.SetRowAttr(row, attr)
			self.grid.Refresh()
			
			self.form.EditMode(self.table.data[row][0])
		
	def SetEditCol(self, idx):
		self.editCol = idx
		attr = wx.grid.GridCellAttr()
		attr.SetRenderer( EditCellRender() )
		self.grid.SetColAttr(self.editCol,  attr)		
		
	def ChangeSort(self, event):
		self.DoSort()
		self.grid.ForceRefresh()
		
	def DoSort(self):	
		No = self.choiceSort.GetSelection()
		if self.checkAsc.GetValue():
			self.table.data = tuple(sorted(self.table.data, key=lambda item: item[No]))
		else:
			self.table.data = tuple(sorted(self.table.data, key=lambda item: item[No], reverse=True))		

	def StopEdit(self):
		self.editMode = False
		for idx in range(self.grid.GetNumberRows()):
			attr = wx.grid.GridCellAttr()
			attr.SetBackgroundColour(wx.NullColor)
			self.grid.SetRowAttr(idx, attr)
		self.grid.Refresh()
