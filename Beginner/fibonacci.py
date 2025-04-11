n = int(input("Enter lenght = "))
a = 0
b = 1
print(a)
for i in range(n):
    
    a, b = b, a+b
    print(a)