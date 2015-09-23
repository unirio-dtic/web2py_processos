__author__ = 'carlos.faruolo'

from gluon import current

from applications.web2py_processos.modules.unirio.api import UNIRIOAPIRequest

kAPIKey = '9287c7e89bc83bbce8f9a28e7d448fa7366ce23f163d2c385966464242e0b387e3a34d0e205cb775d769a44047995075'

# db_api = DAL('postgres://postgres:devdtic2@teste.sistemas.unirio.br/projetos_pesquisa', pool_size=10 )

api = UNIRIOAPIRequest(kAPIKey)

# *** Configure email ***
# auth = Auth(db)
# mail = auth.settings.mailer
# mail.settings.server = 'smtp.gmail.com:587'
# mail.settings.sender = 'naoresponder.projetos@unirio.br'
# mail.settings.login = 'naoresponder.projetos@unirio.br:8mx-SvY-fQh-SV9'

# Current's

# current.mail = mail
# current.auth = auth
current.kAPIKey = kAPIKey
# current.db = db
current.api = api
current.db = None
