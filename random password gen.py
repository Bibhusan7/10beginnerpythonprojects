import random
length = int(input("enter the length of password: "))
characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
#includes all alphabets (lower and capital), numbers and characters to form a strong password.
p = "".join(random.sample(characters, length))
print(p)