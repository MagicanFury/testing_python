"""A Simple login function"""

import hashlib
import mysql

def login(email, pswd, enc = "sha256"):
    if (enc != "sha256"):
        raise Exception("Invalid Encryption Method!")

    hashed = hashlib.sha256(pswd.encode('utf-8')).hexdigest()
    user = mysql.findUser(email, hashed)

    return user

usr = login("ivan.auda@hva.nl", "pass123pass")
print(f"login() returned: {usr}")