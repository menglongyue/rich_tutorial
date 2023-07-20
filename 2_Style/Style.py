#!/usr/bin/env python
# coding=utf-8
'''
Author       : huangqj
Date         : 2023-07-20 12:32:33
LastEditors  : huangqj
LastEditTime : 2023-07-20 12:38:10
FilePath     : /rich/2_Style.py
Description  : Header Notes
 '''
from rich import print as rprint
from rich.console import Console
# The main entry to rich is the Console object. From here you can get more control of 
# the style that is applied when printing.

console = Console()
console.print('This is a print statement from console')
console.print('This is a print statement from console', style='bold')
console.print('This is a print statement from console', style='bold underline')
console.print('This is a print statement from console', style='bold red')
console.print('This is a print statement from console', style='bold red underline')
console.print('This is a print statement from console', style='bold red underline on white')
console.print('This is a print statement from console', style='bold red underline on white', justify='center')