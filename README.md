# pycountwc
A python 3.x package to count words, letters without space, and letters including space in a provided file.

## How to install
[pip install pycountwc](https://pypi.org/project/pycountwc/)

## How to use
This package consists of three functions:
* word() -- counts the words in the given file
* wschar() -- counts the characters (leaving space characters) in the given file
* schar() -- counts the characters (including spaces) in the given file

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
