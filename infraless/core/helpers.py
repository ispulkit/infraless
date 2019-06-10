#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyfiglet import figlet_format

try:
    import colorama
    colorama.init()
except ImportError:
    colorama = None

try:
    from termcolor import colored
except ImportError:
    colored = None


def log(string, color, font="slant", figlet=False, on_color=None):
    """
    Generates colored log on the console.

    Parameters
    ----------
    string : String
        String to log
    color : String
        Color to log
    font : str, optional
        Font, by default "slant"
    figlet : bool, optional
        use figlet, by default False
    on_color : String, optional
        Background color, by default None
    """
    if colored:
        if not figlet:
            if on_color:
                print(colored(string, color, on_color))
            else:
                print(colored(string, color))
        else:
            if on_color:
                print(
                    colored(figlet_format(string, font=font), color, on_color))
            else:
                print(colored(figlet_format(string, font=font), color))
    else:
        print(string)
