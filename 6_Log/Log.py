#!/usr/bin/env python
# coding=utf-8
'''
Author       : huangqj
Date         : 2023-07-20 12:46:45
LastEditors  : huangqj
LastEditTime : 2023-07-20 12:48:25
FilePath     : /rich/6_log.py
Description  : Header Notes
 '''
from rich.console import Console
import time

# Rich comes with an amazing suite of tools to make logging more visually pleasing.
console = Console()

for i in range(10):
    console.log(f'I am about to sleep {i}')
    time.sleep(0.2)
    console.log(f'But i am briefly awake now!')
