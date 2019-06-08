#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
stocksense/controllers/stock.py

"""
import os

from cement import Controller, ex
from PyInquirer import Token, prompt, style_from_dict

from ..controllers.validators import EmptyValidator
from ..core import helpers as hlprs
from ..core.config import INFRALESS_CONST_CONFIG_FILENAME
from ..core.exc import InfralessError

style = style_from_dict({
    Token.QuestionMark: '#E91E63 bold',
    Token.Selected: '#673AB7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#2196f3 bold',
    Token.Question: '',
})


class Generate(Controller):
    class Meta:
        label = 'g'
        description = "Generate modules"
        stacked_on = 'base'
        stacked_type = 'nested'

    @ex(
        help='Generate modules and automated code',
        arguments=[
            (['-p', '--provider'], {
                'help': 'the provider to use for data collection.' +
                'For ex: valueresearchonline.com',
                'action': 'store',
                'dest': 'provider'
            }),
        ],
    )
    def engine(self):
        if INFRALESS_CONST_CONFIG_FILENAME not in os.listdir(os.curdir):
            raise InfralessError('No config file found')
        hlprs.log("Engine added", "green")
