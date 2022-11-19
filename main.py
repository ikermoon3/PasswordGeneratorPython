import random

lower = "abcdefghijklmnñopkrstuvwxyz"
upper = lower.upper()
numbers = "0123456789"

string = lower + upper + numbers
length = 16
password = "".join(random.sample(string, length))

print('Password: '+password)