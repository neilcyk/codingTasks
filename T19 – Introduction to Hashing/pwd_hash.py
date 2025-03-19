import bcrypt

def hash_password(password: str) -> str:

    # Encode the password to bytes
    password_bytes = password.encode('utf-8')
    
    # Generate a salt
    salt = bcrypt.gensalt()
    
    # Hash the password with the salt
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    
    # Return hashed password as a string
    return hashed_password.decode('utf-8')  

# Example usage
user_password = input("Enter a password to hash: ")
hashed_pw = hash_password(user_password)
print(f"Original Password: {user_password}\nHashed Password: {hashed_pw}")