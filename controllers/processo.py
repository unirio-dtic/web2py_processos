# -*- coding: utf-8 -*-
from processoTable import *
from tramitacoesTable import *
import defaultTable
import forms
from SIEProcesso import SIEProcessoDados, SIEProcessoTramitacoes

def index():
    processosAPI = SIEProcessoDados()
    tramitacoesAPI = SIEProcessoTramitacoes()

    try:
        processo = processosAPI.getProcessoDados(request.vars.ID_DOCUMENTO)
        try:
            contentsDict = {
                            "Número Documento" : processo['ID_DOCUMENTO'],
                            "Resumo Assunto" : processo['RESUMO_ASSUNTO'],
                            "Nome do Interessado" : processo['NOME_TIPO_INTERESSADO'] + " - " + processo['NOME_INTERESSADO'],
                            "Procedência" : processo['PROCEDENCIA'],
                            "Código Assunto" : processo['COD_ESTRUTURADO'],
                            "Assunto CONARQ" : processo['DESCR_ASSUNTO']
                            }

            tableDados = ProcessoTable( contentsDict )

            tramitacoes = tramitacoesAPI.getTramitacoes( processo["NUM_PROCESSO"] )
            tableTramitacoes = TramitacoesTable(
                                                tramitacoes,
                                                "Descrição Fluxo,Data Envio,Data Recebimento,Origem,Destino,Despacho,Recebido por".split(",")
                                                )
        except Exception:
            response.flash = "Erro ao buscar tramitações para processo " + processo['COD_ESTRUTURADO']
    except Exception:
        response.flash = "Erro ao buscar dados para processo " + request.vars.ID_DOCUMENTO

    return dict(
                numProcesso=processo['COD_ESTRUTURADO'],
                tableDados=tableDados.printTable("table table-bordered"),
                tableTramitacoes=tableTramitacoes.printTable("table table-bordered"),
                processoCodigo=processo['NUM_PROCESSO']
                )
