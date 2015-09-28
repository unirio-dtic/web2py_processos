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

    def __init__(self, contents, title_list=None):
        self.contents = contents
        self._titleList = title_list

    def print_table(self, table_class=None):
        return TABLE(self.get_table_head(), self.get_table_body(), _class=table_class)

    # print THEAD(TR(TH('<hello>')), _class='test', _id=0)
    def get_table_head(self, td_class=None, tr_class=None):
        heads = []
        for title in self._titleList:
            heads.append(TD(SPAN(title), _class=self._headTDclass))
        return THEAD(TR(heads, _class=self._headTRclass))

    def get_table_body(self):
        return TBODY(self.get_table_rows())

    def get_table_rows(self):
        rows = []
        for content in self.contents:
            rows.append(TR(self.get_row_content(content), _class=self._bodyTRclass))
        return rows

    def get_row_content(self, content):
        pass


class ProcessosTable(DefaultTable):
    def __init__(self, contents, title_list):
        DefaultTable.__init__(self, contents, title_list)

    def get_row_content(self, content):
        link = A(content['NUM_PROCESSO'], _href=URL('processo', 'index', vars={'ID_DOCUMENTO': content['ID_DOCUMENTO']}))
        row = list()
        row.append(TD(link, _class=self._bodyTRclass))
        row.append(TD(content['NOME_INTERESSADO'], _class=self._bodyTRclass) )
        row.append(TD(datetime.datetime.strptime(content['DT_ALTERACAO'], '%Y-%m-%d').strftime('%d/%m/%Y'), _class=self._bodyTRclass))
        return row


class DetalheProcessoTable(DefaultTable):
    def __init__(self, contents_dict):
        DefaultTable.__init__(self, contents_dict)

    def print_table(self, table_class=None):
        return TABLE( self.get_table_body(), _class=table_class)

    def get_table_rows(self):
        rows = []
        for contentKey, contentValue in sorted( self.contents.iteritems() ):
            rows.append(TR(self.get_row_content(contentKey, contentValue), _class=self._bodyTRclass))
        return rows

    def get_row_content(self, contentKey, contentValue):
        row = list()
        row.append(TD(contentKey, _class=self._bodyTRclass))
        row.append(TD(contentValue, _class=self._bodyTRclass))
        return row


class TramitacoesTable(DefaultTable):
    def get_row_content(self, content):
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
