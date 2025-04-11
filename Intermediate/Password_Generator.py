import random
import string

def password_generator(lenght=12):
    char = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(char) for i in range(lenght))
    return password
password = password_generator(12)
print("Generated Password: ", password)