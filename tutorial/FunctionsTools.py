'''
Created on Oct 24, 2018

@author: orcasweb
'''
from builtins import int
def fib(n):
    a, b = 0, 1
    if(n >=2):
        while b < n:
            print(b, end=',')
            a, b = b, a + b
    else:
        print("For fibonacci series the input number should be greater than or equal to 2. Now exiting ")       

#fib(5)
fibn = 2
while fibn >= 2:
    myinput = input("Enter a number greater than 1 to get the fibonacci series: ")
    fibn = int(myinput)
    fib(fibn)
    print()
print("this is the end of the program")
print("Thanks for coding")

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

ask_ok("Do you really want to quit?")
