squares = [1,4,9,18]
sum = 0
for num in squares:
    sum += num
print sum

list = ['glo', 'ritah', 'eve']
if 'eve' in list:
    print 'Yeeeeees'

#print numbers from 0 to 99
for i in range(100):
    print i

fav_movies = [ 'baywatch', 'black panther', 'avengers', 'The mummy' ]
for each_flick in fav_movies:
    print(each_flick)
    print(fav_movies[0])
    print(fav_movies[1])
    print '----------------------'

count = 0
while count < (len(fav_movies)):
    print(fav_movies[count])
    count += 1

isinstance(fav_movies, list)
