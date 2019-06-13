try:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    word = str(input("Введите слово, которое нужно защифровать: "))
    newWord = ""
    key = int(input("Введите ключ: "))

    for i in word:
        newWord = newWord + alphabet[(alphabet.index(i) + key) % 33]
        
    print("Зашифрованное слово:", newWord)

except ValueError:
    print("Ключ должен быть целым числом без знаков препинания.")
