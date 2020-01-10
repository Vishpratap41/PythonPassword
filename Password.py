import bcrypt, hmac, re

class Password:
    def check_complexity(self, password_string):
        uppercase_count = len(re.findall(r'[A-Z]', password_string))
        digit_count = len(re.findall(r'[0-9]', password_string))
        special_count = len(re.findall(r'[#?!@$%^&*-=]', password_string))
        if len(password_string) < 8 or len(password_string) > 70:
            print("Password should be between 8 and 70 characters!")
        elif uppercase_count == 0 or uppercase_count == len(password_string):
            print("You need at least one uppercase and one lowercase character!")
        elif digit_count == 0:
            print("You need at least one numerical character!")
        elif special_count == 0:
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