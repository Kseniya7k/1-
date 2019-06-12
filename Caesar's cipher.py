try:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    word = str(input("Введите слово, которое нужно защифровать: "))
    newWord = ""
    key = int(input("Введите ключ: "))

    for i in word:
        if alphabet.index(i) + key > 32:
            newWord = newWord + alphabet[alphabet.index(i) - 33 + key]
        else:
            newWord = newWord + alphabet[alphabet.index(i) + key]
    print("Зашифрованное слово:", newWord)
except ValueError:
    print("Ключ должен быть целым числом без знаков препинания.")
