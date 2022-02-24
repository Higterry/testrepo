def h2h(s):
    if s.isdigit():
        num = int(s)
    elif s == 'A' or s == 'a':
        num = 10
    elif s == 'B' or s == 'b':
        num = 11
    elif s == 'C' or s == 'c':
        num = 12
    elif s == 'D' or s == 'd':
        num = 13
    elif s == 'E' or s == 'e':
        num = 14
    elif s == 'F' or s == 'f':
        num = 15

    b1 = bin(num).replace('0b', '')
    if len(b1) == 1:
        b1 = '000' + b1
    elif len(b1) == 2:
        b1 = '00' + b1
    elif len(b1) == 3:
        b1 = '0' + b1
    b2 = b1[::-1]
    return hex(int(b2, 2))[-1]

a = h2h('3')
