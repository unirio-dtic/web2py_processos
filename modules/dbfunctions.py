# -*- coding: utf-8 -*-
from gluon import current

def getDadosProcesso(NUM_PROCESSO):
	processo = current.dbSie.executesql("""SELECT DISTINCT D.ID_DOCUMENTO,
															D.NUM_PROCESSO,
															DBSM.RETIRAACENTOS( D.RESUMO_ASSUNTO ) AS RESUMO_ASSUNTO,
															D.EMITENTE,
															D.DT_ALTERACAO,
															D.HR_ALTERACAO,
															A.DESCR_ASSUNTO,
															A.COD_ESTRUTURADO,
															VI.NOME_INTERESSADO,
															VI2.NOME_INTERESSADO AS PROCEDENCIA,
															CASE
																WHEN D.TIPO_INTERESSADO = 'A' THEN 'Alunos'
																WHEN D.TIPO_INTERESSADO = 'K' THEN 'Curso'
																WHEN D.TIPO_INTERESSADO = 'O' THEN 'Outros'
																WHEN D.TIPO_INTERESSADO = 'Q' THEN 'Requerente'
																WHEN D.TIPO_INTERESSADO = 'S' THEN 'Servidor'
																WHEN D.TIPO_INTERESSADO = 'U' THEN 'Universidades'
																WHEN D.TIPO_INTERESSADO = 'F' THEN 'Tipo não reconhecido'
															END AS NOME_TIPO_INTERESSADO															
															FROM DBSM.DOCUMENTOS D LEFT JOIN DBSM.TRAMITACOES T ON D.ID_DOCUMENTO = T.ID_DOCUMENTO
															LEFT JOIN DBSM.TIPOS_DOCUMENTOS TD ON D.ID_TIPO_DOC = TD.ID_TIPO_DOC
															LEFT JOIN DBSM.TIPOS_DOCUMENTOS TD1 ON TD.ID_TIPO_DOC_SUP = TD1.ID_TIPO_DOC
															LEFT JOIN DBSM.ASSUNTOS A ON A.ID_ASSUNTO = D.ID_ASSUNTO
															LEFT JOIN DBSM.V_INTERESSADOS_DOC VI ON D.ID_INTERESSADO = VI.ID_INTERESSADO
															LEFT JOIN DBSM.V_INTERESSADOS_DOC VI2 ON D.ID_PROCEDENCIA = VI2.ID_INTERESSADO AND VI2.TIPO_INTERESSADO = D.TIPO_PROCEDENCIA
															WHERE TD1.ID_TIPO_DOC = 1
															AND D.ID_DOCUMENTO = """ + NUM_PROCESSO + """""", as_dict=True)
	if processo:
		return processo[0]
	else:
		raise Exception("Processo não encontrado")
	
def getTramitacoes(ID_DOCUMENTO):
	return current.dbSie.executesql("""SELECT D.NUM_PROCESSO,
											   REPLACE( CONCAT(CONCAT(CAST(T.DT_DESPACHO AS VARCHAR(20)),' '),CAST(T.HR_DESPACHO AS VARCHAR(20))), '.',':') AS DT_ENVIO,
											   REPLACE( CONCAT(CONCAT(CAST(T.DT_RECEBIMENTO AS VARCHAR(20)),' '),CAST(T.HR_RECEBIMENTO AS VARCHAR(20))), '.',':') AS DT_RECEBIMENTO,
											   T.ID_ORIGEM,
											   T.TIPO_ORIGEM,
											   T.ID_DESTINO,
											   T.TIPO_DESTINO,
											   DBSM.RETIRAACENTOSCLOB( T.DESPACHO ) AS DESPACHO,
											   DBSM.RETIRAACENTOS( F.DESCR_FLUXO ) AS DESCR_FLUXO,
											   T.SITUACAO_TRAMIT,
											   CASE
											   		WHEN T.SITUACAO_TRAMIT = 'R' OR T.SITUACAO_TRAMIT = 'T' THEN (SELECT U.NOME_USUARIO FROM USUARIOS U WHERE U.ID_USUARIO = T.COD_OPERADOR)
											   		WHEN T.SITUACAO_TRAMIT = 'E' THEN ' ' -- Deve ficar em branco
											   		ELSE 'Desconhecido pelo sistema'
											   END AS RECEBIDO,
											   CASE 
												   WHEN T.TIPO_ORIGEM = 9 OR T.TIPO_ORIGEM = 29 THEN (SELECT NOME_UNIDADE FROM DBSM.ORG_INSTITUICAO WHERE ID_UNIDADE = T.ID_ORIGEM)
												   WHEN T.TIPO_ORIGEM = 20 THEN (SELECT NOME_USUARIO FROM DBSM.USUARIOS WHERE ID_USUARIO = T.ID_ORIGEM)
												   ELSE 'Origem não reconhecida pelo sistema'
											   END AS ORIGEM,
											   CASE 
												   WHEN T.TIPO_DESTINO = 9 OR T.TIPO_DESTINO = 29 THEN (SELECT NOME_UNIDADE FROM DBSM.ORG_INSTITUICAO WHERE ID_UNIDADE = T.ID_DESTINO)
												   WHEN T.TIPO_DESTINO = 20 THEN (SELECT NOME_USUARIO FROM DBSM.USUARIOS WHERE ID_USUARIO = T.ID_DESTINO)			
												   ELSE 'Destino não reconhecido pelo sistema'
											   END AS DESTINO 
									   FROM DBSM.DOCUMENTOS D  LEFT JOIN DBSM.TRAMITACOES T ON D.ID_DOCUMENTO = T.ID_DOCUMENTO
															   LEFT JOIN DBSM.TIPOS_DOCUMENTOS TD ON D.ID_TIPO_DOC = TD.ID_TIPO_DOC
															   LEFT JOIN DBSM.TIPOS_DOCUMENTOS TD1 ON TD.ID_TIPO_DOC_SUP = TD1.ID_TIPO_DOC AND TD1.ID_TIPO_DOC = 1
															   LEFT JOIN DBSM.FLUXOS F ON F.ID_FLUXO = T.ID_FLUXO
															   LEFT JOIN DBSM.RESTRICOES R ON T.TIPO_ORIGEM = R.ID_RESTRICAO
									   WHERE D.ID_DOCUMENTO = """ + str(ID_DOCUMENTO) + """
									   ORDER BY T.SEQUENCIA""", as_dict=True)