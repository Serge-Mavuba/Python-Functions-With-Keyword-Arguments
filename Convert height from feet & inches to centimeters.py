import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

# Define the function cm for centimeters that will accept 2 arguments: feet & inches; then assign a default value of zero for each argument. 
def cm(feet = 0, inches = 0):
    """converts height from feet and inches to centimeters."""
    inches_to_cm = inches * 2.54  # first convert inches to centimeters
    feet_to_cm = feet * 12 * 2.54   # second convert feet to centimeters
    return inches_to_cm + feet_to_cm  # return the combined value

# Here is how we call our function with keyword arguments 
# first lets convert 5 feet to centimeters
cm(feet = 5)
print(cm(feet = 5))
# next convert 70 inches to centimeters
cm(inches = 70)
print(cm(inches = 70))
# lastly convert 5 feet 8 inches to centimeters
cm(feet = 5, inches = 8)
print(Fore.GREEN + Style.BRIGHT + str(cm(feet = 5, inches = 8)))
# FYI- We can also perform this calculation by specifying inches first