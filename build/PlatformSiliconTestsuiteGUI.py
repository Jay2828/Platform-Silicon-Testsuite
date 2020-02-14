# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Platform Silicon Test Suite - Renoir", pos = wx.DefaultPosition, size = wx.Size( 788,700 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Renoir", wx.EmptyString, wx.ITEM_CHECK )
		self.m_menu1.Append( self.m_menuItem1 )
		self.m_menuItem1.Check( True )

		self.m_menuItem2 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Vermeer", wx.EmptyString, wx.ITEM_CHECK )
		self.m_menu1.Append( self.m_menuItem2 )

		self.m_menubar1.Append( self.m_menu1, u"Processor Family" )

		self.m_menu2 = wx.Menu()
		self.m_menuItem3 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Add...", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem3 )

		self.m_menubar1.Append( self.m_menu2, u"Wombat IP" )

		self.SetMenuBar( self.m_menubar1 )

		fgSizer49 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer49.SetFlexibleDirection( wx.BOTH )
		fgSizer49.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_panel17 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 775,725 ), wx.TAB_TRAVERSAL )
		bSizer18 = wx.BoxSizer( wx.VERTICAL )

		fgSizer201 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer201.SetFlexibleDirection( wx.BOTH )
		fgSizer201.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		m_choice2Choices = []
		self.m_choice2 = wx.Choice( self.m_panel17, wx.ID_ANY, wx.DefaultPosition, wx.Size( 125,-1 ), m_choice2Choices, 0 )
		self.m_choice2.SetSelection( 0 )
		fgSizer201.Add( self.m_choice2, 0, wx.ALL, 5 )

		fgSizer222 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer222.SetFlexibleDirection( wx.BOTH )
		fgSizer222.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button121 = wx.Button( self.m_panel17, wx.ID_ANY, u"Power On", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer222.Add( self.m_button121, 0, wx.ALL, 5 )

		fgSizer211 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer211.SetFlexibleDirection( wx.BOTH )
		fgSizer211.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button14 = wx.Button( self.m_panel17, wx.ID_ANY, u"Power Off", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer211.Add( self.m_button14, 0, wx.ALL, 5 )

		fgSizer23 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer23.SetFlexibleDirection( wx.BOTH )
		fgSizer23.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button15 = wx.Button( self.m_panel17, wx.ID_ANY, u"Cold Reset", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer23.Add( self.m_button15, 0, wx.ALL, 5 )

		fgSizer241 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer241.SetFlexibleDirection( wx.BOTH )
		fgSizer241.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button16 = wx.Button( self.m_panel17, wx.ID_ANY, u"Warm Reset", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer241.Add( self.m_button16, 0, wx.ALL, 5 )

		fgSizer30 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer30.SetFlexibleDirection( wx.BOTH )
		fgSizer30.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button19 = wx.Button( self.m_panel17, wx.ID_ANY, u"Unlock Wombat", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer30.Add( self.m_button19, 0, wx.ALL, 5 )


		fgSizer241.Add( fgSizer30, 1, wx.EXPAND, 5 )


		fgSizer23.Add( fgSizer241, 1, wx.EXPAND, 5 )


		fgSizer211.Add( fgSizer23, 1, wx.EXPAND, 5 )


		fgSizer222.Add( fgSizer211, 1, wx.EXPAND, 5 )


		fgSizer201.Add( fgSizer222, 1, wx.EXPAND, 5 )


		bSizer18.Add( fgSizer201, 1, wx.EXPAND, 5 )

		fgSizer17 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer17.SetFlexibleDirection( wx.BOTH )
		fgSizer17.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_panel18 = wx.Panel( self.m_panel17, wx.ID_ANY, wx.DefaultPosition, wx.Size( 750,700 ), wx.TAB_TRAVERSAL )
		fgSizer221 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer221.SetFlexibleDirection( wx.BOTH )
		fgSizer221.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_panel7 = wx.Panel( self.m_panel18, wx.ID_ANY, wx.DefaultPosition, wx.Size( 325,685 ), wx.TAB_TRAVERSAL )
		fgSizer20 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer20.SetFlexibleDirection( wx.BOTH )
		fgSizer20.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_treeCtrl1 = wx.TreeCtrl( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.Size( 325,685 ), wx.TR_DEFAULT_STYLE|wx.BORDER_NONE )
		fgSizer20.Add( self.m_treeCtrl1, 0, wx.ALL, 5 )


		self.m_panel7.SetSizer( fgSizer20 )
		self.m_panel7.Layout()
		fgSizer221.Add( self.m_panel7, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel8 = wx.Panel( self.m_panel18, wx.ID_ANY, wx.DefaultPosition, wx.Size( 400,700 ), wx.TAB_TRAVERSAL )
		fgSizer7 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer7.SetFlexibleDirection( wx.BOTH )
		fgSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.fusePanel = wx.Panel( self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.Size( 400,675 ), wx.BORDER_SUNKEN )
		self.fusePanel.Hide()

		bSizer21 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText21 = wx.StaticText( self.fusePanel, wx.ID_ANY, u"Fuse Window:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		self.m_staticText21.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, "Arial" ) )

		bSizer21.Add( self.m_staticText21, 0, wx.ALL, 5 )

		fgSizer21 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer21.SetFlexibleDirection( wx.BOTH )
		fgSizer21.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText9 = wx.StaticText( self.fusePanel, wx.ID_ANY, u"Fuse File:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		fgSizer21.Add( self.m_staticText9, 0, wx.ALL, 5 )

		self.m_filePicker1 = wx.FilePickerCtrl( self.fusePanel, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		fgSizer21.Add( self.m_filePicker1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


		bSizer21.Add( fgSizer21, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button11 = wx.Button( self.fusePanel, wx.ID_ANY, u"Fuse", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer21.Add( self.m_button11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.fusePanel.SetSizer( bSizer21 )
		self.fusePanel.Layout()
		fgSizer7.Add( self.fusePanel, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.readClkPanel = wx.Panel( self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.Size( 400,675 ), wx.BORDER_SUNKEN|wx.TAB_TRAVERSAL )
		self.readClkPanel.Hide()

		bSizer1111 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText21111 = wx.StaticText( self.readClkPanel, wx.ID_ANY, u"Read Clock Window:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21111.Wrap( -1 )

		self.m_staticText21111.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, "Arial" ) )

		bSizer1111.Add( self.m_staticText21111, 0, wx.ALL, 5 )

		fgSizer1111 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1111.SetFlexibleDirection( wx.BOTH )
		fgSizer1111.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		fgSizer1111.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer1111.Add( fgSizer1111, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button511 = wx.Button( self.readClkPanel, wx.ID_ANY, u"Read Clock", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1111.Add( self.m_button511, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.readClkPanel.SetSizer( bSizer1111 )
		self.readClkPanel.Layout()
		fgSizer7.Add( self.readClkPanel, 1, wx.EXPAND |wx.ALL, 5 )

		self.readPostCodesPanel = wx.Panel( self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.Size( 400,675 ), wx.BORDER_SUNKEN|wx.TAB_TRAVERSAL )
		self.readPostCodesPanel.Hide()

		bSizer11111 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText211111 = wx.StaticText( self.readPostCodesPanel, wx.ID_ANY, u"Read Postcodes Window:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText211111.Wrap( -1 )

		self.m_staticText211111.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, "Arial" ) )

		bSizer11111.Add( self.m_staticText211111, 0, wx.ALL, 5 )

		fgSizer11111 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer11111.SetFlexibleDirection( wx.BOTH )
		fgSizer11111.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		fgSizer11111.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer11111.Add( fgSizer11111, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button5111 = wx.Button( self.readPostCodesPanel, wx.ID_ANY, u"Read Postcodes", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11111.Add( self.m_button5111, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.readPostCodesPanel.SetSizer( bSizer11111 )
		self.readPostCodesPanel.Layout()
		fgSizer7.Add( self.readPostCodesPanel, 1, wx.EXPAND |wx.ALL, 5 )

		self.readVDDsPanel = wx.Panel( self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.Size( 400,675 ), wx.BORDER_SUNKEN|wx.TAB_TRAVERSAL )
		self.readVDDsPanel.Hide()

		bSizer111112 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText2111112 = wx.StaticText( self.readVDDsPanel, wx.ID_ANY, u"Read VDDs Window:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2111112.Wrap( -1 )

		self.m_staticText2111112.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, "Arial" ) )

		bSizer111112.Add( self.m_staticText2111112, 0, wx.ALL, 5 )

		fgSizer111112 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer111112.SetFlexibleDirection( wx.BOTH )
		fgSizer111112.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		fgSizer111112.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer111112.Add( fgSizer111112, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button51112 = wx.Button( self.readVDDsPanel, wx.ID_ANY, u"Read VDDs", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer111112.Add( self.m_button51112, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.readVDDsPanel.SetSizer( bSizer111112 )
		self.readVDDsPanel.Layout()
		fgSizer7.Add( self.readVDDsPanel, 1, wx.EXPAND |wx.ALL, 5 )

		self.trainConPanel = wx.Panel( self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.Size( 400,675 ), wx.BORDER_SUNKEN )
		self.trainConPanel.Hide()

		bSizer112 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel16 = wx.Panel( self.trainConPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer15 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText221 = wx.StaticText( self.m_panel16, wx.ID_ANY, u"Training Consistency Window:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText221.Wrap( -1 )

		self.m_staticText221.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, "Arial" ) )

		bSizer15.Add( self.m_staticText221, 0, wx.ALL, 5 )

		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		fgSizer13 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer13.SetFlexibleDirection( wx.BOTH )
		fgSizer13.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText24 = wx.StaticText( self.m_panel16, wx.ID_ANY, u"COM Port:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )

		fgSizer13.Add( self.m_staticText24, 0, wx.ALL, 5 )

		m_choice1Choices = [ u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8", u"9", u"10", u"11", u"12", u"13", u"14", u"15", u"16", u"17", u"18", u"19", u"20", u"21", u"22", u"23", u"24", u"25", u"26", u"27", u"28", u"29", u"30", u"31", u"32", u"33", u"34", u"35", u"36", u"37", u"38", u"39", u"40", u"41", u"42", u"43", u"44", u"45", u"46", u"47", u"48", u"49", u"50", u"51", u"52", u"53", u"54", u"55", u"56", u"57", u"58", u"59", u"60", u"61", u"62", u"63", u"64", u"65", u"66", u"67", u"68", u"69", u"70", u"71", u"72", u"73", u"74", u"75", u"76", u"77", u"78", u"79", u"80", u"81", u"82", u"83", u"84", u"85", u"86", u"87", u"88", u"89", u"90", u"91", u"92", u"93", u"94", u"95", u"96", u"97", u"98", u"99", u"10", u"101", u"102", u"103", u"104", u"105", u"106", u"107", u"108", u"109", u"110", u"111", u"112", u"113", u"114", u"115", u"116", u"117", u"118", u"119", u"120", u"121", u"122", u"123", u"124", u"125", u"126", u"127", u"128", u"129", u"131", u"132", u"133", u"134", u"135", u"136", u"137", u"138", u"139", u"140", u"141", u"142", u"143", u"144", u"145", u"146", u"147", u"148", u"149", u"150", u"151", u"152", u"153", u"154", u"155", u"156", u"157", u"158", u"159", u"160", u"161", u"162", u"163", u"164", u"165", u"166", u"167", u"168", u"169", u"170", u"171", u"172", u"173", u"174", u"175", u"176", u"177", u"178", u"179", u"180", u"181", u"182", u"183", u"184", u"185", u"186", u"187", u"188", u"189", u"190", u"191", u"192", u"193", u"194", u"195", u"196", u"197", u"198", u"199", u"200", u"201", u"202", u"203", u"204", u"205", u"206", u"207", u"208", u"209", u"210", u"211", u"212", u"213", u"214", u"215", u"216", u"217", u"218", u"219", u"220", u"221", u"222", u"223", u"224", u"225", u"226", u"227", u"228", u"229", u"230", u"231", u"232", u"234", u"235", u"236", u"237", u"238", u"239", u"240", u"241", u"242", u"243", u"244", u"245", u"246", u"247", u"248", u"249", u"250", u"251", u"252", u"253", u"254", u"255", u"256" ]
		self.m_choice1 = wx.Choice( self.m_panel16, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0 )
		self.m_choice1.SetSelection( 0 )
		fgSizer13.Add( self.m_choice1, 0, wx.ALL, 5 )

		self.m_staticText25 = wx.StaticText( self.m_panel16, wx.ID_ANY, u"Number of Reboots:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )

		fgSizer13.Add( self.m_staticText25, 0, wx.ALL, 5 )

		self.m_textCtrl121 = wx.TextCtrl( self.m_panel16, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer13.Add( self.m_textCtrl121, 0, wx.ALL, 5 )

		self.m_staticText26 = wx.StaticText( self.m_panel16, wx.ID_ANY, u"Output File Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )

		fgSizer13.Add( self.m_staticText26, 0, wx.ALL, 5 )

		self.m_textCtrl13 = wx.TextCtrl( self.m_panel16, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer13.Add( self.m_textCtrl13, 0, wx.ALL, 5 )

		self.m_checkBox1 = wx.CheckBox( self.m_panel16, wx.ID_ANY, u"Fuse File:", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer13.Add( self.m_checkBox1, 0, wx.ALL, 5 )

		self.m_filePicker2 = wx.FilePickerCtrl( self.m_panel16, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.m_filePicker2.Hide()

		fgSizer13.Add( self.m_filePicker2, 0, wx.ALL, 5 )


		bSizer12.Add( fgSizer13, 0, 0, 5 )

		self.m_staticline1 = wx.StaticLine( self.m_panel16, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer12.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_checkBox12 = wx.CheckBox( self.m_panel16, wx.ID_ANY, u"Custom Settings", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_checkBox12, 0, wx.ALL, 5 )


		bSizer15.Add( bSizer12, 1, wx.EXPAND, 5 )


		self.m_panel16.SetSizer( bSizer15 )
		self.m_panel16.Layout()
		bSizer15.Fit( self.m_panel16 )
		bSizer112.Add( self.m_panel16, 0, wx.ALL, 5 )

		self.m_panel15 = wx.Panel( self.trainConPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 350,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel15.Hide()

		fgSizer14 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer14.SetFlexibleDirection( wx.BOTH )
		fgSizer14.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_checkBox2 = wx.CheckBox( self.m_panel15, wx.ID_ANY, u"Breakpoint", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer14.Add( self.m_checkBox2, 0, wx.ALL, 5 )

		self.m_checkBox3 = wx.CheckBox( self.m_panel15, wx.ID_ANY, u"Username/Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer14.Add( self.m_checkBox3, 0, wx.ALL, 5 )

		self.m_staticText27 = wx.StaticText( self.m_panel15, wx.ID_ANY, u"Username:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )

		self.m_staticText27.Hide()

		fgSizer14.Add( self.m_staticText27, 0, wx.ALL, 5 )

		self.m_textCtrl15 = wx.TextCtrl( self.m_panel15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl15.Hide()

		fgSizer14.Add( self.m_textCtrl15, 0, wx.ALL, 5 )

		self.m_staticText28 = wx.StaticText( self.m_panel15, wx.ID_ANY, u"Password:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )

		self.m_staticText28.Hide()

		fgSizer14.Add( self.m_staticText28, 0, wx.ALL, 5 )

		self.m_textCtrl16 = wx.TextCtrl( self.m_panel15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl16.Hide()

		fgSizer14.Add( self.m_textCtrl16, 0, wx.ALL, 5 )

		self.m_checkBox4 = wx.CheckBox( self.m_panel15, wx.ID_ANY, u"ABL Timeout:", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer14.Add( self.m_checkBox4, 0, wx.ALL, 5 )

		self.m_textCtrl17 = wx.TextCtrl( self.m_panel15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl17.Hide()

		fgSizer14.Add( self.m_textCtrl17, 0, wx.ALL, 5 )

		self.m_checkBox5 = wx.CheckBox( self.m_panel15, wx.ID_ANY, u"1D String:", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer14.Add( self.m_checkBox5, 0, wx.ALL, 5 )

		self.m_dirPicker1 = wx.DirPickerCtrl( self.m_panel15, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		self.m_dirPicker1.Hide()

		fgSizer14.Add( self.m_dirPicker1, 0, wx.ALL, 5 )

		self.m_checkBox6 = wx.CheckBox( self.m_panel15, wx.ID_ANY, u"2D String:", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer14.Add( self.m_checkBox6, 0, wx.ALL, 5 )

		self.m_dirPicker2 = wx.DirPickerCtrl( self.m_panel15, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		self.m_dirPicker2.Hide()

		fgSizer14.Add( self.m_dirPicker2, 0, wx.ALL, 5 )

		self.m_checkBox7 = wx.CheckBox( self.m_panel15, wx.ID_ANY, u"End-Flag String:", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer14.Add( self.m_checkBox7, 0, wx.ALL, 5 )

		self.m_textCtrl18 = wx.TextCtrl( self.m_panel15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl18.Hide()

		fgSizer14.Add( self.m_textCtrl18, 0, wx.ALL, 5 )

		self.m_staticText29 = wx.StaticText( self.m_panel15, wx.ID_ANY, u"End-Flag Timeout:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )

		self.m_staticText29.Hide()

		fgSizer14.Add( self.m_staticText29, 0, wx.ALL, 5 )

		self.m_textCtrl14 = wx.TextCtrl( self.m_panel15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl14.Hide()

		fgSizer14.Add( self.m_textCtrl14, 0, wx.ALL, 5 )

		self.m_checkBox8 = wx.CheckBox( self.m_panel15, wx.ID_ANY, u"Connect to SUT IP:", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer14.Add( self.m_checkBox8, 0, wx.ALL, 5 )

		self.m_textCtrl19 = wx.TextCtrl( self.m_panel15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl19.Hide()

		fgSizer14.Add( self.m_textCtrl19, 0, wx.ALL, 5 )

		self.m_checkBox9 = wx.CheckBox( self.m_panel15, wx.ID_ANY, u"MST Loops:", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer14.Add( self.m_checkBox9, 0, wx.ALL, 5 )

		self.m_textCtrl20 = wx.TextCtrl( self.m_panel15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl20.Hide()

		fgSizer14.Add( self.m_textCtrl20, 0, wx.ALL, 5 )

		self.m_checkBox10 = wx.CheckBox( self.m_panel15, wx.ID_ANY, u"Memory Snapshot:", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer14.Add( self.m_checkBox10, 0, wx.ALL, 5 )

		self.m_textCtrl21 = wx.TextCtrl( self.m_panel15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl21.Hide()

		fgSizer14.Add( self.m_textCtrl21, 0, wx.ALL, 5 )

		self.m_checkBox11 = wx.CheckBox( self.m_panel15, wx.ID_ANY, u"Parsed-Log Only", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer14.Add( self.m_checkBox11, 0, wx.ALL, 5 )


		self.m_panel15.SetSizer( fgSizer14 )
		self.m_panel15.Layout()
		bSizer112.Add( self.m_panel15, 0, wx.ALL, 5 )

		fgSizer24 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer24.SetFlexibleDirection( wx.BOTH )
		fgSizer24.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		fgSizer24.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer112.Add( fgSizer24, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button111 = wx.Button( self.trainConPanel, wx.ID_ANY, u"Start Test", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer112.Add( self.m_button111, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.trainConPanel.SetSizer( bSizer112 )
		self.trainConPanel.Layout()
		fgSizer7.Add( self.trainConPanel, 1, wx.EXPAND |wx.ALL, 5 )

		self.voltVSTempPanel = wx.Panel( self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.Size( 400,675 ), wx.BORDER_SUNKEN|wx.TAB_TRAVERSAL )
		self.voltVSTempPanel.Hide()

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText13 = wx.StaticText( self.voltVSTempPanel, wx.ID_ANY, u"Voltage vs Frequency Window:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		self.m_staticText13.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		bSizer9.Add( self.m_staticText13, 0, wx.ALL, 5 )

		fgSizer19 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer19.SetFlexibleDirection( wx.BOTH )
		fgSizer19.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		m_radioBox1Choices = [ u"50°C", u"70°C", u"90°C" ]
		self.m_radioBox1 = wx.RadioBox( self.voltVSTempPanel, wx.ID_ANY, u"Temperature", wx.DefaultPosition, wx.DefaultSize, m_radioBox1Choices, 1, wx.RA_SPECIFY_COLS )
		self.m_radioBox1.SetSelection( 0 )
		fgSizer19.Add( self.m_radioBox1, 0, wx.ALL, 5 )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		fgSizer202 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer202.SetFlexibleDirection( wx.BOTH )
		fgSizer202.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText15 = wx.StaticText( self.voltVSTempPanel, wx.ID_ANY, u"Chiller COM:   ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		fgSizer202.Add( self.m_staticText15, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		m_choice3Choices = [ u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8", u"9", u"10", u"11", u"12", u"13", u"14", u"15", u"16", u"17", u"18", u"19", u"20", u"21", u"22", u"23", u"24", u"25", u"26", u"27", u"28", u"29", u"30", u"31", u"32", u"33", u"34", u"35", u"36", u"37", u"38", u"39", u"40", u"41", u"42", u"43", u"44", u"45", u"46", u"47", u"48", u"49", u"50", u"51", u"52", u"53", u"54", u"55", u"56", u"57", u"58", u"59", u"60", u"61", u"62", u"63", u"64", u"65", u"66", u"67", u"68", u"69", u"70", u"71", u"72", u"73", u"74", u"75", u"76", u"77", u"78", u"79", u"80", u"81", u"82", u"83", u"84", u"85", u"86", u"87", u"88", u"89", u"90", u"91", u"92", u"93", u"94", u"95", u"96", u"97", u"98", u"99", u"10", u"101", u"102", u"103", u"104", u"105", u"106", u"107", u"108", u"109", u"110", u"111", u"112", u"113", u"114", u"115", u"116", u"117", u"118", u"119", u"120", u"121", u"122", u"123", u"124", u"125", u"126", u"127", u"128", u"129", u"131", u"132", u"133", u"134", u"135", u"136", u"137", u"138", u"139", u"140", u"141", u"142", u"143", u"144", u"145", u"146", u"147", u"148", u"149", u"150", u"151", u"152", u"153", u"154", u"155", u"156", u"157", u"158", u"159", u"160", u"161", u"162", u"163", u"164", u"165", u"166", u"167", u"168", u"169", u"170", u"171", u"172", u"173", u"174", u"175", u"176", u"177", u"178", u"179", u"180", u"181", u"182", u"183", u"184", u"185", u"186", u"187", u"188", u"189", u"190", u"191", u"192", u"193", u"194", u"195", u"196", u"197", u"198", u"199", u"200", u"201", u"202", u"203", u"204", u"205", u"206", u"207", u"208", u"209", u"210", u"211", u"212", u"213", u"214", u"215", u"216", u"217", u"218", u"219", u"220", u"221", u"222", u"223", u"224", u"225", u"226", u"227", u"228", u"229", u"230", u"231", u"232", u"234", u"235", u"236", u"237", u"238", u"239", u"240", u"241", u"242", u"243", u"244", u"245", u"246", u"247", u"248", u"249", u"250", u"251", u"252", u"253", u"254", u"255", u"256" ]
		self.m_choice3 = wx.Choice( self.voltVSTempPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice3Choices, 0 )
		self.m_choice3.SetSelection( 0 )
		fgSizer202.Add( self.m_choice3, 0, wx.ALL, 5 )


		bSizer10.Add( fgSizer202, 0, 0, 5 )

		fgSizer22 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer22.SetFlexibleDirection( wx.BOTH )
		fgSizer22.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText16 = wx.StaticText( self.voltVSTempPanel, wx.ID_ANY, u"SUT IP:             ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )

		fgSizer22.Add( self.m_staticText16, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl11 = wx.TextCtrl( self.voltVSTempPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer22.Add( self.m_textCtrl11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer10.Add( fgSizer22, 0, 0, 5 )

		fgSizer231 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer231.SetFlexibleDirection( wx.BOTH )
		fgSizer231.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText17 = wx.StaticText( self.voltVSTempPanel, wx.ID_ANY, u"Output Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		fgSizer231.Add( self.m_staticText17, 0, wx.ALL, 5 )

		self.m_textCtrl12 = wx.TextCtrl( self.voltVSTempPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer231.Add( self.m_textCtrl12, 0, wx.ALL, 5 )


		bSizer10.Add( fgSizer231, 1, wx.EXPAND, 5 )

		fgSizer212 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer212.SetFlexibleDirection( wx.BOTH )
		fgSizer212.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_checkBox13 = wx.CheckBox( self.voltVSTempPanel, wx.ID_ANY, u"Fuse File:  ", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer212.Add( self.m_checkBox13, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_filePicker3 = wx.FilePickerCtrl( self.voltVSTempPanel, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		fgSizer212.Add( self.m_filePicker3, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


		bSizer10.Add( fgSizer212, 0, 0, 5 )


		fgSizer19.Add( bSizer10, 1, wx.EXPAND, 5 )

		m_radioBox2Choices = [ u"0", u"1", u"2", u"3", u"4", u"5", u"6", u"7" ]
		self.m_radioBox2 = wx.RadioBox( self.voltVSTempPanel, wx.ID_ANY, u"Starting Core", wx.DefaultPosition, wx.DefaultSize, m_radioBox2Choices, 1, wx.RA_SPECIFY_COLS )
		self.m_radioBox2.SetSelection( 0 )
		fgSizer19.Add( self.m_radioBox2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		fgSizer242 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer242.SetFlexibleDirection( wx.BOTH )
		fgSizer242.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		m_radioBox3Choices = [ u"0", u"1", u"2", u"3", u"4", u"5", u"6", u"7" ]
		self.m_radioBox3 = wx.RadioBox( self.voltVSTempPanel, wx.ID_ANY, u"Ending Core", wx.DefaultPosition, wx.DefaultSize, m_radioBox3Choices, 1, wx.RA_SPECIFY_COLS )
		self.m_radioBox3.SetSelection( 7 )
		fgSizer242.Add( self.m_radioBox3, 0, wx.ALL|wx.EXPAND, 5 )

		m_radioBox4Choices = [ u"0.90", u"0.95", u"1.00", u"1.05", u"1.10", u"1.15", u"1.20", u"1.25", u"1.30", u"1.35", u"1.40", u"1.45" ]
		self.m_radioBox4 = wx.RadioBox( self.voltVSTempPanel, wx.ID_ANY, u"Starting Voltage", wx.DefaultPosition, wx.DefaultSize, m_radioBox4Choices, 1, wx.RA_SPECIFY_COLS )
		self.m_radioBox4.SetSelection( 0 )
		fgSizer242.Add( self.m_radioBox4, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer19.Add( fgSizer242, 1, wx.EXPAND, 5 )


		bSizer9.Add( fgSizer19, 0, 0, 5 )


		bSizer9.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_gauge1 = wx.Gauge( self.voltVSTempPanel, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL|wx.GA_SMOOTH )
		self.m_gauge1.SetValue( 0 )
		self.m_gauge1.Hide()

		bSizer9.Add( self.m_gauge1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_button112 = wx.Button( self.voltVSTempPanel, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button112, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.voltVSTempPanel.SetSizer( bSizer9 )
		self.voltVSTempPanel.Layout()
		fgSizer7.Add( self.voltVSTempPanel, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel8.SetSizer( fgSizer7 )
		self.m_panel8.Layout()
		fgSizer221.Add( self.m_panel8, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		self.m_panel18.SetSizer( fgSizer221 )
		self.m_panel18.Layout()
		fgSizer17.Add( self.m_panel18, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer18.Add( fgSizer17, 1, wx.EXPAND, 5 )


		self.m_panel17.SetSizer( bSizer18 )
		self.m_panel17.Layout()
		fgSizer49.Add( self.m_panel17, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( fgSizer49 )
		self.Layout()
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.renoirSelect, id = self.m_menuItem1.GetId() )
		self.Bind( wx.EVT_MENU, self.vermeerSelect, id = self.m_menuItem2.GetId() )
		self.Bind( wx.EVT_MENU, self.newIPSelect, id = self.m_menuItem3.GetId() )
		self.m_button121.Bind( wx.EVT_BUTTON, self.powerOn )
		self.m_button14.Bind( wx.EVT_BUTTON, self.powerOff )
		self.m_button15.Bind( wx.EVT_BUTTON, self.coldReset )
		self.m_button16.Bind( wx.EVT_BUTTON, self.warmReset )
		self.m_button19.Bind( wx.EVT_BUTTON, self.unlockWombat )
		self.m_treeCtrl1.Bind( wx.EVT_TREE_ITEM_ACTIVATED, self.itemSelect )
		self.m_button11.Bind( wx.EVT_BUTTON, self.fuse )
		self.m_button511.Bind( wx.EVT_BUTTON, self.readClk )
		self.m_button5111.Bind( wx.EVT_BUTTON, self.readPostcodes )
		self.m_button51112.Bind( wx.EVT_BUTTON, self.readVDDs )
		self.m_checkBox1.Bind( wx.EVT_CHECKBOX, self.guiInteract )
		self.m_checkBox12.Bind( wx.EVT_CHECKBOX, self.guiInteract )
		self.m_checkBox3.Bind( wx.EVT_CHECKBOX, self.guiInteract )
		self.m_checkBox4.Bind( wx.EVT_CHECKBOX, self.guiInteract )
		self.m_checkBox5.Bind( wx.EVT_CHECKBOX, self.guiInteract )
		self.m_checkBox6.Bind( wx.EVT_CHECKBOX, self.guiInteract )
		self.m_checkBox7.Bind( wx.EVT_CHECKBOX, self.guiInteract )
		self.m_checkBox8.Bind( wx.EVT_CHECKBOX, self.guiInteract )
		self.m_checkBox9.Bind( wx.EVT_CHECKBOX, self.guiInteract )
		self.m_checkBox10.Bind( wx.EVT_CHECKBOX, self.guiInteract )
		self.m_checkBox11.Bind( wx.EVT_CHECKBOX, self.guiInteract )
		self.m_button111.Bind( wx.EVT_BUTTON, self.trainConsistency )
		self.m_checkBox13.Bind( wx.EVT_CHECKBOX, self.guiInteract )
		self.m_button112.Bind( wx.EVT_BUTTON, self.voltVsFreqMarg )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def renoirSelect( self, event ):
		event.Skip()

	def vermeerSelect( self, event ):
		event.Skip()

	def newIPSelect( self, event ):
		event.Skip()

	def powerOn( self, event ):
		event.Skip()

	def powerOff( self, event ):
		event.Skip()

	def coldReset( self, event ):
		event.Skip()

	def warmReset( self, event ):
		event.Skip()

	def unlockWombat( self, event ):
		event.Skip()

	def itemSelect( self, event ):
		event.Skip()

	def fuse( self, event ):
		event.Skip()

	def readClk( self, event ):
		event.Skip()

	def readPostcodes( self, event ):
		event.Skip()

	def readVDDs( self, event ):
		event.Skip()

	def guiInteract( self, event ):
		event.Skip()











	def trainConsistency( self, event ):
		event.Skip()


	def voltVsFreqMarg( self, event ):
		event.Skip()


