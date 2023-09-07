def correct_words(sequence):
    corrected_sequence = []
    words = sequence.split()

    for word in words:
        # Проверяем наличие "ча" и "ща" в слове и исправляем
        if "ча" in word:
            corrected_word = word.replace("ча", "ша")
        elif "ща" in word:
            corrected_word = word.replace("ща", "ча")
        else:
            corrected_word = word

        corrected_sequence.append(corrected_word)

    return " ".join(corrected_sequence)

# Входные данные
sequence = input("Введите последовательность слов: ")

# Проверка и исправление последовательности
corrected_sequence = correct_words(sequence)

# Вывод результата
print("Исправленная последовательность слов:")
print(corrected_sequence)
