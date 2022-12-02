letters = ['b', 'a', 'z']
#numbers = [4, 2, 1, 3]
def swap(lis):
    temp=lis[0]
    lis[0]=lis[1]
    lis[1]=temp

    return lis

#print(swap(letters))

def bubble_sort(lis):
    for n in range(0, len(lis)-1):
        sorted = True
        for e in range(0, len(lis)-(1 + n)):
            if lis[e] > lis[e+1]:
                lis[e], lis[e + 1] = lis[e + 1], lis[e]
                sorted = False

    if sorted:
        return lis

print(bubble_sort(letters))