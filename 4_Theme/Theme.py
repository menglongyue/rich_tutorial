#!/usr/bin/env python
# coding=utf-8
'''
Author       : huangqj
Date         : 2023-07-20 12:40:27
LastEditors  : huangqj
LastEditTime : 2023-07-20 12:43:27
FilePath     : /rich/4_Theme.py
Description  : Header Notes
 '''
from rich.console import Console
from rich.theme import Theme

# You can make your own themes for rich. This is great if you're interested in rendering predefined styles.

custom_theme = Theme({
    'good' : 'green',
    'bad' : 'red',  
})

console = Console(theme=custom_theme)
console.print('File downloaded!', style='good')
console.print('File corrupted!', style='bad')
console.print('The internet is [bad]down![/]')