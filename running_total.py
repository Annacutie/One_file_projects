def add_numbers():
    total=0
    answer=input("do you what to enter a numbers to add: ")
    while answer == 'yes':
        number=int(input("Enter your number: "))
        answer=input("do you what to enter a numbers to add: ")
        total=total+number
    else:
        print(f'Your total is {total}')

def add_up(li):
    total=0
    for i in li:
        print(i)
        total=total+i

    print(f'total is {total}')

add_up([2, 3, 8])