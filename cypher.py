from random import shuffle
from random import randrange


def encrypt_string(string, offset, char_set):
    """
    A script that uses the ceaser cypher to encrypt text. Instead of
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
        offset_this_char = offset[index % num_offsets]  # Get the offset that will be used for this char, This is an int from the offest list. will loop over [2, 32, 5]
        char_index = char_set.find(char) + offset_this_char  # the index at which the encrypted is found in char_set that is if char_set was looping indefinitely
        # which it doesn't, so we need to go back to the beginning and go form there)
        char_index = char_index % len_char_set  # the index at which the encrypted version of the char is found, Int
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


def len_longest_item_in_list(list):
    """
    list: duh, a list
    returns: Int. Length of the longest item.
    Finds the longest item in list. Long: length in chars. I.e. '312' is longer than '76'
    [1, 2, ... 114] -> 114 -> '114' -> 3 (len of last item in range_len)
    """
    # return len(str(list[-1]))  # this assumes the loongest item is the last in the last
    len_longest = 0
    for item in list:
        if len(str(item)) > len_longest:
            len_longest = len(str(item))

    return len_longest


def caeser_cypher(string='Hello World', offset='auto', char_set='default', offset_max_length='auto', show_char_set=True, show_encrypt=True, show_decrypt=True, show_offset=True, no_print=False, verify_cypher=False, return_type='list'):
    """
    Lets the user run cypher interactively. Preferred method of using cypher()
    Any character that is not in the char_set will be encrypted as char_set[-1]

    string: String. A string to encrypt.
    offset: 'auto' or list of ints. If 'auto' it will auto generate a list of random offsets. You can specify a offset or let have one generated for you.
    char_set: 'auto' or String. String of char that are in the message
    offset_max_length: Int. The number of random offsets generated. Default is 20. Only used when no offset is provided
    show_char_set: Boolean. Show the char_set which
    show_encrypt: Boolean. Show encrypted string.
    show_decrypt: Boolean. show_decrypt the message at runtime, used to verify the encryption. Will also print the show_decrypted message.
    show_offset: Boolean. Show offset when running the command.
    no_print: Boolean. If True no print statement inside function will run. Simpler than putting False for all the show_bla
    verify_cypher: Boolean. Does the decrypted message match the original input?
    return_type: 'list' or 'dict'. User picks their desired return type. Dictionary has keys but no order, list has only order
    """
    chars_default = '`~!@#$%^&()-_=+\|]}[{"\';:/?.>,<*abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 '
    chars_default = shuffle_string(chars_default)  # shuffle the order of chars_default

    # get the char_set
    if char_set == 'input':
        char_set = build_char_set_from_string(string)  # build a char_set made up of input string
    elif char_set == 'default':
        char_set = chars_default  # use chars_default
    else:
        pass  # if the user provided their own char_set use it

    # if user wants 'auto' offset set the max length to length of string
    if offset_max_length == 'auto':  # offset length is as long as string itself, safest
        offset_max_length = len(string)

    len_char_set = len(char_set)  # used for getting the index of the new letter

    if offset is 'auto':  # no offset list is specified, generate one
        # generate a list of random offsets for encryption
        offset = [randrange(0, len_char_set+1) for i in range(offset_max_length)]  # +1 because randrange is exclusive

    # List, [1, 2, 3, 4, ...] for the length of the input string, will be used for printing. A simple index of chars
    range_len = list(range(len(string)))

    # encrypt
    encrypted_string = encrypt_string(string, offset, char_set)

    # None of the print statements will print
    if no_print is True:
        show_encrypt = False
        show_decrypt = False
        show_char_set = False
        show_offset = False
        verify_cypher = False

    # print out char_set
    if show_char_set:
        print('Character set')
        print(add_spaces_to_sequence(range(len(char_set))))
        print(add_spaces_to_sequence(char_set))

    # show the offset to the user
    if show_offset:
        print('\nOffset')

        """
        So unlike the en/decrypted string which can be broken down into single chars the offset list cannot. i.e. 51 into 5, 1 is just silly.
        So we have to evenly space the offset

         0  1  2  3  4  5  6  7  8  9 10 11 12 13 14
         2  5  7  0 33  2  5  7  0 33  2  5  7  0 33
        """
        len_longest_str = max(len_longest_item_in_list(range_len), len_longest_item_in_list(offset))

        if len(offset) < len(string):  # if the offset list is shorter than the string we loop the offset until it matches the length of the string
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

    # show encrypted string
    if show_encrypt:
        print('\nEncrypted String')
        print(add_spaces_to_sequence(range_len))
        print(add_spaces_to_sequence(encrypted_string))


    def decrypt(encrypted_string, offset, char_set):
        decrypted_string = encrypt_string(encrypted_string, offset, char_set)
        return decrypted_string

    # show_decrypt, by default we don't decrypt because there is no point in returning the decrypted string, only used for printing
    if show_decrypt:
        offset = [len_char_set-i for i in offset]  # to show_decrypt encrypt again
        decrypted_string = decrypt(encrypted_string, offset, char_set)
        print('\nDecrypted String')
        print(add_spaces_to_sequence(range_len))
        print(add_spaces_to_sequence(decrypted_string))

    # check that the decrypted and original message are the same. Just to be sure they are indeed the same, which they really should be.
    if verify_cypher:
        if string == decrypted_string:
            print('\nDecrypted matches original')
        else:
            print('\nDecrypted does NOT match original')
        print('\nOriginal: ' + string)
        print('Decrypted:' + decrypted_string)
        print('Encrypted:' + encrypted_string)

    # two different ways to return the same data
    if return_type == 'list':
        return [char_set, offset, encrypted_string]  # return a list of required information to decrypt message
    else:
        return {'Character Set': char_set, 'Offset': offset, 'Encrypted String': encrypted_string}  # return a dictionary of required information to decrypt message


caeser_cypher(string='This is an example of the Caesar Cypher.', offset=[2, 5, 7], verify_cypher=True)
