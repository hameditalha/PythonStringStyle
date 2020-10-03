from colorama import Fore, Style, Back

print(f'{Fore.BLACK}I am Black{Fore.RESET}')
print(f'{Fore.RED}I am Red{Fore.RESET}')
print(f'{Fore.GREEN}I am Green{Fore.RESET}')
print(f'{Fore.YELLOW}I am Yellow{Fore.RESET}')
print(f'{Fore.BLUE}I am Blue{Fore.RESET}')
print(f'{Fore.MAGENTA}I am Magenta{Fore.RESET}')
print(f'{Fore.CYAN}I am Cyan{Fore.RESET}')
print(f'{Fore.WHITE}I am White{Fore.RESET}')

print(f'{Back.BLACK}  Hello World!  {Back.RESET}')
print(f'{Back.RED}  Hello World!  {Back.RESET}')
print(f'{Back.GREEN}  Hello World!  {Back.RESET}')
print(f'{Back.YELLOW}  Hello World!  {Back.RESET}')
print(f'{Back.BLUE}  Hello World!  {Back.RESET}')
print(f'{Back.MAGENTA}  Hello World!  {Back.RESET}')
print(f'{Back.CYAN}  Hello World!  {Back.RESET}')
print(f'{Back.WHITE}  Hello World!  {Back.RESET}')

print(f'{Style.BRIGHT}I am bold{Style.RESET_ALL}')
print(f'{Style.DIM}I am light{Style.RESET_ALL}')

print('\033[32;40;1mSome bright green text on black background\033[39;49;22m')
print('\033[31;47;2mSome dim red text on white background\033[39;49;22m')
print('\033[30;43mBye...Bye!\033[39;49m')