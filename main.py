from settings.settings import settings
from settings.commands import commands
from modules.functions import functions
from modules.functions.private import decorations, priv_math
from colorama import init, Fore

init(convert=True)

if __name__ == '__main__':
    decorations.draw_dashed_line(settings.ENTRANCE_DASH_NUMBER)
    print(Fore.RED + settings.ENTRANCE_LOGO)
    decorations.draw_dashed_line(settings.ENTRANCE_DASH_NUMBER)
    
    print(Fore.YELLOW + "\nEnter operation:")
    user_operator_choice = input(Fore.LIGHTYELLOW_EX + f"{settings.TAB_SPACE}1. Addition (+)\n{settings.TAB_SPACE}2. Substraction (-)\n{settings.TAB_SPACE}3. Multiplication (*)\n{settings.TAB_SPACE}4. Division (/) \n" + Fore.CYAN +"\nOr type " + Fore.MAGENTA + "'f' " + Fore.CYAN + "for mathematical functions: " + Fore.RESET)
    
    if user_operator_choice.lower() in commands.MATH_ADD_COMMAND:
        decorations.load_text('adder')
        num1, num2 = functions.ask_num1_num2()
        priv_math.add(num1, num2)
        decorations.draw_dashed_line(settings.SEPERATOR_DASH_NUMBER)
        
    elif user_operator_choice.lower() in commands.MATH_SUBSTRACT_COMMAND:
        decorations.load_text('substracter')
        num1, num2 = functions.ask_num1_num2()
        priv_math.substract(num1, num2)
        
    elif user_operator_choice.lower() in commands.MATH_MULTIPLY_COMMAND:
        decorations.load_text('multiplier')
        num1, num2 = functions.ask_num1_num2()
        priv_math.multiply(num1, num2)
        
    elif user_operator_choice.lower() in commands.MATH_DIVIDE_COMMAND:
        decorations.load_text('divider')
        num1, num2 = functions.ask_num1_num2()
        priv_math.divide(num1, num2)
        
    user_quit_choice = input(Fore.LIGHTYELLOW_EX + "\nType " + Fore.MAGENTA + "'q'" + Fore.LIGHTYELLOW_EX + " to " + Fore.RED + "quit" + Fore.RESET + ": ")
    