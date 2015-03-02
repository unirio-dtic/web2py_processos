# -*- coding: utf-8 -*-
import datetime
from gluon.html import *
from DefaultTable import *


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
