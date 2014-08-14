# -*- coding: utf-8 -*-
from processoTable import *
from tramitacoesTable import *
import defaultTable
import dbfunctions
import forms
from queryfilter import *

def index():
    tableDados = None
    numProcesso = None
    tableTramitacoes = None
    processoCodigo = None

    try:
        contents = dbfunctions.getDadosProcesso( request.vars.ID_DOCUMENTO )

        processoCodigo = contents['NUM_PROCESSO']

        contentsDict = {
                        "Número Documento" : contents['ID_DOCUMENTO'],
                        "Resumo Assunto" : contents['RESUMO_ASSUNTO'],
                        "Nome do Interessado" : contents['NOME_TIPO_INTERESSADO'] + " - " + contents['NOME_INTERESSADO'],
                        "Procedência" : contents['PROCEDENCIA'],
                        "Código Assunto" : contents['COD_ESTRUTURADO'],
                        "Assunto CONARQ" : contents['DESCR_ASSUNTO']
                        }

        tableDados = ProcessoTable( contentsDict )
        tableDados = tableDados.printTable("table table-bordered")

        tramitacoes = dbfunctions.getTramitacoes( contents['ID_DOCUMENTO'] )
        tableTramitacoes = TramitacoesTable(
                                            tramitacoes,
                                            "Descrição Fluxo,Data Envio,Data Recebimento,Origem,Destino,Despacho,Recebido por".split(",")
                                            )
        tableTramitacoes = tableTramitacoes.printTable("table table-bordered")
    except Exception, e:
        response.flash = e

    return dict(
                numProcesso=numProcesso,
                tableDados=tableDados,
                tableTramitacoes=tableTramitacoes,
                processoCodigo=processoCodigo
                )
