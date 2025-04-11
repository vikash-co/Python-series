num = int(input("Enter a number = "))
if num ==0 or num == 1:
    print("It is not a prime number")
elif num>1:
    for i in range(2, num):
        if (num%i == 0):
            print("It is not prime Number")
            break
    else:
        print("It is prime Number")

else:
        print("It is not a prime Number")        