#!/usr/bin/env python
# coding=utf-8
'''
Author       : huangqj
Date         : 2023-07-20 14:02:53
LastEditors  : huangqj
LastEditTime : 2023-07-20 14:03:07
FilePath     : /rich_tutorial/12_Progress/Progress.py
Description  : Header Notes
 '''
from rich.progress import track
import time

for i in track(range(20)):
    time.sleep(0.5)
