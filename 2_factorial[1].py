def fact(n):  
   if n == 1:  
       return n  
   else:  
       return n*fact(n-1)  

num = int(input("Enter a number: "))   

if num < 0:  
   print("Factorial does not exist for negative numbers")  

elif num == 0:  
   print("The factorial of 0 is 1")  

else:  
   print("The factorial is",fact(num))