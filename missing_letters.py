def missing_letters(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in string:
        if letter in alphabet:
            alphabet = alphabet.replace(letter, "")
            if len(alphabet) == 0:
                break
    if len(alphabet) == 0:
        print("All letters are present")
    else:
        print(f"Missing letters are: {alphabet}")
given_string = "The quick brown fox jumps over the lazy dog"
given_string1 = "Satyajeet Gaur"

missing_letters(given_string)
missing_letters(given_string1)