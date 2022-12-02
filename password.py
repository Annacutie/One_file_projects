correct_password = "ornery"
password = input("Please enter the password: ")
while password != correct_password:
        password = input("Please enter the password: ")
        print("Sorry, incorrect! Try again.")
else:
    print("Entery gained")

'''
REPEAT
    INPUT password
    PRINT "Sorry, incorrect! Try again."
UNTIL password = correntPassword
PRINT "Entery gained"
'''