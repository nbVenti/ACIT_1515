from getpass import getpass

# Add your functions here

def main():
    # password = getpass("Please enter your password: ")
    password = ""
    if strong_password(password):
        print("Strong Password")
    else:
        print("Weak Password")

def strong_password(password:str) -> bool:
    if has_uppercase(password) and has_lowercase(password) and has_number(password) and has_special(password) and has_length(password) and has_consecutive_characters(password):
        return True
    else:
        return False
        

def has_uppercase(password:str) -> bool:
    for i in password:
        if i.isupper():
            # print("is upper")
            return True
    print("no caps")    
    return False


def has_lowercase(password:str) -> bool:
    for i in password:
        if i.islower():
            # print("is lower")
            return True
    print("no lowers")
    return False

    
def has_number(password:str) -> bool:
    for i in password:
        if i.isdigit():
            # print("is digit")
            return True
    print("no numbers")
    return False


def has_special(password:str) -> bool:
    for i in password:
        if i == "~" or "!" or "@" or "$" or "%" or "^" or "&" or "*" or "_" or "+" or "-" or "=":
            # print("is special")
            return True
        
    print("need special")
    return False


def has_length(password:str) -> bool:
    if len((password)) >= 12:
        # print("is long")
        return True
    else:
        return False


def has_consecutive_characters(password:str) -> bool:
    for i in range(len(password)):
        if password[i] != password[i+1]:
    # if len(set(password)) == len(password):
        # print("uh idk good job?")
            return False   
        return True 
    return True


if __name__ == "__main__":
    main()