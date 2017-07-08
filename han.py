#!/usr/bin/env python
def han(n,x,y,z):
	if n ==1:
		print(x,'-->',y)
	else:
		han(n-1,x,z,y)
		print(x,'-->',y) 
		han(n-1,y,x,z)
n=int(input('shuru ceng shu:'))
han(n,'x','y','z')
print "hello world"
