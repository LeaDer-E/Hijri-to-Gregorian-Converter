from hijri_converter import Hijri
from colorama import init, Fore, Style

# Initialize color support in the Terminal
init(autoreset=True)

# Function to convert Hijri date to Gregorian
def convert_hijri_to_gregorian(hijri_str):
    # Remove leading/trailing whitespace
    hijri_str = hijri_str.strip()
    
    # Check for empty input
    if not hijri_str:
        return None, "Input cannot be empty. Please enter a date in dd/mm/yyyy format.", hijri_str
    
    # Check if the input contains only digits and '/'
    if not all(c.isdigit() or c == '/' for c in hijri_str):
        return None, "Invalid characters. Use only numbers and '/' in dd/mm/yyyy format.", hijri_str
    
    # Split the input string into parts based on "/"
    parts = hijri_str.split('/')
    # Check if the input has exactly 3 parts (day/month/year)
    if len(parts) != 3:
        return None, "Invalid format. Use dd/mm/yyyy (e.g., 01/02/1442).", hijri_str
    
    try:
        # Convert parts to integers
        day, month, year = map(int, parts)
        # Validate ranges for day, month, year
        if not (1 <= month <= 12):
            return None, "Month must be between 1 and 12.", hijri_str
        if not (1 <= year <= 1492):  # Adjusted to reflect typical Hijri year limit
            return None, "Year must be between 1 and 1492 AH.", hijri_str
        if not (1 <= day <= 30):
            return None, "Day must be between 1 and 30.", hijri_str
        
        # Create a Hijri date object and convert it to Gregorian
        greg_date = Hijri(year, month, day).to_gregorian()
        # Return the Gregorian date and the original input for display
        return greg_date.strftime('%d %B %Y'), None, hijri_str
    except (ValueError, OverflowError) as e:
        # Handle invalid Hijri date or out-of-range errors
        return None, f"Invalid Hijri date: {str(e)}. Please ensure the date is within valid range (1-1492 AH).", hijri_str

# Welcome message with ASCII art
print(Fore.CYAN + Style.BRIGHT + """
=========================================
 Hijri to Gregorian Converter - Hebr SA     
=========================================
""")
print(Fore.CYAN + "Enter a Hijri date in the format dd/mm/yyyy (e.g., 14/03/1442 or 01/02/1442)")
print(Fore.YELLOW + "Type 'exit' to quit the program.")
print(Fore.CYAN + "====================================\n")

# Infinite loop to take user input
while True:
    user_input = input(Fore.GREEN + Style.BRIGHT + "Enter Hijri date (dd/mm/yyyy) or 'exit': ")
    
    # Exit the program if the user types 'exit'
    if user_input.lower().strip() == "exit":
        print(Fore.RED + Style.BRIGHT + "\n====================================")
        print(Fore.RED + "Exited. Goodbye!")
        print(Fore.RED + "====================================\n")
        break

    # Attempt to convert the date
    result, error, original_input = convert_hijri_to_gregorian(user_input)
    if result:
        # If conversion is successful, display the result with formatted output
        print(Fore.MAGENTA + Style.BRIGHT + "\n================ Result ===============")
        print(Fore.MAGENTA + f"Hijri date: {Fore.WHITE + Style.BRIGHT + original_input}")
        print(Fore.MAGENTA + f"Gregorian date: {Fore.WHITE + Style.BRIGHT + result}")
        print(Fore.MAGENTA + "======================================\n")
    else:
        # If conversion fails, display a clear error message
        print(Fore.RED + Style.BRIGHT + "\n=============== Error ===============")
        print(Fore.RED + f"Error: {error}")
        print(Fore.RED + "Please try again with a valid Hijri date.")
        print(Fore.RED + "====================================\n")