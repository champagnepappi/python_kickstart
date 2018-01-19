def digit_sum(n):
    a = 0
    for each in str(n):
      a = a + int(each)

    return a

print digit_sum(4198701)
