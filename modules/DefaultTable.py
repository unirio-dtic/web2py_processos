# -*- coding: utf-8 -*-
from gluon.html import *

class DefaultTable(object):
	contents = None
	_titleList = None
	_headTRclass = None
	_headTDclass = None
	_bodyTRclass = None
	_bodyTDclass = None

	def __init__(self, contents, titleList=None):
		self.contents = contents
		self._titleList = titleList

	def printTable(self, tableClass=None):
		return TABLE( self.getTableHead(), self.getTableBody(), _class=tableClass)

	#print THEAD(TR(TH('<hello>')), _class='test', _id=0)
	def getTableHead(self, tdClass=None, trClass=None):
		heads = []
		for title in self._titleList:
			heads.append( TD( SPAN(title), _class=self._headTDclass ) )
		return THEAD( TR( heads, _class=self._headTRclass) )

	def getTableBody(self):
		return TBODY( self.getTableRows() )

	def getTableRows(self):
		rows = []
		for content in self.contents:
			rows.append( TR( self.getRowContent(content), _class=self._bodyTRclass) )
		return rows

	def getRowContent(self, content):
		pass
