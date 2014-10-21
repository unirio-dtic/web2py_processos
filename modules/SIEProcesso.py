# -*- coding: utf-8 -*-
from unirio.api import UNIRIOAPIRequest
from gluon import current

class SIEProcesso(object):
    def __init__(self):
        self.apiRequest = UNIRIOAPIRequest(current.kAPIKey)
        self.path = "V_PROCESSOS_DADOS"
        self.lmin = 0
        self.lmax = 50

    def getProcessos(self, params={}):
        processos = self.apiRequest.performGETRequest(self.path, params)
        raise Exception(processos)
        return processos.content
