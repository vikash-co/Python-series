num = int(input("How many no you want to add = "))
li = []
for i in range(num):
    item = int(input(f"Add {i+1} number = "))
    li.append(item)
min_no = min(li)
max_no = max(li)
print(f"Largest No = {max_no} \nSmallest No = {min_no}")