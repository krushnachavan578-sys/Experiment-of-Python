def add(a,b):
    return a+b
def substract(a,b):
    return a-b
def multiply(a,b):
    return(a*b)
def division(a,b):
    return a/b
print("simple calculator")
print("1.addition")
print("2.substraction")
print("3.muiltiplication")
print("4.division")
choice = int(input("Enter your choice (1-4): "))
num1 = float (input("enter first number:"))
num2 = float(input("enter second number:"))
if choice == 1:
    print("result:",add(num1,num2))
elif choice == 2:
    print("result:",substract(num1,num2))
elif choice == 3:
    print("result:",multiply(num1,num2))
elif choice == 4:
    if num != 0:
       print("result:",divide(num1,num2))
    else:
        print("error: division by zero")
else:
    print("invalid choice")
