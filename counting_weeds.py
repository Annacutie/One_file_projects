n_weeds = []
for x in range(5):
    n_weeds.append([])
    for y in range(5):
        amount_of_weeds = int(input(f"Enter the number of weed found at {x + 1},{y + 1}: "))
        n_weeds[i].append(amount_of_weeds)
print()  
total = 0
for row in n_weeds:
    for elem in row:
        total+=elem
        print(elem, end=' ')
    print()
print() 
print(f"The total number of weeds found was - {total}")