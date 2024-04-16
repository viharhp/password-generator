import random
import string

def generate_password(length=12, use_lowercase=True, use_uppercase=True, use_digits=True, use_symbols=True):
    characters = []
    
    if use_lowercase:
        characters.extend(string.ascii_lowercase)
    if use_uppercase:
        characters.extend(string.ascii_uppercase)
    if use_digits:
        characters.extend(string.digits)
    if use_symbols:
        characters.extend(string.punctuation)
    
    if not characters:
        print("Error: Please select at least one character type.")
        return None
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    password_length = 16
    include_lowercase = True
    include_uppercase = True
    include_digits = True
    include_symbols = True
    
    generated_password = generate_password(
        length=password_length,
        use_lowercase=include_lowercase,
        use_uppercase=include_uppercase,
        use_digits=include_digits,
        use_symbols=include_symbols
    )
    
    if generated_password:
        print("Generated Password:", generated_password)
