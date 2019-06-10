#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
infraless/controllers/generate.py

"""
import os

from cement import Controller, ex
from PyInquirer import Token, prompt, style_from_dict

from ..controllers.validators import EmptyValidator
from ..core import config
from ..core import helpers as hlprs
from ..core.exc import InfralessError

style = style_from_dict({
    Token.QuestionMark: '#E91E63 bold',
    Token.Selected: '#673AB7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#2196f3 bold',
    Token.Question: '',
})


class Generate(Controller):
    """
    Generate controller.
    This controller can generate engines.

    Raises
    ------
    InfralessError
    """

    class Meta:
        label = 'g'
        description = "Generate modules"
        stacked_on = 'base'
        stacked_type = 'nested'

    enginetype = 'serverless'
    enginename = None

    @ex(
        help='Generate modules and automated code',
        arguments=[(['-et', '--enginetype'], {
            'help': 'Engine Type' + 'For ex: serverless, docker',
            'action': 'store',
            'dest': 'enginetype'
        }),
                   (['-en', '--enginename'], {
                       'help': 'Engine Name',
                       'action': 'store',
                       'dest': 'enginename'
                   })],
    )
    def engine(self):
        """
        Generates an engine.

        Raises
        ------
        InfralessError
            - When engine name is not specified.
        """
        engine_type = str(self.app.pargs.enginetype).strip().lower()
        engine_name = str(self.app.pargs.enginename).strip().lower()

        if not engine_type or engine_type == 'none':
            hlprs.log(
                'Falling back on \'serverless\' as default engine type. Use -et to specify engine type.',
                'yellow')
        if not engine_name or engine_name == 'none':
            raise InfralessError('Engine name not specified.')
        engine_type = self.enginetype
        config.validate_ilconfig()
        hlprs.log("Engine: {} added".format(engine_name), "green")
