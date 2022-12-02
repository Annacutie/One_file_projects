import random
from count_list_items import count

num_lis = open("numbers.txt", "w")

lis_size = int(input("Enter the amount of numbers you what to get with:"))

r_n=[]
for i in range(lis_size):
    r_n.append(random.randint(0, 100))


def minimum(num):
    m=num[0]    
    for i in num:
        if i < m:
            m=i

    return m

def maximum(num):
    m=num[0]    
    for i in num:
        if i > m:
            m=i

    return m

def display_list(li):
    for n in li:
        print(n)
 

#print(minimum([10, 2, -1, 0, 5]))
#print(maximum([10, 2, -1, 0, 5]))

def options(li, o):
    if o == 'minumum':
       minimum(li)

    elif o == 'maximum':
       maximum(li)

    elif o == 'count seartain numbers':
        counted_number=input('Enter number you want to count: ')

    elif o == 'display the list':
        display_list(li)

    elif  o == 'quilt':
        pass
        # print(count(counted_number,li))

num_lis.write(str(r_n))
num_lis.close()

num_lis_unpack = open("numbers.txt", "r")
lis=num_lis_unpack.read().split(', ')
#print(lis)

option=input('What do you want to do find minimum, maximum, count seartain numbers, display the list or quilt: ').lower()

options(lis, option)

#print(maximum([10, 2, 2, 5, 5, 10]))