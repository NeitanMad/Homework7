#Задача 34
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

def print_operation_table(operation, num_rows = 9, num_columns = 9):
    for i in range(1, num_rows + 1):
        row = []
        for j in range(1, num_columns + 1):
            row.append(operation(i, j))
        print(*row)


#Задача 34
# Ввод стихотворения
#poem = input("Введите стихотворение: ")
#result = check_rhythm(poem)
#print(result)

# Функция умножения двух чисел
multiply = lambda x, y: x * y

# Вывод таблицы умножения
print_operation_table(multiply)