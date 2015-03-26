# -*- coding: utf-8 -*-
from gluon import current


class SIEProcesso(object):
    def __init__(self):
        self.apiRequest = current.api
        self.path = NotImplementedError
        self.lmin = 0
        self.lmax = 1000

    def getContent(self, params={}):
        """

        :type params: dict
        """
        limits = {"LMIN": self.lmin, "LMAX": self.lmax}
        for k, v in params.items():
            params[k] = str(params[k]).upper()
        params.update(limits)

        processos = self.apiRequest.performGETRequest(self.path, params, cached=86400)
        return processos.content


class SIEProcessoDados(SIEProcesso):
    def __init__(self):
        super(SIEProcessoDados, self).__init__()
        self.path = "V_PROCESSOS_DADOS"

    def getProcessos(self, params={}):
        return self.getContent(params)

    def getProcessoDados(self, ID_DOCUMENTO):
        params = {"ID_DOCUMENTO": ID_DOCUMENTO}
        content = self.getProcessos(params)
        return content[0]


class SIEProcessoTramitacoes(SIEProcesso):
    def __init__(self):
        super(SIEProcessoTramitacoes, self).__init__()
        self.path = "V_PROCESSOS_TRAMITACOES"

    def getTramitacoes(self, NUM_PROCESSO):
        params = {"NUM_PROCESSO": NUM_PROCESSO}
        return self.getContent(params)