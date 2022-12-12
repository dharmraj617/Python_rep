def dec2base():
    a = int(input('Enter decimal number: \t'))
    d = int(input('Enter the base of number system: \t'))
    b = ""
    while a != 0:
        x = '0123456789ABCDEF'
        c = a % d
        c1 = x[c]
        b = str(c1) + b
        a = int(a // d)
    return (b)
print(dec2base())