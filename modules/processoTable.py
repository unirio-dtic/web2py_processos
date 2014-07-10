# -*- coding: utf-8 -*-
from gluon.html import *
from DefaultTable import *

class ProcessoTable(DefaultTable):
	def __init__(self, contentsDict):
		DefaultTable.__init__(self, contentsDict)

	def printTable(self, tableClass=None):
		return TABLE( self.getTableBody(), _class=tableClass)

	def getTableRows(self):
		rows = []
		for contentKey, contentValue in sorted( self.contents.iteritems() ):
			rows.append( TR( self.getRowContent(contentKey, contentValue), _class=self._bodyTRclass) )
		return rows

	def getRowContent(self, contentKey, contentValue):
		row = []
		row.append( TD(contentKey, _class=self._bodyTRclass) )
		row.append( TD(contentValue, _class=self._bodyTRclass) )
		return row
	