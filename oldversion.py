from hijri_converter import Hijri
from colorama import init, Fore, Style

# Initialize color support
init(autoreset=True)

def convert_hijri_to_gregorian(hijri_str):
    try:
        day, month, year = map(int, hijri_str.strip().split('/'))
        greg_date = Hijri(year, month, day).to_gregorian()
        return greg_date.strftime('%d %B %Y')  # Windows-compatible format
    except ValueError:
        return None

print(Fore.CYAN + Style.BRIGHT + "\nHijri to Gregorian Converter")
print(Fore.CYAN + "Enter Hijri date in this format: 14/3/1442")
print(Fore.YELLOW + "Type 'exit' to quit.\n")

while True:
    user_input = input(Fore.GREEN + "Enter Hijri date: ").strip()
    
    if user_input.lower() == "exit":
        print(Fore.RED + "Program exited.")
        break

    result = convert_hijri_to_gregorian(user_input)
    if result:
        print(Fore.MAGENTA + f"Gregorian date: {Fore.WHITE + Style.BRIGHT + result}\n")
    else:
        print(Fore.RED + "Invalid date format. Please try again.\n")
