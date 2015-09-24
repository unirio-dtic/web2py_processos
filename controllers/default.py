# -*- coding: utf-8 -*-
from sie.SIEProcesso import SIEProcessoDados
from ProcessosTable import *
from tramitacoesTable import *
import forms


def index():
    tableProcessos = None
    processosAPI = SIEProcessoDados()

    form = FORM(
        forms.printControlGroup("Descrição", "DESCR_ASSUNTO", INPUT(_name="DESCR_ASSUNTO")),
        forms.printControlGroup("Resumo do Assunto", "RESUMO_ASSUNTO", INPUT(_name="RESUMO_ASSUNTO")),
        forms.printControlGroup("Nome do Interessado", "NOME_INTERESSADO", INPUT(_name="NOME_INTERESSADO")),
        forms.printControlGroup("Emitente", "EMITENTE", INPUT(_name="EMITENTE")),
        forms.printControlGroup("Número ( Favor digitar o número completo. Ex: 99999.999999/9999-99)", "NUM_PROCESSO", INPUT(_name="NUM_PROCESSO")),
        INPUT(_type="submit")
    )

    if form.process().accepted:
        redirect(URL('default', 'index', vars=form.vars))
    elif request.vars:
        try:
            filtros = request.vars
            filtros.update({'ORDERBY': 'DT_ALTERACAO'})
            processos = processosAPI.getProcessos(filtros)

            tableProcessos = ProcessosTable(processos, ('Número', 'Nome', 'Data')).printTable("table table-bordered")
            response.flash = "%d processos encontrados." % len(processos)
        except ValueError:
            response.flash = "Nenhum resultado encontrado"

    return dict(
        form=form,
        tableProcessos=tableProcessos
    )