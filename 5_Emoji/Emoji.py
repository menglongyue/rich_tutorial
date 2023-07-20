#!/usr/bin/env python
# coding=utf-8
'''
Author       : huangqj
Date         : 2023-07-20 12:43:53
LastEditors  : huangqj
LastEditTime : 2023-07-20 12:46:14
FilePath     : /rich/5_Emoji.py
Description  : Header Notes
 '''
from rich.console import Console

# You can use rich to show emoji! They render natively when you render a string in a Console object.
console = Console()
console.print('This is a smiley face! :smiley:')
console.print(':thumbs_up: This is a thumbs up! ')