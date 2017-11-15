pyg = 'ay'

print "Welcome to Pig Latin Translator"

original = raw_input("Enter a word:")

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = word + first + pyg
    new_word = new_word[1:len(new_word)]
    print "Original word is: "+ original
    print "The new word is: " + new_word
else:
    print "empty"

