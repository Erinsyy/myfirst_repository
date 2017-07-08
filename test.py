#!/usr/bin/env python
def factory(n):
	a=n
	for i in range(1,a):
		a=a*i
	return a
num=int(input("qing shu ru yi ge zheng zhengshu:"))
result=factory(num)
print "result is %d" %result
