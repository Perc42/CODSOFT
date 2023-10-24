import string
import random

def password_generator(length):
    all = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all) for i in range(length))
    return password

length = int(input("enter length:"))
print(password_generator(length))
