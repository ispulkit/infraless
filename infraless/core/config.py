#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import yaml

from infraless.core.exc import InfralessError

INFRALESS_CONST_CONFIG_FILENAME = '.ilconfig'


def ilassert_ilconfig_exists():
    """
    Checks if .ilconfig exists

    Raises
    ------
    InfralessError
        Raised if .ilconfig doesn't exist in the current dir.
    """
    if INFRALESS_CONST_CONFIG_FILENAME not in os.listdir(os.curdir):
        raise InfralessError('No config file found')


def validate_ilconfig():
    """
    Validates the format of ilconfig and checks for required keys.

    Raises
    ------
    InfralessError
        Raised if the config file is invalid.
    """
    ilassert_ilconfig_exists()
    with open(INFRALESS_CONST_CONFIG_FILENAME, 'r') as stream:
        try:
            ilconfig = yaml.safe_load(stream)
        except yaml.YAMLError:
            raise InfralessError('Invalid .ilconfig found.')
