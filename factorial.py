def find_factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)

num = raw_input("What's your number:")
print find_factorial(3)
