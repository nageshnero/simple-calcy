from random import choice
from xml.dom.expatbuilder import ElementInfo


def add(a, b, c):
    return a+b+c
def sub(a, b, c):
    return a-b-c
def mul(a, b, c):
    return a*b*c
def div(a, b, c):
    return a//b//c
print("""choose the operation
1.additon
2.subtraction
3.multiplication
4.division""")
choice=int(input("enter your choice"))
a=int(input("enter your number1"))
b=int(input("enter your number2"))
c=int(input("enter your number3"))
if choice == 1:
    print(add(a, b, c))
elif choice == 2:
    print(sub(a, b, c))
elif choice == 3:
    print(mul(a, b, c))
elif choice == 4:
    print(div(a, b, c))
else:
    print("select the right choice")