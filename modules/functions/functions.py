from colorama import init, Fore

from settings.settings import settings
from modules.functions.private import decorations

init(convert=True)

def ask_num1_num2():
    decorations.draw_dashed_line(settings.SEPERATOR_DASH_NUMBER)
    
    num1 = input(Fore.LIGHTYELLOW_EX + "\nEnter num1: " + Fore.BLUE)
    num2 = input(Fore.LIGHTYELLOW_EX + "Enter num2: " + Fore.BLUE)
    
    return num1, num2
