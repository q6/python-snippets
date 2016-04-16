"""
                            PASSWORD GENERATOR
This is a python script that will generate password(s).

User can determine how many password to generate, length of password, what character the password will be made off,
what characters to exclude from the password.
"""

from random import choice

# character the password can be made up off
chars_numbers = '1234567890'
chars_alphabet_lower = 'abcdefghijklmnopqrstuwxyz'
chars_alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUWXYZ'
chars_special = '`~!@#$%^&*()-_=+\|]}[{";:/?.>,<*\'"'
# add all sets together, will be used for determining what chars the password will be made of
chars_sets = [chars_numbers, chars_alphabet_lower, chars_alphabet_upper, chars_special]


def empty_to_new_value(var, new_value=1):
    # helper function, turns empty string into new_value
    if var == '':
        return new_value
    return var  # if not empty return the original


def ask_user_password_quantity():
    # ask user how many passwords to generate
    password_quantity = input('\nHow many passwords would you like to generate? (Press Enter to generate just 1)\n:')
    password_quantity = empty_to_new_value(password_quantity)  # if no input set to 1
    password_quantity = int(password_quantity)  # is the user entered a number we have to convert from str to int
    return password_quantity


def ask_user_password_length():
    # ask user password length
    password_length = input('\nHow long should the password(s) be? (Press Enter to generate a 14 character one)\n:')
    password_length = empty_to_new_value(password_length, 12)  # if no input set to 12
    password_length = int(password_length)  # if the user entered something we have to convert str to int
    return password_length


def ask_user_character_set():
    # ask user what characters the password should be made off
    user_character_set = input('\
    \nPassword can be made up of several character sets. (Press Enter to use all)\
    \n1. numbers: {0}\
    \n2. lower case letters: {1}\
    \n3. upper case letters: {2}\
    \n4. special characters: {3}\
    \nType in the sets you would like to use.\
    \n:'.format(chars_numbers, chars_alphabet_lower, chars_alphabet_upper, chars_special))
    user_char_sets = empty_to_new_value(user_character_set, '1234')  # if empty use all sets
    return user_char_sets


def generate_character_set(user_char_sets):
    # generate a string the password will be made off
    set_for_password = ''
    for c in user_char_sets:
        set_for_password += chars_sets[int(c)-1]
    return set_for_password


def ask_user_exclude_characters():
    # ask the user if they want to exclude any characters
    chars_exclude = input('\nAre there any character you want to exclude? (If no, press Enter.)\n:')
    exclude_characters = ''.join(sorted(set(chars_exclude)))  # remove dupes from string
    return exclude_characters


def take_out_exclude_characters(password_set, exclude_characters):
    # take out the chars the user wants to exclude
    new_set = ''
    for c in password_set:
        if c in exclude_characters:
            pass
        else:
            new_set += c
    return new_set


def generate_passwords(password_quantity, password_length, password_set):
    # generate password from set for a certain number of times (quantity)
    # all_passwords = []  # if you want to return all password uncomment this
    for p in range(password_quantity):
        password = ''
        # generate one password
        for i in range(password_length):
            password += choice(password_set)
        print(password)  # comment if you want to return all passwords instead printing one by one
        # all_passwords.append(password)  # uncomment if you want to return all password
    # return '\n'.join(all_passwords)


def ask_user_parameters_and_generate():
    # this is the master function. It asks the user the necessary question and generates and prints the passwords
    user_password_quantity = ask_user_password_quantity()  # how many passwords
    user_password_length = ask_user_password_length()  # password length
    user_password_sets = ask_user_character_set()  # what the password should be made off
    password_set = generate_character_set(user_password_sets)  # characters password will be made of
    exclude_characters = ask_user_exclude_characters()  # what characters should not be in password
    password_set = take_out_exclude_characters(password_set, exclude_characters)  # remove unwanted character from set
    generated_passwords = generate_passwords(user_password_quantity, user_password_length, password_set)

    # print out final password with header, footer
    print('Welcome to the password generator.')
    print('\n', '='*10, 'GENERATED PASSWORD', '='*10, '\n', sep='')
    print(generated_passwords)
    print('\n', '='*38, sep='')
    print('\npassword generated from this set:', password_set, sep='\n')
    print('\nThe following characters were excluded:', exclude_characters, sep='\n')

# Runs the password generator over again. Allows the user to quit/rerun after any generation.
while True:
    ask_user_parameters_and_generate()
    user_continue = input('\nWould you like to generate more passwords?\
\n1. Yes\
\n2. No\
\n:')
    if user_continue != '1':
        break


input('\nPress Enter to exit.')
