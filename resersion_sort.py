from os import curdir


numbers = [2, 1, 9, 5]

def resersion_sort(lis):
    for i in range(1, len(lis)):
        current = lis[i]
        position = i
        while position > 0 and lis[position - 1] > current:
            lis[position] = lis[position - 1]
            position = position - 1

        lis[position] = current

    return lis


print(resersion_sort(numbers))