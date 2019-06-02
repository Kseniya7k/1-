def get_num():
    try:
        num = int(input("Ввведите сдачу(целое положительное число): "))
    except ValueError:
        num = 0
    return num


number = get_num()
while number <= 0:
    print("Некорректные данные.")
    number = get_num()

if number == 0:
    print("Сдача не требуется.")
result = 0
my_list = [50, 10, 5, 1]
for i in range(len(my_list)):
    c = my_list[i]
    cdiv = number // c
    cmod = number % c
    if cdiv > 0:
        result += cdiv
    number = cmod
print("Минимальное количество монет для сдачи: ", result)




