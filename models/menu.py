# -*- coding: utf-8 -*-
response.logo = A("DTIC/UNIRIO",
                  _class="brand",_href="http://www.unirio.br/dtic")
response.title = request.application.replace('_',' ').title()
response.subtitle = ''

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Your Name <you@example.com>'
response.meta.description = 'a cool new app'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Web Framework'

## your http://google.com/analytics id
response.google_analytics_id = None

response.menu = [
    (T('Home'), False, URL('default', 'index'), [])
]