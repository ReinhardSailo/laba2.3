def find_occurrences(sentence, char1, char2):
    occurrences = []
    for i in range(len(sentence)):
        if sentence[i] == char1 or sentence[i] == char2:
            occurrences.append(i)
    return occurrences

# Входные данные
sentence = input("Введите предложение: ")
char1 = input("Введите первый символ: ")
char2 = input("Введите второй символ: ")

# Поиск вхождений
result = find_occurrences(sentence, char1, char2)

# Вывод результата
if result:
    print(f"Вхождения символов {char1} и {char2} в предложении:")
    for index in result:
        print(f"Позиция {index}: {sentence[index]}")
else:
    print(f"Символы {char1} и {char2} не найдены в предложении.")
