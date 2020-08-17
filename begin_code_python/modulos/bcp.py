import random
import time
import sys
#import modulos.cripto as cr

def hola(name):
    print("Hello {name}!!".format(name=name))


def rolled_dice():
    print("You have rolled {}".format(random.randint(1,6)))

  
def divisor_pattern(number):
    for i in range(1, number+1):
        for j in range(1, number+1):
            if ((i % j == 0) or (j % i == 0)):
                print("* ",end="")
            else:
                print("  ",end="")
        print((i+1))

    
def regurgitator():
    age = int(input("Please enter your age: "))
    while age < 1 or age > 95:
        # Repeat this code while the age is invalid
        print("This age is not valid")
        age = int(input("Please enter your age: "))
    print("Thank you for entering your age!")
    
def catching_exception():
    while True:
        try:
            ride_number = int(input("Please enter the ride number you want: "))
            print(f"You have entered: {ride_number}")
            break
        except ValueError as ve:
            print("Invalid number")
            print(ve.__str__()) 
        

def arguments():
    print(f"Arguments count: {len(sys.argv)}")
    for i, arg in enumerate(sys.argv):
        print(f"Argument: {i:>6}: {arg}")