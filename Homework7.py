def check_rhythm(poem):
    phrases = poem.split()
    syllables = []

    for phrase in phrases:
        words = phrase.split('-')
        num_syllables = 0

        for word in words:
            num_syllables += count_vowels(word)
        syllables.append(num_syllables)

    if len(set(syllables)) == 1:
        return "Парам пам-пам"
    else:
        return "Пам парам"

def count_vowels(word):
    vowels = 'уеыаоэяиюУЕЫАОЭЯИЮ'
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count

# Ввод стихотворения
poem = input("Введите стихотворение: ")
result = check_rhythm(poem)
print(result)