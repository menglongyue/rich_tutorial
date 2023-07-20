#!/usr/bin/env python
# coding=utf-8
'''
Author       : huangqj
Date         : 2023-07-20 13:12:33
LastEditors  : huangqj
LastEditTime : 2023-07-20 13:15:08
FilePath     : /rich/9_Tree.py
Description  : Header Notes
 '''
from rich.console import Console
from rich.tree import Tree

console = Console(record=True, width=100)

tree = Tree(':thumbs_up: [link=https://koaning.io]Vincent D. Warmerdam', guide_style='bold bright_black')

python_tree = tree.add("📦 Open Source Packages", guide_style="bright_black")
python_tree.add("[bold link=https://scikit-lego.netlify.app/]scikit-lego[/] - [bright_black]lego bricks for sklearn")
python_tree.add("[bold link=https://koaning.github.io/human-learn/]human-learn[/] - [bright_black]rule-based components for sklearn")

online_tree = tree.add("⭐ Online Projects", guide_style="bright_black")
online_tree.add("[bold link=https://koaning.io]koaning.io[/]   - [bright_black]personal blog")
online_tree.add("[bold link=https://calmcode.io]calmcode.io[/]  - [bright_black]dev education service")

talk_tree = tree.add("🎙️ Popular Talks", guide_style="bright_black")
talk_tree.add("[bold link=https://youtu.be/qcrR-Hd0LhI?t=542]Optimal Benchmarks and Other Failures[/]")
talk_tree.add("[bold link=https://www.youtube.com/watch?v=nJAmN6gWdK8]Playing by the Rules-Based-Systems[/]")

employer_tree = tree.add("👨‍💻 Employer", guide_style="bright_black")
employer_tree.add("[bold link=https://rasa.com]Rasa[/] - [bright_black]conversational software")

console.print(tree)
console.print("")
console.print("[green]Follow me on twitter [bold link=https://twitter.com/fishnets88]@fishnets88[/]")

CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""

console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)
