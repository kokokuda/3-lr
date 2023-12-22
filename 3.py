# 12.  Ввести строку, вывести слово, содержащее наибольшее количество гласных букв.
while True:
    input_string = input("Enter the string (>2 words): ")
    words = input_string.split()
    if len(words) >= 2:
        break
    else:
        print("Enter at least two words.")

max_vowel_word = ""
max_vowel_count = 0

for word in words:
    vowel_count = 0
    for i in word:
        if i in "AEIOUaeiouауоиэыяюеёАУЩИЭЫЯЮЕЁ":
            vowel_count += 1
    if vowel_count > max_vowel_count:
        max_vowel_word = word
        max_vowel_count = vowel_count

if max_vowel_word:
        print("The word with the most vowels:", max_vowel_word)
else:
    print("There are no matching words in the string.")
