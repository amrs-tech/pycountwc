import os
def word(file):
	for dirpath, dirnames, filenames in os.walk("."):
		for filename in [f for f in filenames if f.endswith(file)]:
			file = os.path.join(dirpath, filename)
			break
	f = open(file, encoding="latin-1", errors="surrogateescape")
	res = []
	for i in f:
		res.append(i.replace('\n',''))
	x = ''
	for i in res:
		x += i + ' '

	a = [i for i in x.split(' ')]
	a.pop()
	wc = len(a)
	return wc

def schar(file):
	for dirpath, dirnames, filenames in os.walk("."):
		for filename in [f for f in filenames if f.endswith(file)]:
			file = os.path.join(dirpath, filename)
			break
	f = open(file, encoding="latin-1", errors="surrogateescape")
	res = []
	for i in f:
		res.append(i.replace('\n',''))
	x = ''
	for i in res:
		x += i + ' '
	lsc = len(x)-1
	lc = len(x.replace(' ',''))
	return lsc
	
def wschar(file):
	for dirpath, dirnames, filenames in os.walk("."):
		for filename in [f for f in filenames if f.endswith(file)]:
			file = os.path.join(dirpath, filename)
			break
	f = open(file, encoding="latin-1", errors="surrogateescape")
	res = []
	for i in f:
		res.append(i.replace('\n',''))
	x = ''
	for i in res:
		x += i + ' '
	lsc = len(x)-1
	lc = len(x.replace(' ',''))
	return lc
	