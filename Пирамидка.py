try:
    h = int(input("Введите высоту пирамиды: "))
    if h > 0 and h < 24:
        p = " "
        for i in range(h):
            if i == h - 1:
                p = ""
            else:
                p = " "
            p = p * (h - i - 1)
            for j in range(i + 2):
                p += "#"
            print(p)
    else:
        print("Введите число в пределах от 1 до 23.")
except ValueError:
    print("Введите положительное целое число, без точек и запятых")