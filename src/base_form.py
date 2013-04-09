#-*- coding: utf-8 -*-

import wx
import datetime
from db import *
from useful import *
from base_fields import *

class BaseTab():
	pass

class BaseForm(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent)
		self.trigger = []
		self.EditRowID = -1
		self.fields =[]
		
		sizerAdd = wx.BoxSizer(wx.VERTICAL)
		bmpAdd = wx.Image("../media/add.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
		self.buttonAdd = wx.BitmapButton(self, -1, bmpAdd)
		self.Bind(wx.EVT_BUTTON, self.ClickAdd, self.buttonAdd)
		sizerAdd.AddSpacer(2)
		sizerAdd.Add(self.buttonAdd, flag=wx.ALIGN_CENTER)

		sizerCancel = wx.BoxSizer(wx.VERTICAL)
		bmpCancel = wx.Image("../media/cancel.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
		self.buttonCancel = wx.BitmapButton(self, -1, bmpCancel, name="cancel")
		self.Bind(wx.EVT_BUTTON, self.ClickCancel, self.buttonCancel)
		sizerCancel.AddSpacer(2)
		sizerCancel.Add(self.buttonCancel, flag=wx.ALIGN_CENTER)
		self.buttonCancel.Show(False)
		
		sizerDelete = wx.BoxSizer(wx.VERTICAL)
		bmpDelete = wx.Image("../media/delete.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
		self.buttonDelete = wx.BitmapButton(self, -1, bmpDelete)
		self.Bind(wx.EVT_BUTTON, self.ClickDelete, self.buttonDelete)
		sizerDelete.AddSpacer(2)
		sizerDelete.Add(self.buttonDelete, flag=wx.ALIGN_CENTER)
		self.buttonDelete.Show(False)				
		
		self.fieldsSizer = wx.BoxSizer(wx.HORIZONTAL)
		sizer = wx.BoxSizer(wx.HORIZONTAL)
		sizer.Add(self.fieldsSizer)
		#sizer.AddSpacer(5)
		sizer.Add(sizerAdd)
		sizer.AddSpacer(10)
		sizer.Add(sizerCancel)
		sizer.AddSpacer(10)
		sizer.Add(sizerDelete)		
		self.SetSizer(sizer)
		
	def	ForceRefresh(self):
		for ctr in self.trigger:
			ctr.ForceRefresh()
	
	def EditMode(self, ID):
		self.EditRowID = ID

		editColor = wx.Colour(154,205,50) 
		for field in self.fields:
			field.SetFieldColor(editColor)
		
		bmpSave = wx.Image("../media/save.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
		self.buttonAdd.SetBitmapLabel(bmpSave)

		self.buttonCancel.Show(True)
		self.buttonDelete.Show(True)
					
		self.OnEditMode()
		self.Layout()

		
	def AddMode(self):
		self.EditRowID = -1
		for field in self.fields:
			field.SetFieldColor(wx.NullColor)	
		
		bmpAdd = wx.Image("../media/add.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
		self.buttonAdd.SetBitmapLabel(bmpAdd)
		self.buttonCancel.Show(False)	
		self.buttonDelete.Show(False)	
			
	def OnEditMode(self):
		pass

	def SubscribeForRefresh(self, ctr):
		self.trigger += [ctr]
		
	def ClickAdd(self, event):
		if self.EditRowID < 0:
			self.OnClickAdd(event)
		else:
			self.OnClickUpdate(event)
			self.AddMode()	

	def ClickCancel(self, event):
		self.AddMode()
		
	def ClickDelete(self, event):
		dlg = wx.MessageDialog(self, 'Are you sure, you want to remove row ?','Delete row', wx.YES_NO | wx.ICON_WARNING)
		result = dlg.ShowModal()
		dlg.Destroy()
		if result == wx.ID_YES:
			self.OnClickDelete(event)
				
	def OnClickAdd(self, event):
		pass	
		
	def OnClickUpdate(self, event):
		pass
					
	def OnClickDelete(self, event):
		pass

	def AddField(self, field):
		self.fields += [field]
		self.fieldsSizer.Add(field)
		self.fieldsSizer.AddSpacer(10)
		
