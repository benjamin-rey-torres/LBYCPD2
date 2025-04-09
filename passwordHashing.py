import bcrypt

def returnHashPass(input_pass):
    "Hashes (One-way encryption) password"
    return bcrypt.hashpw(bytes(input_pass,"utf-8"),bcrypt.gensalt())

def checkHashPass(input_pass,req_hash):
    if bcrypt.checkpw(bytes(input_pass,"utf-8"), req_hash):
        return True
    else:
        return False
    
