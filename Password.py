import bcrypt, hmac, re

class Password:
    def check_complexity(self, password_string):
        uppercaseCount = len(re.findall(r'[A-Z]', password_string))
        digitCount = len(re.findall(r'[0-9]', password_string))
        specialCount = len(re.findall(r'[#?!@$%^&*-=/\]', password_string))
        if len(password_string) < 8 or len(password_string) > 70:
            print("Password should be between 8 and 70 characters!")
        elif uppercaseCount == 0 or uppercaseCount == len(password_string):
            print("You need at least one uppercase and one lowercase character!")
        elif digitCount == 0:
            print("You need at least one numerical character!")
        elif specialCount == 0:
            print("You need at least one special character!")
        else:
            return True
        return False

    def hash_password(self, password_string):
        hashed_password = bcrypt.hashpw(password_string, bcrypt.gensalt())
        return hashed_password
        
    def hash_check(self, cleartext_password, hashed_password):
        if (hmac.compare_digest(bcrypt.hashpw(cleartext_password, hashed_password), hashed_password)):
            print("Yes")
        else:
            print("No")