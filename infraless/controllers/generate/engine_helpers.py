#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from infraless.core.exc import InfralessError

REQUIRED_ENGINE_MODULES = ['engines_list.py', 'engine_router.py']


def check_engine_project_modules():

    if not set(REQUIRED_ENGINE_MODULES).issubset(set(os.listdir(os.curdir))):
        raise InfralessError('Required Engine project modules are missing!')
