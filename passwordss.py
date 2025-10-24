import bcrypt

def encrypt_password(raw_password):
    return bcrypt.hashpw(raw_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(raw_password, hashed_password):
    """Compare the entered password to the stored hash."""
    return bcrypt.checkpw(raw_password.encode('utf-8'), hashed_password.encode('utf-8'))

def decrypt_password():
        if password and not password.startswith("$2b$"):
             password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        else:
             password = password
