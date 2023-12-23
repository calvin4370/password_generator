import random

""" Version 23/12/23 A
                         NOTES ON STRONG PASSWORDS
---------------------------------------------------------------------------
- at least 12 characters but 14 or more is better
- contains a mix of lowercase (a-z) and uppercase (A-Z) letters
- contains at least 1 number (0-9)
- contains at least 1 special characters (~`! @#$%^&*()-_+={}[]|;:"<>,./?)

NOTE: I removed " and ' to temporarily prevent bugs in code

My generator produces passwords that meet these criteria:
- length of between 12 and 18 characters
- 6-10 alphabet letters of varying capitalisation
- 2-6 numeric digits (0-9)
- 2-6 special characters (~`! @#$%^&*()-_+={}[]|;:<>,./?) inclusive, but missing out " ' \

"""

# CONSTANTS
MIN_PASSWORD_LEN = 12
MAX_PASSWORD_LEN = 18
SPECIALS = "(~`! @#$%^&*()-_+={}[]|;:<>,./?)"

genned_password = ""
def password_generator():
    """Generates a strong password based on guidelines by various organisation"""
    global genned_password
    genned_password = ""

    # Add 6-10 letters, randomly capitalised
    for _ in range(0, random.randint(6, 10)):
        add_letter()
    
    # Add 2-6 numbers
    for _ in range(0, random.randint(2, 6)):
        add_number()
    
    # Add 2-6 special characters
    for _ in range(0, random.randint(2, 6)):
        add_special()
    
    shuffled_password = shuffle(genned_password)

    # Check password generated against my criteria, if failed, run the function again
    if check_password(shuffled_password):
        return shuffled_password
    else:
        return password_generator()


def add_letter():
    global genned_password
    letters = "abcdefghijklmnopqrstuvwxyz"
    capitalise = random.randint(0, 1)
    if capitalise:
        letter = letters[random.randint(0,25)].upper()
    else:
        letter = letters[random.randint(0,25)]
    genned_password += letter

def add_number():
    global genned_password
    number = random.randint(0, 9)
    genned_password += str(number)

def add_special():
    global genned_password
    specials = SPECIALS
    special = specials[random.randint(0,len(specials)-1)]
    genned_password += special

def shuffle(password):
    letter_list = list(password)
    random.shuffle(letter_list)
    password = "".join(letter_list)

    return password

def check_password(password):
    """Checks whether the password put in meets my criteria as stated in the documentation\n
       Returns True/False"""
    lowers = "abcdefghijklmnopqrstuvwxyz"
    uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    specials = SPECIALS
    letter_count = 0
    upper_count = 0
    lower_count = 0
    number_count = 0
    special_count = 0

    if len(password) < MIN_PASSWORD_LEN or len(password) > MAX_PASSWORD_LEN:
        return False

    for char in password:
        if char.lower() in lowers:
            letter_count += 1
            if char in lowers:
                lower_count += 1
            elif char in uppers:
                upper_count += 1
        elif char in numbers:
            number_count += 1
        elif char in specials:
            special_count += 1
        else:
            return False
    
    if upper_count == 0 or lower_count == 0:
        return False
    
    return True