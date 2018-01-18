import random

print "Lucky numbers! 3 numbers will be generated."
print "If one of them is a '5', you lose!"

count = 0

while count < 3:
    num = random.randint(1, 6)
