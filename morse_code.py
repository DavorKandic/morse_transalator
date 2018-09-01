import sys

letts_nums = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
morse_list =['.-', '-...', '-.-.','-..', '.', '..-.', '--.', '....', '..',
             '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.',
             '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..',
             '.----', '..---', '...--', '....-', '.....', '-....', '--...',
             '---..', '----.', '-----']
def encode(plaintext):
    coded = ''
    for letter in plaintext:
        if letter in letts_nums:
            ind = letts_nums.index(letter)
            coded += morse_list[ind]
        else:
            coded += letter
        coded += ' '
    return coded

def decode(coded):
    plain = ''
    code = ''
    i=0
    while i < len(coded):
        if coded[i] == ' ':
            if coded[i+1] == ' ':
                code += ' | '
            else:
                code += ' '
        else:
            code += coded[i]
        i += 1   
    cod = code.split()
    for sym in cod:
        if sym in morse_list:
            ind = morse_list.index(sym)
            plain += letts_nums[ind]
        elif sym == '|':
            plain += ' '
        else:
            plain += sym
    return plain
            

ans = 'a'    
while (ans != 'e') or (ans != 'd') or (ans != 'q'):
    print()
    ans = input("""Enter 'e' if you want to encode message,
or 'd' if you want to decode message,
or 'q' if you want to quit program: """)
    if ans == 'e':
        print()
        txt = input('Enter your message:\n')
        txt = txt.upper()
        mrs = encode(txt)
        print(mrs)
    elif ans == 'd':
        print()
        print("Separate characters in word with one 'space',\nand words in message with two 'spaces'.")
        mrs = input('Enter your coded message:\n')
        txt = decode(mrs)
        print(txt)
    elif ans == 'q':
        print()
        print("Good bye!")
        sys.exit()
            
