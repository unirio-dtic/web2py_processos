# -*- coding: utf-8 -*-
def index():
    from unirio.api import *
    APIKey = "62e1c0e9b6be2387e01e6f8d101786a9c8f04dc7c81e178822daa5ffc5b609da5bd3c828df0d8f939d6e409a77d65c9a"

    uAPi = UNIRIOAPIRequest( APIKey, 1 )
    path = "ALUNOS"
    params = {"LMIN" : 0,
              "LMAX" : 1000,
              "SEXO" : "F",
              "ETNIA_ITEM" : 1
    }
    fields = ["ID_ALUNO", "ID_PESSOA", "SEXO", "ETNIA_ITEM"]

    ret = uAPi.performGETRequest( path, params )

    return dict(ret = ret.content)