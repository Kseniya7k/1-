arr = []

while True:
    try:
        size = int(input("Введите размер поля(3 или 4): "))
        if size == 3 or size == 4:
            break
    except ValueError:
        print("Введены некорректные данные")


def init():
    value = size * size - 1
    for i in range(size):
        arr.append([])
        for j in range(size):
            arr[i].append(value)
            value -= 1
    if size == 4:
        arr[3][1], arr[3][2] = arr[3][2], arr[3][1]


def draw():
    underline = " ________________ " if size == 4 else " ____________ "
    print(underline)
    print("")
    for i in range(size):
        print("|", end="")
        for j in range(size):
            if arr[i][j] == 0:
                print(" _", " ", end="")
            elif 0 < arr[i][j] <= 9:
                print("", arr[i][j], " ", end="")
            else:
                print("", arr[i][j], "", end="")
        print("|")
    print(underline)


def move(step):
    for i in range(size):
        for j in range(size):
            if arr[i][j] == 0:
                break
        if arr[i][j] == 0:
            break

    if step == "w":
        if i != size - 1:
            arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]
    elif step == "d":
        if j != 0:
            arr[i][j], arr[i][j - 1] = arr[i][j - 1], arr[i][j]
    elif step == "s":
        if i != 0:
            arr[i][j], arr[i - 1][j] = arr[i - 1][j], arr[i][j]
    elif step == "a":
        if j != size - 1:
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
    else:
        return print("Некорректный шаг!")


def won():
    counter = 1
    if arr[size - 1][size - 1] != 0:
        return False

    for i in range(size):
        for j in range(size):
            if i != size - 1 and j != size - 1 and arr[i][j] != counter:
                return False
            counter += 1
    return True


init()
draw()
is_victory = won()
print("Для игры необходимо вводить шаги: w - вверх, s - вниз, a - влево, d - вправо")
while not is_victory:
    move(input("Введите шаг: ").lower())
    draw()
    is_victory = won()
print("Победа!")
