from User import User
from Password import Password
import hashlib
import sys

password = b"bobob001A$"
checkPass = password.decode('utf-8')

user1 = User()
user1.set_name("Bert")

p=Password()

if p.check_complexity(checkPass) == False:
    print("Password not complex enough!")
    exit()
hashed_password = p.hash_password(password)

user1.set_password(hashed_password)
hashed_password = user1.get_password()
p.hash_check(password, hashed_password)


