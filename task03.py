# Дана некоторая последовательность вещественных чисел. Необходимо
# написать приложение, которое эффективным способом:
# меняет местами экстремальные элементы (если их несколько, то
# первые/последние из найденных элементов последовательности).


def get_max_number(ls):
    max_number = ls[0]
    max_index_number = 0
    for element in ls:
        if element > max_number:
            max_number = element
            max_index_number = ls.index(max_number)
    return max_index_number


def get_min_number(ls):
    min_number = ls[0]
    min_index_number = 0
    for element in ls:
        if element < min_number:
            min_number = element
            min_index_number = ls.index(min_number)
    return min_index_number


def main():
    ls = []
    print("Input elements of list. For exit input '-1'.")

    while True:
        number = float(input("element: "))
        if number == -1:
            break
        ls.append(int(number))

    result_1 = get_max_number(ls)
    result_2 = get_min_number(ls)

    ls[result_1], ls[result_2] = ls[result_2], ls[result_1]

    print(ls)


main()
