
def findRoots(a, b, c):  
  
    f= b * b - 4 * a * c
    f1=f**2
    eq=f1**0.5
    sqrt= (eq)**0.5
  
  
    if f> 0:  
        print(" real and different roots ")  
        print((-b + sqrt) / (2 * a))  
        print((-b - sqrt) / (2 * a))  
  
    elif f == 0:  
        print(" real and same roots")  
        print(-b / (2 * a))  
  
  
    else:  
        print("Complex Roots")  
        print(- b / (2 * a), " + i", sqrt)  
        print(- b / (2 * a), " - i", sqrt)  
  
  
a = int(input('Enter a:'))  
b = int(input('Enter b:'))  
c = int(input('Enter c:'))  
  
# If a is 0, then incorrect equation  
if a == 0:  
    print("Input correct quadratic equation")  
  
else:  
    findRoots(a, b, c)  