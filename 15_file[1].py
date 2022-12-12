file=open("C:\Programs\POE of Python\student.txt", "w")
file.write("I am Poly")

file=open("C:\Programs\POE of Python\student.txt", "r")
print(file.readline())

file=open("C:\Programs\POE of Python\student.txt", "a+")
file.write(" Hey Beautiful")

file=open("C:\Programs\POE of Python\student.txt", "r")
print(file.readline())

file.close