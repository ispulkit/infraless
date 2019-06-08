#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
src/controllers/validators.py

"""
from PyInquirer import (ValidationError, Validator)


class EmptyValidator(Validator):
    def validate(self, value):
        if len(value.text):
            return True
        else:
            raise ValidationError(message="You can't leave this blank",
                                  cursor_position=len(value.text))
