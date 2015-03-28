web2py_processos
================

Portal de Processos da universidade. Desenvolvido em Python utilizando o framework Web2py

Para que o mesmo funcione, adicione um novo modelo (por exemplo: `models/1.py`) que contenha as seguintes dados:

```python
# -*- coding: utf-8 -*-
from unirio.api import UNIRIOAPIRequest
from gluon import current

kAPIKey = "73cf4de9b6be2387e01e6f8d101786a9c8f04dc7c81e172288dab5ffc5b609da5bc3c86z8df0d8f939d6e409a77d65c9a"

api = UNIRIOAPIRequest(kAPIKey)
current.api = api

```
