import random
random_no = random.randint(1, 100)

guess = int(input("Enter any number ="))


if random_no == guess:
    print("Congratulations you guessed it right")
    print(random_no)

elif random_no > guess:
    print("Your guess is too low")
    print(random_no)

elif random_no < guess:
    print("Your guess is too high")
    print(random_no)

