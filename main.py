from settings.settings import settings
from settings.commands import commands
from modules.functions import functions
from modules.functions.private import decorations, priv_math
from colorama import init, Fore

init(convert=True)

if __name__ == '__main__':
    for i in range(1, settings.ENTRANCE_DASH_NUMBER):
        print(end=Fore.RED + '-')
    print()
    print(Fore.RED + settings.ENTRANCE_LOGO)
    for i in range(1, settings.ENTRANCE_DASH_NUMBER):
        print(end=Fore.RED + '-')
    
    print(Fore.YELLOW + "\nEnter operation:")
    print(Fore.LIGHTYELLOW_EX + f"{settings.TAB_SPACE}1. Addition (+)\n{settings.TAB_SPACE}2. Substraction (-)\n{settings.TAB_SPACE}3. Multiplication (*)\n{settings.TAB_SPACE}4. Division (/)")
    user_operator_choice = input(Fore.CYAN +"\nOr type " + Fore.MAGENTA + "'f' " + Fore.CYAN + "for " + Fore.BLUE + "mathematical functions" + Fore.CYAN + " or " + Fore.MAGENTA + "'q'" + Fore.CYAN + " to " + Fore.RED + "quit" + Fore.CYAN + ": " + Fore.RESET)
       
    while True:
        if user_operator_choice.lower() in commands.MATH_ADD_COMMAND:
            decorations.load_text('adder')
            num1, num2 = functions.ask_num1_num2()
            decorations.calculating_text()
            priv_math.add(num1, num2)
            decorations.draw_dashed_line(settings.SEPERATOR_DASH_NUMBER)
            
        elif user_operator_choice.lower() in commands.MATH_SUBSTRACT_COMMAND:
            decorations.load_text('substracter')
            num1, num2 = functions.ask_num1_num2()
            decorations.calculating_text()
            priv_math.substract(num1, num2)
            decorations.draw_dashed_line(settings.SEPERATOR_DASH_NUMBER)
            
        elif user_operator_choice.lower() in commands.MATH_MULTIPLY_COMMAND:
            decorations.load_text('multiplier')
            num1, num2 = functions.ask_num1_num2()
            decorations.calculating_text()
            priv_math.multiply(num1, num2)
            decorations.draw_dashed_line(settings.SEPERATOR_DASH_NUMBER)
            
        elif user_operator_choice.lower() in commands.MATH_DIVIDE_COMMAND:
            decorations.load_text('divider')
            num1, num2 = functions.ask_num1_num2()
            decorations.calculating_text()
            priv_math.divide(num1, num2)
            decorations.draw_dashed_line(settings.SEPERATOR_DASH_NUMBER)
        
        elif user_operator_choice.lower() in commands.QUIT_OPTION:
            raise ValueError('Error for exiting the program')
        
        else:
            print(Fore.RED + f"OperatorInputError: Error in OperatorInput, no such operator as <{user_operator_choice}>")
            
        user_quit_choice = input(Fore.LIGHTYELLOW_EX + "\nType " + Fore.MAGENTA + "'q'" + Fore.LIGHTYELLOW_EX + " to " + Fore.RED + "quit" + Fore.LIGHTYELLOW_EX + " or " + Fore.GREEN + "'c'" + Fore.LIGHTYELLOW_EX + " to " + Fore.LIGHTGREEN_EX + "continue" + Fore.RESET + ": ")
        
        if user_quit_choice.lower() in commands.CONTINUE_OPTION:
            user_operator_choice = input(Fore.LIGHTYELLOW_EX + "\nEnter operator: ")
        
        elif user_quit_choice.lower() in commands.QUIT_OPTION:
            raise ValueError('Error for exiting the program')
        