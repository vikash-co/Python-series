year = int(input("Please type any year = "))
if (year%4 ==0 and year%100 != 0) or year % 400 == 0:
    print("It is leap year")
else:
    print("It is not leap year") 
