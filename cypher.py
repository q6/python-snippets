from random import randrange

s = 'There once was a king who lived in castle. Every Monday the king would give a speech. Except this Monday. He had though it was Sunday.'
# s = 'bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla'


def cypher(s, offset_lst, len_char_set, char_set):
    s = list(s.upper())
    num_offsets = len(offset_lst)
    len_letters = len_char_set
    for index, char in enumerate(s):
        offset = offset_lst[index % num_offsets]
        char_index = char_set.find(char) + offset
        char_index = char_index % len_letters
        s[index] = char_set[char_index]
        # s[index]
        char_set[char_index]
    return ''.join(s)


def cypher_interactive(string='Hello World', offset=None, show_offset=True, decrypt=True, offset_max_length=20, char_set=None):
    """
    Lets the user run cypher interactively. Preferred method of using cypher()

    string: String. A string to encrypt.
    offset: None or List. If None it will auto generate a list of random offsets with a max list length of 100. You can specify a offset or let have one generated for you.
    show_offset: Boolean. Show offset when running the command.
    decrypt: Boolean. Decrypt the message at runtime, used to verify the encryption. Will also print the decrypted message.
    offset_max_length: Int. The number of random offsets generated. Default is 20.
    char_set: None or 'auto'. 'auto' to be implemented.
    """
    chars_default = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890.'  # default char list, not very comprehensive.

    # get the char_set
    if char_set == None:
        # use default chars list
        char_set = chars_default

    # if user wants 'auto' offset set the max length to length of string
    print(type(offset_max_length))
    if offset_max_length == 'auto':  # offset length is as long as string itself, safest
        offset_max_length = len(string)
    # generate a list of random offsets for encryption
    len_char_set = len(char_set)
    offset = [randrange(0, len_char_set+1) for i in range(offset_max_length)]  # +1 because randrange is exclusive


    # show the offset to the user
    if show_offset:
        print(offset)
        print('')

    # encrypt
    encrypted_string = cypher(string, offset, len_char_set, char_set)
    print(encrypted_string)

    # decrypt
    if decrypt:  # and False is debug
        offset = [len_char_set-i for i in offset]  # to decrypt encrypt again
        decrypted_string = cypher(encrypted_string, offset, len_char_set, char_set)
        print('')
        print(decrypted_string)

    return encrypted_string

cypher_interactive(string=s, offset_max_length='auto')

