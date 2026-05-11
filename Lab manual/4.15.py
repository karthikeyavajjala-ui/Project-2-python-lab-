#generate a random password

import random
import string
def generate_password(n):
    if n<4:
        return "Password length must be at least 4 to include all character types."
    all_chars=string.ascii_letters+string.digits+string.punctuation
    #ensure at least one character  from each required categorey
    password=[random.choice(string.ascii_uppercase),random.choice(string.ascii_lowercase),random.choice(string.digits),random.choice(string.punctuation)]
    #fill the rest of the password with random choices for all_chars
    password+=random.choices(all_chars,k=n-4)
    #shuffle the password to avoid predictable patterns
    random.shuffle(password)
    return" ".join(password)
    #example usage
print(generate_password(12))