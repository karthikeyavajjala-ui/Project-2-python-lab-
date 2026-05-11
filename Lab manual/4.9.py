#Vowels or consonents

def check_vowel_or_consonant(char):
    vowels="aeiouAEIOU"
    if len(char)!=1 or not char.isalpha():
        return "Invalid input!please enter a single alphabetic character."
    return "Vowel"if char in vowels else "consonant"
char=input("Enter a character: ").strip()
print(check_vowel_or_consonant(char))