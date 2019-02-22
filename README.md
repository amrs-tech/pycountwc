# pycountwc

[![GitHub](https://img.shields.io/badge/license-MIT-brightgreen.svg)](https://raw.githubusercontent.com/amrs-tech/pycountwc/master/LICENSE)
[![PyPI Downloads](https://img.shields.io/pypi/dm/pycountwc.svg)](https://pypi.org/project/pycountwc/)
[![PyPI](https://img.shields.io/pypi/v/pycountwc.svg)](https://pypi.org/project/pycountwc/)

A python 3.x package to count words, letters without space, and letters including space in a provided file.
This package works well for macOS.

## How to install
```python
pip install pycountwc
```
## How to use
This package consists of three functions:
* `word()` -- counts the words in the given file
* `wschar()` -- counts the characters (leaving space characters) in the given file
* `schar()` -- counts the characters (including spaces) in the given file

Pass in your required file (to count words/chars) to any of the above function.

Contributions are most welcome.

## Example
```python
import pycountwc.pycountwc as pp

pp.word(" ") #give your filename
'''This returns an integer denoting number of words'''

pp.wschar(" ") #filename inside quotes
'''This returns an integer denoting number of characters without space count'''
```
