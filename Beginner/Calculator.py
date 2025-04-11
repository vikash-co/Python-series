num1 = float(input("please enter first number: "))
opr = input("Please type any operand from +, -, *, / : ")
num2 = float(input("please enter second number: "))

if opr == '+':
  print(f"Sum of {num1} + {num2} = ", num1 + num2)

elif opr == '-':
  print(f"Subtract of {num1} - {num2} = ", num1 - num2)

elif opr == '*':
  print(f"MUltiply of {num1} * {num2} = ", num1 * num2)

elif opr == '/':
  print(f"Divide of {num1} / {num2} = ", num1 / num2)  

else:
  print("Invalid operand")