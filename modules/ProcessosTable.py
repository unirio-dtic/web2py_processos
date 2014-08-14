# -*- coding: utf-8 -*-
from gluon.html import *
from DefaultTable import *

class ProcessosTable(DefaultTable):
    def __init__(self, contents, titleList):
        DefaultTable.__init__(self, contents, titleList)

    def getRowContent(self, content):
        link = A(content['NUM_PROCESSO'], _href=URL('processo','index', vars={'ID_DOCUMENTO' : content['ID_DOCUMENTO']} ))
        row = []
        row.append( TD(link, _class=self._bodyTRclass) )
        row.append( TD(content['NOME_INTERESSADO'], _class=self._bodyTRclass) )
        row.append( TD(content['DT_ALTERACAO'], _class=self._bodyTRclass) )
        return row