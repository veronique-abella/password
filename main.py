import hashlib

def check_password_requirements(password):
    length_req = len(password) >= 8
    uppercase_req = any(char.isupper() for char in password)
    lowercase_req = any(char.islower() for char in password)
    digit_req = any(char.isdigit() for char in password)
    special_char_req = any(char in '!@#$%^&*' for char in password)
    
    return length_req and uppercase_req and lowercase_req and digit_req and special_char_req

def hash_password(password):
    hash_object = hashlib.sha256(password.encode())
    hashed_password = hash_object.hexdigest()
    return hashed_password

def main():
    while True:
        user_password = input("Veuillez choisir un mot de passe : ")

        if check_password_requirements(user_password):
            hashed_password = hash_password(user_password)
            print(f"Le mot de passe haché (SHA-256) est : {hashed_password}")
            print("Le mot de passe respecte les exigences de sécurité.")
            break
        else:
            print("Le mot de passe ne respecte pas les exigences de sécurité. Veuillez réessayer.")

if __name__ == "__main__":
    main()
