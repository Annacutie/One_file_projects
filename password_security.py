import string 
def password_checker(password):
    for i in password:
        if len(password)>=8:
            pass 
        elif any(x.isupper() for x in password):
            pass
        elif any(x.islower() for x in password):
            pass
        elif  " " not in password:
            pass
        elif string.is_alfa_numeric():
            pass
        elif string.ispunctuation in password:
            pass
        else:
            return 'unrelible password'

    return 'relible password'
 
print(password_checker('cute Puppy1.'))