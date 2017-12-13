from sys import argv

script, filename = argv

print "We're going to erase %r" % filename
print "if you don't want that hit CTRL-C (^C)"
print "If you do want that hit RETURN"

raw_input("?")
print "OPening file..."
target = open(filename, 'w')
