import goslate

a='1'

while (a!='0'):

	a=raw_input()

	gs=goslate.Goslate()

	result=gs.translate(a,'zh-tw')

	print(result)