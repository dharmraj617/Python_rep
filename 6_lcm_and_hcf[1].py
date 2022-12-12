def lcm(n1,n2):
    if n1 > n2:
        greater = n1
    else:
        greater = n2

    while(True):
        if(greater % n1 == 0 and greater % n2 == 0):
            res = greater
            break
        greater += 1
    return res

def hcf(n1,n2):
    while n2:
        n1, n2 = n2, n1 % n2
    return n1

i1 = int(input("Enter the first number: "))
i2 = int(input("Enter the second number: "))

print("LCM is:",lcm(i1,i2))
print("HCF is:",hcf(i1,i2))

