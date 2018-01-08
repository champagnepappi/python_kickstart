def add(a,b):
    print "ADDING %d + %d" % (a,b)
    return a + b

def subtract(a,b):
    print "SUBTRACTING %d - %d" %(a,b)
    return a - b

def multiply(a,b):
    print "MULTIPLYING %d * %d" %(a,b)
    return a * b

def divide(a,b):
    print "DIVIDING %d / %d" % (a,b)
    return a / b

print "let's do some math with just functions!"

age = add(30,5)
height = subtract(87,3)
weight = multiply(95,3)
iq = divide(100,2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d " % (age,height,weight,iq)

print "Here is a puzzle"

what  = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "THat becomes:", what, "Can you do it by hand"

