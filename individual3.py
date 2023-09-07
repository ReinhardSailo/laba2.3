def insert_letter(sentence, letter):
    # Находим последнюю позицию буквы "и" в предложении
    last_i_index = sentence.rfind('и')

    # Если "и" найдена
    if last_i_index != -1:
        # Разбиваем предложение на части до и после последней "и"
        before_i = sentence[:last_i_index]
        after_i = sentence[last_i_index:]

        # Вставляем заданную букву перед последней "и"
        modified_sentence = before_i + letter + after_i

        return modified_sentence
    else:
        return sentence

# Входные данные
sentence = input("Введите предложение (оканчивающееся на точку): ")
letter = input("Введите букву для вставки: ")

# Проверка и вставка буквы
modified_sentence = insert_letter(sentence, letter)

# Вывод результата
print("Измененное предложение:")
print(modified_sentence)
