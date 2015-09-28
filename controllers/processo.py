# -*- coding: utf-8 -*-

from tables import DetalheProcessoTable, TramitacoesTable
from sie.SIEProcesso import SIEProcessoDados, SIEProcessoTramitacoes


# noinspection PyBroadException
def index():
    processos_api = SIEProcessoDados()
    tramitacoes_api = SIEProcessoTramitacoes()

    try:
        processo = processos_api.get_processo_dados(request.vars.ID_DOCUMENTO)
        try:
            contents_dict = {
                "Número Documento": processo['ID_DOCUMENTO'],
                "Resumo Assunto": processo['RESUMO_ASSUNTO'],
                "Nome do Interessado": processo['NOME_TIPO_INTERESSADO'] + " - " + processo['NOME_INTERESSADO'],
                "Procedência": processo['PROCEDENCIA'],
                "Código Assunto": processo['COD_ESTRUTURADO'],
                "Assunto CONARQ": processo['DESCR_ASSUNTO']
            }

            table_dados = DetalheProcessoTable(contents_dict)

            tramitacoes = tramitacoes_api.get_tramitacoes(processo["NUM_PROCESSO"])
            table_tramitacoes = TramitacoesTable(
                tramitacoes,
                "Descrição Fluxo,Data Envio,Data Recebimento,Origem,Destino,Despacho,Recebido por".split(",")
            )

            return dict(
                numProcesso=processo['COD_ESTRUTURADO'],
                tableDados=table_dados.print_table("table table-bordered"),
                tableTramitacoes=table_tramitacoes.print_table("table table-bordered"),
                processoCodigo=processo['NUM_PROCESSO']
            )

        except Exception:
            session.flash = "Erro ao buscar tramitações para processo " + processo['COD_ESTRUTURADO']
            redirect(URL('default', 'index'))
    except Exception:
        session.flash = "Erro ao buscar dados para processo " + request.vars.ID_DOCUMENTO
        redirect(URL('default', 'index'))


