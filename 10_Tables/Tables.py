#!/usr/bin/env python
# coding=utf-8
'''
Author       : huangqj
Date         : 2023-07-20 13:22:29
LastEditors  : huangqj
LastEditTime : 2023-07-20 13:26:22
FilePath     : /rich/10_Tables.py
Description  : Header Notes
 '''
from rich.console import Console
from rich.table import Table

# Tables are another nice feature that are nice to have in the terminal!

table = Table(title='Pandas Versions')
table.add_column('Released', style='cyan')
table.add_column('Version number', justify='center', style='magenta')
table.add_column('Description', style='green')

table.add_row('May 16, 2023', 'v1.0.0', 'First release')
table.add_row('Dec 18, 2023', 'v2.0.0', 'Breaking change release')
table.add_row('Aug 18, 2024', 'v2.1.0', 'Feature release')
table.add_row('Jun 14, 2025', 'v3.0.0', ':thumbs_up: [underline red]Breaking change[/] release')

console = Console()
console.print(table)