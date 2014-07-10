# -*- coding: utf-8 -*-
from gluon.html import *
from DefaultTable import *

class TramitacoesTable(DefaultTable):
	def __init__(self, contents, titleList):
		DefaultTable.__init__(self, contents, titleList)

	def getRowContent(self, content):
		row = []
		row.append( TD(content['DESCR_FLUXO'], _class=self._bodyTRclass) )
		row.append( TD(content['DT_ENVIO'], _class=self._bodyTRclass) )
		row.append( TD(content['DT_RECEBIMENTO'], _class=self._bodyTRclass) )
		row.append( TD(content['ORIGEM'].decode('1252').encode('utf-8'), _class=self._bodyTRclass) )
		row.append( TD(content['DESTINO'].decode('1252').encode('utf-8'), _class=self._bodyTRclass) )
		row.append( TD(content['DESPACHO'], _class=self._bodyTRclass) )
		row.append( TD(content['RECEBIDO'], _class=self._bodyTRclass) )
		return row
	