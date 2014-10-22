# -*- coding: utf-8 -*-
from ProcessosTable import *
from SIEProcesso import *
from tramitacoesTable import *
import forms

def index():
    tableDados = None
    numProcesso = None
    tableProcessos = None
    processosAPI = SIEProcessoDados()

    form = FORM(
        forms.printControlGroup("Descrição", "DESCR_ASSUNTO", INPUT(_name="DESCR_ASSUNTO")),
        forms.printControlGroup("Resumo do Assunto", "RESUMO_ASSUNTO", INPUT(_name="RESUMO_ASSUNTO")),
        forms.printControlGroup("Nome do Interessado", "NOME_INTERESSADO", INPUT(_name="NOME_INTERESSADO")),
        forms.printControlGroup("Emitente", "EMITENTE", INPUT(_name="EMITENTE")),
        forms.printControlGroup("Número", "NUM_PROCESSO", INPUT(_name="NUM_PROCESSO")),
        INPUT(_type="submit")
    )

    if form.process().accepted:
        try:
            filtros = form.vars
            processos = processosAPI.getProcessos( filtros )

            tableProcessos = ProcessosTable(processos, "Número,Nome,Data".split(",")).printTable("table table-bordered")
        except ValueError as e:
            response.flash = "Nenhum resultado encontrado"
        except Exception as e:
            raise e


    return dict(
        form=form,
        tableProcessos=tableProcessos
    )


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())
