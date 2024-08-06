num = int(input())
text = input()
nul = 0
for c in text:
    if c.isalpha():
        nul = ord(c)
    elif c.isspace():
        print(" ", end="")
        continue
    else:
        continue
    shift = nul - num
    if shift < 97:
        shift += 26
        print(chr(shift), end='')
    elif 97 <= shift < 122:
        print(chr(shift), end='')