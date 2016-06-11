from random import shuffle
from random import randrange
from re import findall

chars_default = '`~!@#$%^&()-_=+\|]}[{"\';:/?.>,<*abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 '  # define globally so all functions have access to it

def encrypt_string(string, offset, char_set):
    """
    A script that uses the Caesar cypher to encrypt text. Instead of
    using the same offset for each letter, it uses a sequence of offsets.
    This sequence looks something like this [23, 43, 6], it can be any length
    greater than zero. If the string is longer than len(offset)
    than it will loop over the seq again.

    string: str Ex. 'Hello World'
    offset: list of ints Ex. [2, 32, 5]
    char_set: str Ex. 'abcdefghijklmnopqrstuwxyz'
    """
    len_char_set = len(char_set)
    string = list(string)  # 'convert the input string to a list of chars. Ex.Hello World' -->  ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
    num_offsets = len(offset)  # how many items are in the offset list? Ex. 3
    for index, char in enumerate(string):
        offset_this_char = offset[index % num_offsets]  # Get the offset that will be used for this char, This is an int from the offset list. will loop over [2, 32, 5]
        char_index = char_set.find(char) + offset_this_char  # the index at which the encrypted is found in char_set that is if char_set was looping indefinitely
        # which it doesn't, so we need to go back to the beginning and go form there)
        char_index %= len_char_set  # the index at which the encrypted version of the char is found, Int
        string[index] = char_set[char_index]  # change char
    return ''.join(string)  # list back to string


def build_char_set_from_string(string):
    """
    A string of every character in another string. Ex. "Hello World" --> "Helo Wrld".
    Useful because a string might have character in it that are not in cypher_interactive's chars_default. This will
    enable users to encrypt any string.
    """
    chars_in_string = set()  # a set of characters in string. A set has no duplicates (python takes care of that)
    for char in string:
        chars_in_string.add(char)
    return ''.join(chars_in_string)


def shuffle_string(string):
    """
    Takes a string and shuffles the order
    Ex. 'monday' --> 'ondyam'
    """
    string = list(string)
    shuffle(string)
    string = ''.join(string)
    return string


# helper function
def add_spaces_to_sequence(str_or_list, max_length=None):
    """
    This is a printing tool
    Takes a string or list and returns a string of characters where each character get space padding to a length of max_length
    str_or_list: a list of ints Ex. [21, 6, 7, 8, 0, 62]
    str_or_list: a str Ex. 'abc   def   ghi'  # just a random str

    Ex. string = 'abc   def   ghi'  --> 15 --> 2 a  b  d  e'
    Ex. sequence_numbers = [21, 6, 7, 8, 0, 62] --> '21   6   7   8   0  62'
    """
    if max_length is None:
        max_length = len(str(len(str_or_list)))  # 'abc   def   ghi'  --> 15 --> 2. Same for list and str

    if type(str_or_list) == 'str':
        output = [c.rjust(max_length, ' ') for c in str_or_list]
    else:  # assume otherwise that it's a list
        output = [''.join(str(i)).rjust(max_length, ' ') for i in str_or_list]
    return ' '.join(output)  # convert list to str


def len_longest_item_in_list(lst):
    """
    list: duh, a list
    returns: Int. Length of the longest item.
    Finds the longest item in list. Long: length in chars. I.e. '312' is longer than '76'
    [1, 2, ... 114] -> 114 -> '114' -> 3 (len of last item in range_len)
    """
    # return len(str(list[-1]))  # this assumes the longest item is the last in the last
    len_longest = 0
    for item in lst:
        if len(str(item)) > len_longest:
            len_longest = len(str(item))

    return len_longest


def print_offset(offset, string, range_len):
    print('\nOffset')

    """
    So unlike the en/decrypted string which can be broken down into single chars the offset list cannot. i.e. 51 into 5, 1 is just silly.
    So we have to evenly space the offset

     0  1  2  3  4  5  6  7  8  9 10 11 12 13 14
     2  5  7  0 33  2  5  7  0 33  2  5  7  0 33
    """
    len_longest_str = max(len_longest_item_in_list(range_len), len_longest_item_in_list(offset))

    if len(offset) < len(
            string):  # if the offset list is shorter than the string we loop the offset until it matches the length of the string
        """
         0 1 2 3 4
         2 5 7
        turns into
         0 1 2 3 4
         2 5 7 2 5
        """
        offset_for_print = offset * (len(string) // len(offset))
        offset_for_print += offset[:(len(string) % len(offset))]
        offset = offset_for_print

    if len(offset) > len(string):
        """
         0  1  2
         2  5  7 33 12 43 29
        turns into
         0  1  2
         2  5  7
        """
        offset = offset[:len(string)]

    # finally print something
    print(add_spaces_to_sequence(range_len, len_longest_str))
    print(add_spaces_to_sequence(offset, len_longest_str))


def print_encrypt(range_len, encrypted_string):  # TODO add docs
    """
    Print an encrypted message.
    Example output
    0  1  2  3  4  5  6  7  8  9 10
    i  t  e  e  e  s  p     n  q
    """
    print('\nEncrypted String')
    print(add_spaces_to_sequence(range_len))
    print(add_spaces_to_sequence(encrypted_string))


def print_decrypt(offset, encrypted_string, char_set, len_char_set=None, range_len=None):  # TODO change so I no longer need to provide len_char_set and range_len
    """
    Print decrypted message

    Example output:
    Decrypted String
    0  1  2  3  4  5  6  7  8  9 10
    j  h  y  y  v  k  i  l  j  v  w
    """
    if len_char_set is None:
        len_char_set = len(char_set)

    if range_len is None:
        range_len = len_string_to_list_range(encrypted_string)



    decrypted_string = decrypt(encrypted_string, offset, char_set, len_char_set)
    print('\nDecrypted String')
    print(add_spaces_to_sequence(range_len))
    print(add_spaces_to_sequence(decrypted_string))


def decrypt(encrypted_string, offset, char_set, len_char_set):
    """
    Decrypt an encrypted message
    encrypted_string: str. A message to decrypt
    offset: list. A list of integers
    char_set: str. A string of chars. Ex. 'abcde'
    """
    offset = [len_char_set - i for i in offset]  # to show_decrypt encrypt again
    decrypted_string = encrypt_string(encrypted_string, offset, char_set)
    return decrypted_string


def generate_offset_list(len_char_set, string=None, offset_length='auto'):
    """
    len_char_set: Int. How long the character set is.
    offset_max_length: Int. How long the List of offsets should be

    If string is not provided offset_length must be

    Ex. [3, 9, 2, 10]
    """
    # if user wants 'auto' offset set the max length to length of string
    if offset_length == 'auto':  # offset length is as long as string itself, safest
        offset_length = len(string)

    # generate a list of random offsets for encryption
    offset = [randrange(0, len_char_set + 1) for i in range(offset_length)]  # +1 because randrange is exclusive
    return offset


def print_char_set(char_set):
    """
    char_set: A string of character.
    """
    print('Character Set')
    print(add_spaces_to_sequence(range(len(char_set))))
    print(add_spaces_to_sequence(char_set))


def verify_cypher(encrypted_string, string, char_set, offset_list):
    """
    check that the decrypted and original message are the same. Just to be sure they are indeed the same, which they really should be.
    """
    len_char_set = len(char_set)
    decrypted_string = decrypt(encrypted_string, offset_list, char_set, len_char_set)
    if string == decrypted_string:
        print('\nDecrypted matches original')
    else:
        print('\nDecrypted does NOT match original')
    print('\nOriginal: ' + string)
    print('Decrypted:' + decrypted_string)
    print('Encrypted:' + encrypted_string)


def len_string_to_list_range(string):
    """
    Generates a list of ints starting at zero increasing sequentially until len(string)
    string: String. Any string
    returns: List of ints
    'Hello' --> [0, 1, 2, 3, 4]
    """
    return list(range(len(string)))


def string_of_int_to_list_of_ints(string_of_ints):
    """
    Convert a string of ints to a list of ints
    string_of_ints: String. A series of integers separated by whitespace
    Ex. '53 6 12 98' --> [53, 6, 12, 98]
    """
    list_of_ints = findall('(\d+)', string_of_ints)  # ['53', '6', '12', '98']
    list_of_ints = [int(i) for i in list_of_ints]  # [53, 6, 12, 98]
    return list_of_ints


def caesar_cypher(string='Hello World', offset='auto', char_set='default', shuffle_char_set=True, offset_length='auto', show_char_set=True, show_encrypt=True, show_decrypt=True, show_offset=True, no_print=False, verify_cypher_option=False, return_type='list'):
    """
    Lets the user run cypher interactively. Preferred method of using cypher()
    Any character that is not in the char_set will be encrypted as char_set[-1]

    string: String. A string to encrypt.
    offset: 'auto' or list of ints. If 'auto' it will auto generate a list of random offsets. You can specify a offset or let have one generated for you.
    char_set: 'auto' or String. String of char that are in the message
    offset_length: Int. The number of random offsets generated. Default is 20. Only used when no offset is provided
    show_char_set: Boolean. Show the char_set which
    show_encrypt: Boolean. Show encrypted string.
    show_decrypt: Boolean. show_decrypt the message at runtime, used to verify the encryption. Will also print the show_decrypted message.
    show_offset: Boolean. Show offset when running the command.
    no_print: Boolean. If True no print statement inside function will run. Simpler than putting False for all the show_bla
    verify_cypher: Boolean. Does the decrypted message match the original input?
    return_type: 'list' or 'dict'. User picks their desired return type. Dictionary has keys but no order, list has only order
    """
    global chars_default  # TODO better than a global var?

    # get the char_set
    if char_set == 'input':
        char_set = build_char_set_from_string(string)  # build a char_set made up of input string
    elif char_set == 'default':
        char_set = chars_default  # use chars_default
    else:
        pass  # if the user provided their own char_set use it

    # randomize the order of the character set
    if shuffle_char_set:
        char_set = shuffle_string(char_set)

    # if user wants 'auto' offset set the max length to length of string
    if offset_length == 'auto':  # offset length is as long as string itself, safest
        offset_length = len(string)

    len_char_set = len(char_set)  # used for getting the index of the new letter

    if offset == 'auto':  # generate a full length offset list
        offset = generate_offset_list(len_char_set, string, offset_length)

    # List, [1, 2, 3, 4, ...] for the length of the input string, will be used for printing. A simple index of chars
    range_len = len_string_to_list_range(string)

    # encrypt
    encrypted_string = encrypt_string(string, offset, char_set)

    # None of the print statements will print
    if no_print is True:
        show_encrypt = False
        show_decrypt = False
        show_char_set = False
        show_offset = False
        verify_cypher_option = False

    # print out char_set
    if show_char_set:
        print_char_set(char_set)

    # show the offset to the user
    if show_offset:
        print_offset(offset, string, range_len)

    # show encrypted string
    if show_encrypt:
        print_encrypt(range_len, encrypted_string)

    # show_decrypt, by default we don't decrypt because there is no point in returning the decrypted string, only used for printing
    if show_decrypt:
        print_decrypt(offset, encrypted_string, char_set, len_char_set, range_len)

    # make sure encrypted message can be decrypted using the encrypted message, offset list, character set
    if verify_cypher_option:
        verify_cypher(encrypted_string, string, char_set, offset)

    # two different ways to return the same data
    if return_type == 'list':
        return [char_set, offset, encrypted_string]  # return a list of required information to decrypt message
    else:
        return {'Character Set': char_set, 'Offset': offset, 'Encrypted String': encrypted_string}  # return a dictionary of required information to decrypt message


def interactive_caesar_cypher():
    greeting = """
=== Welcome to the Interactive Caesar Cypher ===

This is a script that will let you encrypt a message so that it cannot be read without a key.
It's a variation of the Caesar Cypher because not all characters don't have to have the same offset.
In addition to encrypting messages, it can also decrypt messages using a provided key.

The key consists of two (2) items:
   - Character Set ( a list of characters, Ex. ['a', 'b', 'c', ..., 'z', ' '] )
   - Offset Set ( a list of integers, Ex. [6, 7, 7, ...] )
"""

    tutorial = """
=== Tutorial - How to decrypt an encrypted string manually ===

1. Ensure you have:

   Character set
    Index      0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
    Character  a  b  c  d  e  f  g  h  i  j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z

   Encrypted String
    Index      0  1  2  3  4  5  6  7  8  9 10
    Character  n  l  s  m  a  i  c  z  o  j  p

   Offset
    Index   0  1  2  3  4  5  6  7  8  9 10
    Offset  6  7  7  1 13  9  7 11 24 25 12

2. For every character in the encrypted message find that character in the Character Set.
   Example #1
    The letter at index 0 in the encrypted message is 'n'
    'n' in the Character Set is at index 13

   Example #2
    The letter at index 6 is 'c'
    'c' in the Character Set is at index 2

3. In the Offset Set at the same location as the character from step 2 look at the offset number
   ( If in step 2 you were on the 5th letter in the Offset Set look at the 5th offset number )
   Example #1
    The offset at index 0 in the Offset Set is 6

   Example #2
    The offset at index 6 in the Offset Set is 7

4. Subtract the number obtained in step 3 from that obtained in step 2. This will be the decrypted letter
   ( If the resulting number is smaller than 0 add the length of the Character Set to it )
   Example #1
    13 - 6 = 7
    The character at index 7 in the Character Set is 'h'

   Example #2
    2 - 7 = -5
    Because -7 is smaller than 0 we add 27 ( 27 is the length of the Character Set ) to it.
    -5 + 27 = 22
    The character at index 22 in the Character Set is 'w'

5. Repeat process for all characters in the encrypted message and you will have decrypted your message
   Decrypted String
    Index      0  1  2  3  4  5  6  7  8  9 10
    Character  h  e  l  l  o     w  o  r  l  d
"""

    user_options = """
1. Encrypt a string
2. Decrypt a string
3. Tutorial - How to decrypt string manually
4. Exit
:"""  # TODO add background info section

    # greet the user
    print(greeting)


    while True:

        # ask the user what they want to do
        user_choice = input(user_options)

        # user wants to encrypt a string
        if user_choice == '1':

            # let user know they are encrypting a string
            print('=== Encrypt a String ===')

            # ask user to enter a string to encrypt
            user_string = input('Enter a string to encrypt\n:')

            # what kind of character set
            user_char_set = input(
"""
What kind of character set would you like to use?
1. Default set:
    {}
2. Build from input string
3. Custom ( will at least include characters from the input string )
:""".format(chars_default))

            if user_char_set == '1':  # default set
                user_char_set = 'default'  # TODO move char set back into caesar cypher, no need for it to be in global
            elif user_char_set == '2':  # build from input string
                user_char_set = 'input'
            elif user_char_set == '3':  # user want to make own chars set. But at least those c in string have to be included
                user_char_set = input('Enter the characters you want to include in addition to the one in the input string\n:')
                user_char_set = set(build_char_set_from_string(user_string) + user_char_set)
                user_char_set = ''.join(user_char_set)

            # ask the user if they want to shuffle the string
            user_shuffle_char_set = input(
"""
Would you like to shuffle the character set? It is suggested you choose yes to make breaking the cypher more difficult.
Example: 'abcdef' --> 'cefbda'
1. Yes
2. No
:""")
            if user_shuffle_char_set == '1':  # if user wants to shuffle string
                user_shuffle_char_set = True
            else:  # do not shuffle
                user_shuffle_char_set = False

            # ask user what kind of offset list
            user_offset = input(
"""
What kind of offset would you like use?
1. I want to provide a custom offset list
2. Generate one for me
:""")

            # User will enter their own offset list
            if user_offset == '1':
                user_offset = input(
"""
Enter a custom offset list.
Example: "5 32 9 12 7" ( no quotes, only digits and spaces )
:""")
                user_offset = string_of_int_to_list_of_ints(user_offset)
                user_offset_length = 'auto'

            # generate an offset list for user, still need to ask them how long it should be
            elif user_offset == '2':
                user_offset_length = input(
"""
How long should the offset list be?
Enter \'auto\' ( no quotes ) to be the full length of the input string ( this is the secure option )
Or enter a number larger than 0.
:""")
                if user_offset_length == 'auto':  # generate a full length offset list  # TODO find out even though offset is generated here will Caesar cypher generate one anyway because of 'auto'
                    user_offset = 'auto'
                elif user_offset_length.isdigit():  # user entered a number, specified length
                    user_offset_length = int(user_offset_length)
                    user_offset = 'auto'  # TODO find out if this is necessary setting it to auto
                    # user_offset = generate_offset_list(len(user_char_set), offset_length=user_offset_length)

                # user_offset = 'auto'  # DEBUG

            # print('DEBUG'*20)
            # print('string', user_string)
            # print('offset', user_offset)
            # print('offset length', user_offset_length)
            # print('char set', user_char_set)
            # print('user_shuffle_char_set', user_shuffle_char_set)
            caesar_cypher(string=user_string, offset=user_offset, offset_length=user_offset_length, char_set=user_char_set, shuffle_char_set=user_shuffle_char_set, verify_cypher_option=True)

        if user_choice == '2':
            print('=== Decrypt a String ===')
            user_encrypted_string = input("""
To decrypt a string you must provide the following:
    - Encrypted string
    - Offset List
    - Character Set

Please enter the encrypted String
:""")

            user_offset_list = input(
"""
Enter the offset list.
Example: "5 32 9 12 7" ( no quotes, only digits and spaces )
:""")
            user_offset_list = string_of_int_to_list_of_ints(user_offset_list)

            user_char_set_choice = input(
"""
What kind of character set would you like to use?
1. Default
    {}
2. Custom
:""".format(chars_default))

            # use the default character set to decrypt
            if user_char_set_choice == '1':
                user_char_set = chars_default

            # let the user provide their character set
            if user_char_set_choice == '2':
                user_char_set = input(
"""
Enter to character set.
Example: "abcdefghijklmnopqrstuvwxyz 0123456789" ( no quotes )
:""")
            # DEBUG
            print(user_offset_list)
            print(user_encrypted_string)
            print(user_char_set)
            print_decrypt(user_offset_list, user_encrypted_string, user_char_set)


        if user_choice == '3':
            print(tutorial)

        if user_choice == '4':
            print('=== Successfully exited ===')
            break


interactive_caesar_cypher()
