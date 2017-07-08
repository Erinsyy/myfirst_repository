#s!/usr/bin/env python
def factorial(n):
	if n == 1:
	 	return 1
	else:
		return n*factorial(n-1)

number = int(input('qing shu ru zheng shu'))
result = factorial(number)
print('%d de ji cheng shi %d'%(number,result))
