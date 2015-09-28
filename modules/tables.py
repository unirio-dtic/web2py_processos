# -*- coding: utf-8 -*-
import datetime
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
        return TABLE(self.getTableHead(), self.getTableBody(), _class=tableClass)

    # print THEAD(TR(TH('<hello>')), _class='test', _id=0)
    def getTableHead(self, tdClass=None, trClass=None):
        heads = []
        for title in self._titleList:
            heads.append(TD(SPAN(title), _class=self._headTDclass))
        return THEAD(TR(heads, _class=self._headTRclass))

    def getTableBody(self):
        return TBODY(self.getTableRows())

    def getTableRows(self):
        rows = []
        for content in self.contents:
            rows.append(TR(self.getRowContent(content), _class=self._bodyTRclass))
        return rows

    def getRowContent(self, content):
        pass


class ProcessosTable(DefaultTable):
    def __init__(self, contents, titleList):
        DefaultTable.__init__(self, contents, titleList)

    def getRowContent(self, content):
        link = A(content['NUM_PROCESSO'], _href=URL('processo','index', vars={'ID_DOCUMENTO' : content['ID_DOCUMENTO']} ))
        row = []
        row.append( TD(link, _class=self._bodyTRclass) )
        row.append( TD(content['NOME_INTERESSADO'], _class=self._bodyTRclass) )
        row.append( TD(datetime.datetime.strptime(content['DT_ALTERACAO'], '%Y-%m-%d').strftime('%d/%m/%Y'), _class=self._bodyTRclass) )
        return row


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


class TramitacoesTable(DefaultTable):
    def getRowContent(self, content):
        """
        :type content: dict
        """
        row = []
        # TODO remover esse hack escroto e ver pq a view não está retornando DESCR_FLUXO
        if 'DESCR_FLUXO' in content:
            row.append(TD(content['DESCR_FLUXO'], _class=self._bodyTRclass))
        else:
            row.append(TD("--resolver--", _class=self._bodyTRclass))
        row.append(TD(content['DT_ENVIO'], _class=self._bodyTRclass))
        row.append(TD(content['DT_RECEBIMENTO'], _class=self._bodyTRclass))
        row.append(TD(content['ORIGEM'], _class=self._bodyTRclass))
        row.append(TD(content['DESTINO'], _class=self._bodyTRclass))
        row.append(TD(content['DESPACHO'], _class=self._bodyTRclass))
        row.append(TD(content['RECEBIDO'], _class=self._bodyTRclass))
        return row
