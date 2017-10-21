def is_isogram(word):
    if word == "":
        return (word, False)
    elif type(word) != str:
        raise TypeError('Argument is a string')
    else:
        word = word.lower()
        for char in word:
            if word.count(char) > 1:
                return (word, False)
            else:
                return (word, True)

