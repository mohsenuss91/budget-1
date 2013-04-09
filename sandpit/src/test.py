#-*- coding: utf-8 -*-
import wx


class MyTab(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent)
		
		self.button1 = wx.Button(self, -1, "Button1")
		self.button2 = wx.Button(self, -1, "Button2")
		
		self.Bind(wx.EVT_BUTTON, self.ClickButton1, self.button1)
		self.Bind(wx.EVT_BUTTON, self.ClickButton2, self.button2)

		self.sizer = wx.BoxSizer(wx.VERTICAL)
		self.sizer.Add(self.button1, flag=wx.ALIGN_CENTER)
		self.sizer.AddSpacer(20)
		self.sizer.Add(self.button2, flag=wx.ALIGN_CENTER)
		self.SetSizer(self.sizer)
		
		self.button2.Hide()
		#self.sizer.Hide(self.button2)
		
		
	def ClickButton1(self, event):
		
		self.button2.Show(True)
		#self.sizer.Add(self.button2, flag=wx.ALIGN_CENTER)
		self.Layout()
		
	def ClickButton2(self, event):
		self.button2.Hide()

		
class MainWindow(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, -1, "Budget ver. 0.7", size=(1100, 650))
		self.Centre(wx.BOTH)
		panel = wx.Panel(self, -1)
		
		notebook = wx.Notebook(panel)
		notebook.AddPage(MyTab(notebook), "Tab1")
		notebook.AddPage(MyTab(notebook), "Tab2")

		
		sizer = wx.BoxSizer()
		sizer.Add(notebook, 1, wx.EXPAND)
		panel.SetSizer(sizer)


if __name__ == '__main__':
	app = wx.PySimpleApp()
	frame = MainWindow()
	frame.Show(True)
	app.MainLoop()
