try:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    message = str(input("Введите слово, которое нужно защифровать: "))
    result = ""
    key = str(input("Введите ключ: "))

    key *= (len(message) // len(key)) + 1

    for i, j in enumerate(message):
        tmp = alphabet.index(j) + alphabet.index(key[i])

        result += alphabet[tmp % 33 + 1]

    print("Зашифрованное слово:", result)

except ValueError:
    print("Вы ввели некорректные данные")
