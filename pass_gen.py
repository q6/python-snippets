# this is a python script that will generate a single password
# user can determine length, characters, exclude characters, how many passwords to generate

from random import choice
from re import sub

# character the password can be made up off
chars_numbers = '1234567890'
chars_alphabet_lower = 'abcdefghijklmnopqrstuwxyz'
chars_alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUWXYZ'
chars_special = '`~!@#$%^&*()-_=+\|]}[{";:/?.>,<*\'"'
sets = [chars_numbers, chars_alphabet_lower, chars_alphabet_upper, chars_special]


# helper function, turns empty string into new_value
def empty_to_new_value(var, new_value=1):
    if var == '':
        return new_value
    return var  # if not empty return the original


def ask_user_password_number():
    # ask user how many passwords to generate
    password_numbers = input('\nHow many password would you like to generate? (Press Enter to generate just 1)\n:')
    password_numbers = empty_to_new_value(password_numbers)  # if no input set to 1
    password_numbers = int(password_numbers)  # is the user entered a number we have to convert from str to int
    return password_numbers


def ask_user_password_length():
    # ask user password length
    length = input('\nHow long should the password be? (Press Enter to generate a 14 character one)\n:')
    length = empty_to_new_value(length, 12)  # if no input set to 12
    length = int(length)  # if the user entered something we have to convert str to int
    return length


def ask_user_char_sets():
    # ask user what characters the password should be made off
    user_char_sets = input('\
    \nPassword can be made up of several character sets. (Press Enter to use all)\
    \n1. numbers: {0}\
    \n2. lower case letters: {1}\
    \n3. upper case letters: {2}\
    \n4. special characters: {3}\
    \nType in the sets you would like to use.\
    \n:'.format(chars_numbers, chars_alphabet_lower, chars_alphabet_upper, chars_special))
    user_char_sets = empty_to_new_value(user_char_sets, '1234')  # if empty use all sets
    return user_char_sets


def generate_password_set(user_char_sets):
    # generate a string the password will be made off
    set_for_password = ''
    for c in user_char_sets:
        set_for_password += sets[int(c)-1]
    return set_for_password


def ask_user_exclude_characters():
    # ask the user if they want to exclude any characters
    chars_exclude = input('\nAre there any character you want to exclude? (If no, press Enter.)\n:')
    chars_exclude = ''.join(set(chars_exclude))  # remove dupes from str
    return chars_exclude


def take_out_exclude_characters(password_set, exclude_characters):
    # take out the chars the user wants to exclude
    # set_for_password = sub(r'{}'.format(exclude_characters), '', password_set)
    new_set = ''
    for c in password_set:
        if c in exclude_characters:
            pass
        else:
            if c not in new_set:
                new_set += c
    return new_set

    print('*'*20)
    print(set_for_password)
    return set_for_password


def generate_passwords(password_numbers, length, set_for_password):
    # generate password from set for a certain number of times
    passwords = []
    print(set_for_password)
    for p in range(password_numbers):
        password = ''
        # generate one password
        for i in range(length):
            password += choice(set_for_password)
        passwords.append(password)
    return '\n'.join(passwords)


def ask_user_parameters_and_generate():
    password_number = ask_user_password_number()
    password_length = ask_user_password_length()
    user_desired_password_sets = ask_user_char_sets()
    password_sets = generate_password_set(user_desired_password_sets)
    exclude_characters = ask_user_exclude_characters()
    password_sets_2 = take_out_exclude_characters(password_sets, exclude_characters)
    generated_passwords = generate_passwords(password_number, password_length, password_sets_2)

    print('Welcome to the password generator.')
    print('\n', '='*10, 'GENERATED PASSWORD', '='*10, '\n', sep='')
    print(generated_passwords)
    print('\n', '='*38, sep='')
    print('\npassword generated from this set:', password_sets_2, sep='\n')
    print('\nThe following characters were excluded:', exclude_characters, sep='\n')


while True:
    ask_user_parameters_and_generate()
    user_continue = input('\nWould you like to generate more passwords?\
\n1. Yes\
\n2. No\
\n:')
    if user_continue != '1':
        break


input('\nPress Enter to exit.')
