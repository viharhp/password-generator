import random
import string

LOWER_CASE = string.ascii_lowercase
UPPER_CASE = string.ascii_uppercase
DIGITS = string.digits
SYMBOLS = string.punctuation

def generate_password(
    length=12,
    use_lowercase=True,
    use_uppercase=True,
    use_digits=True,
    use_symbols=True
):
    """Generate a random password with specified parameters."""
    character_sets = []
    
    if use_lowercase:
        character_sets.append(LOWER_CASE)
    if use_uppercase:
        character_sets.append(UPPER_CASE)
    if use_digits:
        character_sets.append(DIGITS)
    if use_symbols:
        character_sets.append(SYMBOLS)
    
    if not character_sets:
        raise ValueError("Please select at least one character type.")
    
    characters = ''.join(character_sets)
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    try:
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
        
        print("Generated Password:", generated_password)
    except ValueError as e:
        print("Error:", e)
