myName=input("Enter your Name: ")
print('Your Name is ',myName)

try:
    age=int(input("Age: "))
    print('Your age is ',age)
except ValueError as ve:
    print("Wrong value : ",ve,'Please enter Numbers as your age')
    age=int(input('Age: '))
    print('Your Age is :')