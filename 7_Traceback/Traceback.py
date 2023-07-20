#!/usr/bin/env python
# coding=utf-8
'''
Author       : huangqj
Date         : 2023-07-20 12:50:09
LastEditors  : huangqj
LastEditTime : 2023-07-20 13:05:29
FilePath     : /rich/7_Traceback.py
Description  : Header Notes
 '''
import time
from rich.console import Console
from rich.traceback import install

# You can get a much better developer experience by using the rich traceback feature.
# It makes it much more easthetically pleasing and will also make bug-finding a less painful experience.
install()

def add_two(n1, n2):
    d = {'a': 1, 'b': 2}
    console.log('About to add two numbers', log_locals=True)
    return n1 + n2

console = Console()

for i in range(10):
    time.sleep(0.2)
    add_two(1, i)

add_two(1, 'a')


    