'''
Created on Oct 25, 2018

@author: orcasweb
'''
i = 5
def f(arg=i):
    print(arg)


i = 6
f()

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot(type="me",action= "play",state="sleep",voltage=10)