from re import search


txt='Harry Potter and the chaber of secrets'
cute_babies=['kitten', 'kitten', 'puppy', 'kitten', 'puppy', 'puppy', 'puppy', 'puppy']
number2d=[[1, 2, 2, 4], [1, 2, 1, 5], [3, 9, 9, 9], [1, 1, 1, 5], [3, 9, 4, 4]]
def count(o, c):
    counter=0
    for i in range(len(c)):
        if c[i] == o:
            counter=counter+1

    return counter

#print(search('kitten', cute_babies))

print(count('4', number2d))
n=0
for i in range(len(number2d)):
    n=n+count(4, number2d[i])

print(n)