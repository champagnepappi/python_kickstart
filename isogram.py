def is_isogram(word):
    if word == "":
        return (word, False)
    elif type(word) != str:
        raise TypeError('Argument is a string')
