#!/usr/bin/env python
# coding=utf-8
'''
Author       : huangqj
Date         : 2023-07-20 13:26:51
LastEditors  : huangqj
LastEditTime : 2023-07-20 13:52:10
FilePath     : /rich_tutorial/11_Constructions/Constructions.py
Description  : Header Notes
 '''
from rich.columns import Columns
from rich.panel import Panel
from rich.markdown import Markdown
from rich.console import Console

# Columns, Panels and Markdown
# Rich is a flexible system of components that can really click together too. 
# To demonstrate this we'll combine the Columns, Panel and Markdown classes together in the example below.

md1 = """
# Hello World

## This is Markdown

And it renders *very* **nicely**!
"""

md2 = """
## This is Markdown, Again

With code!

```python
print("hello world")
```
"""

console = Console(record=True, width=100) # width= 100
panel_1 = Panel(Markdown(md1), title='pannel one', width=60)
panel_2 = Panel(Markdown(md2), title='pannel two', width=60)
console.print(Columns([panel_1, panel_2]))
