def reverse(text):
    string = ""
    l = len(text)
    while l > 0:
        string += text[l-1]
        l -= 1
    return string

print reverse("KEvin")
