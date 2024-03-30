from settings.settings import settings
from colorama import init, Fore

init(convert=True)

def draw_dashed_line(dash_number):
    for i in range(dash_number+1):
        print(end=Fore.LIGHTGREEN_EX + '-')

def load_text(user_choice):
    if settings.ENABLE_LOADING == True:
        print(Fore.YELLOW + "\nLoading: " + Fore.LIGHTCYAN_EX + "math." + Fore.LIGHTBLUE_EX + f"{user_choice}" + Fore.LIGHTRED_EX + "()" + Fore.RESET + "...")
        print(Fore.LIGHTGREEN_EX + f"Success: " + Fore.LIGHTYELLOW_EX + "In loading --> " + Fore.LIGHTCYAN_EX + "math." + Fore.LIGHTBLUE_EX + f"{user_choice}" + Fore.LIGHTRED_EX + "()\n")
    
    else:
        pass