# -*- coding: utf-8 -*-
from gluon.html import *


def printControlGroup(labelTitle, labelFor, controlContent):
    return DIV(
        LABEL(labelTitle, _for=labelFor, _class="control-label"),
        DIV(controlContent, _class="controls"),
        _class="control-group"
    )


def printSelectbox(itensDict, value, text):
    options = []

    options.append('')
    for i in itensDict:
        options.append(OPTION(i[text], _value=i[value]))
    return SELECT(options, _class="combo", _name=text)
