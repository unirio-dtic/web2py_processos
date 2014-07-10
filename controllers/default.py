# -*- coding: utf-8 -*-
from processoTable import *
from tramitacoesTable import *
import defaultTable
import dbfunctions
import forms

def index():
    tableDados = None
    numProcesso = None
    tableTramitacoes = None
    processoCodigo = None

    form = FORM(
                forms.printControlGroup( "Título", "titulo", INPUT(_name="titulo") ),
                INPUT(_name="busca"),
                INPUT(_type="submit")
                )

    if form.process().accepted:
        try:
            contents = dbfunctions.getDadosProcesso( form.vars.busca )

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
            response.flash = e[0]

    return dict(
                form=form,
                numProcesso=numProcesso,
                tableDados=tableDados,
                tableTramitacoes=tableTramitacoes,
                processoCodigo=processoCodigo
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
