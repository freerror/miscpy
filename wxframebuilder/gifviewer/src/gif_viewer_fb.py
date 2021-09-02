# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.9.0 Jun 19 2021)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv

###########################################################################
## Class frameMain
###########################################################################

class frameMain ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Gif Viewer", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 950,750 ), wx.DefaultSize )

		bSizerFrame = wx.BoxSizer( wx.VERTICAL )

		self.panelMain = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizerMain = wx.BoxSizer( wx.VERTICAL )

		bSizerSplitT = wx.BoxSizer( wx.HORIZONTAL )

		bSizerSplitT.SetMinSize( wx.Size( -1,50 ) )
		sbSizerDir = wx.StaticBoxSizer( wx.StaticBox( self.panelMain, wx.ID_ANY, u"Images Directory" ), wx.HORIZONTAL )

		self.dirPicker = wx.DirPickerCtrl( sbSizerDir.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select image directory", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_USE_TEXTCTRL )
		sbSizerDir.Add( self.dirPicker, 1, wx.ALL|wx.EXPAND, 15 )


		bSizerSplitT.Add( sbSizerDir, 1, wx.ALL, 10 )


		bSizerMain.Add( bSizerSplitT, 0, wx.EXPAND, 0 )

		bSizerSplitB = wx.BoxSizer( wx.HORIZONTAL )

		bSizerSplitL = wx.BoxSizer( wx.VERTICAL )

		sbSizerList = wx.StaticBoxSizer( wx.StaticBox( self.panelMain, wx.ID_ANY, u"File List" ), wx.VERTICAL )

		listBoxFilesChoices = []
		self.listBoxFiles = wx.ListBox( sbSizerList.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listBoxFilesChoices, 0 )
		sbSizerList.Add( self.listBoxFiles, 1, wx.ALL|wx.EXPAND, 15 )


		bSizerSplitL.Add( sbSizerList, 1, wx.ALL|wx.EXPAND, 10 )


		bSizerSplitB.Add( bSizerSplitL, 1, wx.EXPAND, 0 )

		bSizerSplitR = wx.BoxSizer( wx.VERTICAL )

		sbSizerViewer = wx.StaticBoxSizer( wx.StaticBox( self.panelMain, wx.ID_ANY, u"Viewer" ), wx.VERTICAL )

		self.animCtrl = wx.adv.AnimationCtrl( sbSizerViewer.GetStaticBox(), wx.ID_ANY, wx.adv.NullAnimation, wx.DefaultPosition, wx.DefaultSize, wx.adv.AC_NO_AUTORESIZE )
		sbSizerViewer.Add( self.animCtrl, 1, wx.ALL|wx.EXPAND, 5 )


		bSizerSplitR.Add( sbSizerViewer, 1, wx.ALL|wx.EXPAND, 10 )


		bSizerSplitB.Add( bSizerSplitR, 1, wx.EXPAND, 0 )


		bSizerMain.Add( bSizerSplitB, 1, wx.EXPAND, 5 )


		self.panelMain.SetSizer( bSizerMain )
		self.panelMain.Layout()
		bSizerMain.Fit( self.panelMain )
		bSizerFrame.Add( self.panelMain, 1, wx.ALL|wx.EXPAND, 0 )


		self.SetSizer( bSizerFrame )
		self.Layout()
		bSizerFrame.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.dirPicker.Bind( wx.EVT_DIRPICKER_CHANGED, self.m_dirPicker2OnDirChanged )
		self.listBoxFiles.Bind( wx.EVT_LISTBOX, self.m_listBoxFilesOnListBox )
		self.listBoxFiles.Bind( wx.EVT_LISTBOX_DCLICK, self.m_listBoxFilesOnListBoxDClick )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def m_dirPicker2OnDirChanged( self, event ):
		event.Skip()

	def m_listBoxFilesOnListBox( self, event ):
		event.Skip()

	def m_listBoxFilesOnListBoxDClick( self, event ):
		event.Skip()


