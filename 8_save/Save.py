#!/usr/bin/env python
# coding=utf-8
'''
Author       : huangqj
Date         : 2023-07-20 13:05:50
LastEditors  : huangqj
LastEditTime : 2023-07-20 13:12:12
FilePath     : /rich/8_Save.py
Description  : Header Notes
 '''
import time
from rich.console import Console
from rich.traceback import install

install()

def add_two(n1, n2):
    console.log('About to add two numbers', log_locals=True)
    return n1 + n2

try:
    console = Console(record=True)  # everything recorded will be saved in console.save_html()
    for i in range(10):
        time.sleep(0.2)
        add_two(1, i)
except:
    # if not except, statment below: console.save_* will not be processed!!!
    console.print_exception()
      
console.save_html('traceback.html')
# console.save_text('traceback.txt')
# console.save_svg('traceback.svg')
        
        