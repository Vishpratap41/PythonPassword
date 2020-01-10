import bcrypt
import hmac
from password_strength import PasswordPolicy

class Password:
    def check_complexity(self, password_string):
        policy = PasswordPolicy.from_names(
            length = 8,
            uppercase = 1,
            numbers = 1,  
        )
        testlist = policy.test(password_string)
        if len(testlist) == 0:
            return True
        else: 
            print("Invalid password.")
            return False

    def hash_password(self, password_string):
        hashed_password = bcrypt.hashpw(password_string, bcrypt.gensalt())
        return hashed_password
        
    def hash_check(self, cleartext_password, hashed_password):
        if (hmac.compare_digest(bcrypt.hashpw(cleartext_password, hashed_password), hashed_password)):
            print("Yes")
        else:
            print("No")