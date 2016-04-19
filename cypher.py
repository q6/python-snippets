from random import randrange

s = 'There once was a king who lived in castle. Every Monday the king would give a speech. Except this Monday. He had though it was Sunday.'
# s = 'bla bla bla bla bla bla bla'


def cypher(string, offset, len_char_set, char_set):
    """
    A script that uses the ceaser cypher to encrypt text. Instead of
    using the same offset for each letter, it uses a sequence of offsets.
    This sequence looks something like this [23, 43, 6], it can be any length
    greater than zero. If there are more then len(seq) chars in the test
    than it will loop over the seq again.

    see cypher_interactive for input documentation.
    """
    string = list(string)
    num_offsets = len(offset)
    for index, char in enumerate(string):
        offset_this_char = offset[index % num_offsets]  # get the offset for this char
        char_index = char_set.find(char) + offset_this_char
        char_index = char_index % len_char_set  # where the new letter is found in char_set
        string[index] = char_set[char_index]  # change char
    return ''.join(string)


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


# helper function
def add_spaces_to_string_sequence(string):
    """
    Takes a string and returns a string of characters where each character get space padding to a length of max_length
    Ex. string='abde', 'max_length = len(str(len(string)))  # 'abc   def   ghi'  --> 15 --> 2 a  b  d  e'
    string: a string Ex. 'dfasgfqwe'
    """
    max_length = len(str(len(string)))  # 'abc   def   ghi'  --> 15 --> 2
    output = [c.rjust(max_length, ' ') for c in string]
    output = ' '.join(output)
    return output


# helper function
def add_spaces_to_number_sequence(sequence_numbers):
    """
    Takes a number sequence and returns a string of characters where each character get space padding to a length of max_length
    Ex. sequence_numbers=[21, 6, 7, 8, 0, 62] --> '21   6   7   8   0  62'
    sequence_numbers: list of ints Ex. [21, 6, 7, 8, 0, 62]
    """
    max_length = len(str(len(sequence_numbers)))  # 'abc   def   ghi'  --> 15 --> 2
    output = [''.join(str(i)).rjust(max_length, ' ') for i in sequence_numbers]
    output = ' '.join(output)
    return output


def cypher_interactive(string='Hello World', offset=None, show_offset=True, decrypt=True, offset_max_length=20, char_set='auto', show_char_set=True):
    """
    Lets the user run cypher interactively. Preferred method of using cypher()
    Any character that is not in the chars_set will be encrypted as char_set[-1]

    string: String. A string to encrypt.
    offset: None or List. If None it will auto generate a list of random offsets with a max list length of 100. You can specify a offset or let have one generated for you.
    show_offset: Boolean. Show offset when running the command.
    decrypt: Boolean. Decrypt the message at runtime, used to verify the encryption. Will also print the decrypted message.
    offset_max_length: Int. The number of random offsets generated. Default is 20. Only used when no offset is provided
    char_set: None or String. String of char that are in the message. see chars_default for an example.
    """

    # get the char_set
    if char_set == 'auto':
        char_set = build_char_set_from_string(string)  # build a char_set made up of input string

    # print out char_set
    if show_char_set:
        print('Character set')
        print(char_set)

    # if user wants 'auto' offset set the max length to length of string
    if offset_max_length == 'auto':  # offset length is as long as string itself, safest
        offset_max_length = len(string)

    len_char_set = len(char_set)  # used for getting the index of the new letter

    if offset is None:  # no offset list is specified, generate one
        # generate a list of random offsets for encryption
        offset = [randrange(0, len_char_set+1) for i in range(offset_max_length)]  # +1 because randrange is exclusive

    # [1, 2, 3, 4, ...] for the length of the input string, will be used for printing. A simple index of chars
    range_len = list(range(len(string)))

    # show the offset to the user
    if show_offset:
        print('\nOffset')
        print(add_spaces_to_number_sequence(range_len))
        print(add_spaces_to_number_sequence(offset))

    # encrypt
    encrypted_string = cypher(string, offset, len_char_set, char_set)
    print('\nEncrypted String')
    print()
    print(add_spaces_to_number_sequence(range_len))
    print(add_spaces_to_string_sequence(encrypted_string))

    # decrypt
    if decrypt:
        offset = [len_char_set-i for i in offset]  # to decrypt encrypt again
        decrypted_string = cypher(encrypted_string, offset, len_char_set, char_set)
        print('\nDecrypted String')
        print(add_spaces_to_number_sequence(range_len))
        print(add_spaces_to_string_sequence(decrypted_string))

    return encrypted_string

# s = 'Where to be today'
# s = input('Enter a string to encrypt.\n')  # uncomment to allow user to enter a message
cypher_interactive(string=s, show_offset=True, offset_max_length='auto')
# cypher_interactive(string=s, show_offset=True, offset_max_length=10)
# print(build_char_set_from_string(s))
