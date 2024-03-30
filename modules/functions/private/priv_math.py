from colorama import init, Fore
import math

init(convert=True)

def add(num1, num2):
    if num1.isdigit() and num2.isdigit():
        print(Fore.GREEN + "RESULT: " + Fore.LIGHTBLUE_EX + f"{num1} + {num2} = {int(num1)+int(num2)}" + Fore.RESET)

    else:
        print(Fore.RED + "CommandError: Input cannot contain strings")
        
def substract(num1, num2):
    if num1.isdigit() and num2.isdigit():
        print(Fore.GREEN + "RESULT: " + Fore.LIGHTBLUE_EX + f"{num1} - {num2} = {int(num1)-int(num2)}" + Fore.RESET)

    else:
        print(Fore.RED + "CommandError: Input cannot contain strings")
        
def multiply(num1, num2):
    if num1.isdigit() and num2.isdigit():
        print(Fore.GREEN + "RESULT: " + Fore.LIGHTBLUE_EX + f"{num1} x {num2} = {int(num1)*int(num2)}" + Fore.RESET)

    else:
        print(Fore.RED + "CommandError: Input cannot contain strings")
    
def divide(num1, num2):
    if num1.isdigit() and num2.isdigit():
        print(Fore.GREEN + "RESULT: " + Fore.LIGHTBLUE_EX + f"{num1} ÷ {num2} = {int(num1)/int(num2)}" + Fore.RESET)

    else:
        print(Fore.RED + "CommandError: Input cannot contain strings")