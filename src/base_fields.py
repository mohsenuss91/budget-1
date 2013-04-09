import wx
import datetime
from db import *
		
class BaseField(wx.Panel):
	def __init__(self, parent, header):
		wx.Panel.__init__(self, parent)
		self.header = header
		self.field = 0
		
		label = wx.StaticText(self, -1, header, size=(-1, -1))		
		self.sizer = wx.BoxSizer(wx.VERTICAL)
		self.sizer.Add(label, flag=wx.ALIGN_CENTER)
		self.SetSizer(self.sizer)
		
	def	GetValue(self):
		return self.field.GetValue()

	def	SetValue(self, value):
		return self.field.SetValue(value)
		
	def Validate(self):
		return 0

	def SetFieldColor(self, newColor):
		self.field.SetBackgroundColour(newColor)
	
	def SetDefaultFieldColor(self):	
		self.field.SetBackgroundColour(wx.NullColor)
		
				
class EditField(BaseField):
	def __init__(self, parent, header, fieldWidth=-1, defaultText=""):
		BaseField.__init__(self, parent, header)
		self.field = wx.TextCtrl(self, -1, defaultText, size=(fieldWidth, -1))
		self.sizer.Add(self.field, flag=wx.ALIGN_CENTER)
		
class DateField(EditField):
	def __init__(self, parent, header, fieldWidth=-1):
		EditField.__init__(self, parent, header, fieldWidth, str(datetime.datetime.now().date()))


class MoneyField(EditField):
	def __init__(self, parent, header, fieldWidth=-1):
		EditField.__init__(self, parent, header, fieldWidth)


class DropdownField(BaseField):
	def __init__(self, parent, header, table):
		BaseField.__init__(self, parent, header)
		self.table = table	
		self.field = wx.Choice(self, -1, choices=GetSelectNames(self.table) )
		self.sizer.Add(self.field, flag=wx.ALIGN_CENTER)

	def	GetValue(self):
		return GetSelectIdByName( self.table, self.field.GetStringSelection() )	

	def SetValue(self, value):
		for row in self.table:
			if row[0] == value :
				self.field.SetStringSelection(row[1])

		
class CheckboxField(BaseField):
	def __init__(self, parent,header):
		BaseField.__init__(parent, header)
		
		
