web2py_processos
================

Portal de Processos da universidade. Desenvolvido em Python utilizando o framework Web2py

Para que o mesmo funcione, adicione um novo modelo (por exemplo: `models/1.py`) que contenha as seguintes dados:

```python
# -*- coding: utf-8 -*-
from gluon import current


db = DAL('postgres://theusername:supersecret@localhost/processos')
kAPIKey = "62e1c0e9jh4fcuhruivhzui4vhtiuxgek4ht7if478t3d7yj39xkkqy309tsky78939d6e409a77d65c9a" 

current.kAPIKey = kAPIKey
```
