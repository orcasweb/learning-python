'''
Created on Oct 24, 2017
Numbers 1234, 3.1415, 3+4j, 0b111, Decimal(), Fraction()
Strings 'spam', "Bob's", b'a\x01c', u'sp\xc4m'
Lists [1, [2, 'three'], 4.5], list(range(10))
Dictionaries {'food': 'spam', 'taste': 'yum'}, dict(hours=10)
Tuples (1, 'spam', 4, 'U'), tuple('spam'), namedtuple
Files open('eggs.txt'), open(r'C:\ham.bin', 'wb')
Sets set('abc'), {'a', 'b', 'c'}
Other core types Booleans, types, None
Program unit types Functions, modules, classes (Part IV, Part V, Part VI)
Implementation-related types Compiled code, stack tracebacks (Part IV, Part VII)
@author: orcasweb
'''
num1 = 10
print("This is decimal num1 %d", num1)
print("This is float num1 %f", num1)
mylist = [1111,
          2222,
          3333]
while True:
    reply = input("enter text here. type 'stop' to exit the loop: ")
    if reply == "stop" :break
    print(reply.upper())

print("Now lets learn about Lists...")
mylist1 = list(range(10))
print(mylist1)