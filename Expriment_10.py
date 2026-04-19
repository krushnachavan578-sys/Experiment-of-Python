def prime (n) :
    if n<= 1:
        print("Not prime")
        return
    for i in range(2, n):
        if n % i==0:
            print("Not prime")
            return
    print("prime")
num = int(input("Enter a number :  "))
prime(num)
