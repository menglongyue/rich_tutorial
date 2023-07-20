#!/usr/bin/env python
# coding=utf-8
'''
Author       : huangqj
Date         : 2023-07-20 12:37:15
LastEditors  : huangqj
LastEditTime : 2023-07-20 12:39:30
FilePath     : /rich/3_Emphasis.py
Description  : Header Notes
 '''
from rich import print as rprint
from rich.console import Console


# The rich Console object will be the main object you'll interact with. 
# The standard print feature is nice, but the Console is much more flexible. 
# Here's some more examples showing the bold and underline features.

console = Console()
console.print("This is some text.")
console.print("This is some text.", style="bold")
console.print("This is some text.", style="bold underline")
# only underline 'is' word
console.print("[bold]This [underline]is[/] some text.[/]")
console.print("[bold red]This [underline]is[/] some text.[/]")