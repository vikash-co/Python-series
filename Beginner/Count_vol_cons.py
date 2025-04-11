def vol_cons(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0

    for char in text:
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

    return vowel_count, consonant_count

text = input("Type any word = ")
print(vol_cons(text))            