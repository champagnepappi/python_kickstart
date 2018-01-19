def reverse(text):
    string = ""
    l = len(text)-1
    while l > 0:
        string += text[l]
        l -= 1
    return string

