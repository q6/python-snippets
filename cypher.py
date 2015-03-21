
s = 'The Date is 12 may 20 year 4715. King of the Castle.'

def cypher(s, offset):
    s = list(s.upper())
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890.'
    len_letters = len(letters)
    for index, char in enumerate(s):
       char_index = letters.find(char) + offset 
       char_index = char_index % len_letters
       s[index] = letters[char_index] 
    return ''.join(s)


letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890.'
# n = int(input('Enter an int for the offset:\n'))
n = 12
s = cypher(s, n)
print(s)

s = cypher(s, len(letters)-n)
print(s)

