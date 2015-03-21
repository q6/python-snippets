import cProfile

s = 'If you can read this you have cracked the code piano stairs'

def cypher(s, offset_lst):
    s = list(s.upper())
    num_offsets = len(offset_lst)
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890.'
    len_letters = len(letters)
    for index, char in enumerate(s):
        offset = offset_lst[index % num_offsets]
        char_index = letters.find(char) + offset 
        char_index = char_index % len_letters
        s[index] = letters[char_index] 
    return ''.join(s)


letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890.'
# print(len(letters))
# n = int(input('Enter an int for the offset:\n'))
n = [24, 3, 19, 36, 33, 5, 22]
s = cypher(s, n)
print(s)
n = [len(letters)-o for o in n]
s = cypher(s, n)
print(s)

