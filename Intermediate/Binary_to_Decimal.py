bin = (input("Enter binary no. = "))
bin = bin[::-1]
Total = 0
for i in range(len(bin)):
   sum = int(bin[i]) * (2**i)
   Total += sum 
print(Total)