'''
Created on Oct 24, 2018

@author: orcasweb
'''
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a + b
