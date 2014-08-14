# -*- coding: utf-8 -*-
class QueryFilter(object):
	_filters = None

	def __init__(self, filtros ):
		self._filters = filtros

	def addFilter(self, filter):
		self._filters.update(filter)

	def teste(self):
		return self._filters

	def getFilters(self):
		stmt = []
		for var in self._filters:
			if self._filters[var]:
				if var == 'NUM_PROCESSO':
					stmt.append(""" AND D.NUM_PROCESSO LIKE '%""" + self._filters[var] + """%'""" )
				elif var == 'EMITENTE':
					stmt.append(""" AND D.EMITENTE LIKE '%""" + self._filters[var] + """%'""" )
				elif var == 'NOME_INTERESSADO':
					stmt.append(""" AND (VI.NOME_INTERESSADO LIKE '%""" + self._filters[var] + """%' OR VI2.NOME_INTERESSADO LIKE '%""" + self._filters[var] + """%' )""" )
				elif var == 'DESCR_ASSUNTO':
					stmt.append(""" AND A.DESCR_ASSUNTO LIKE '%""" + self._filters[var] + """%'""" )
				else:
					raise Exception("Erro: Filtro de pesquisa inválido.")

		return ''.join(stmt)




