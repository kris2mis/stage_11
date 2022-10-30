# Дана некоторая последовательность вещественных чисел. Необходимо напи-
# сать приложение, которое эффективным способом:
# находит экстремальные элементы заданной последовательности (наиболь-
# ший и наименьший элементы последовательности, а также среднеарифме-
# тическое)


def get_max_number(ls):
    max_number = ls[0]
    for element in ls:
        if element > max_number:
            max_number = element
    return max_number


def get_min_number(ls):
    min_number = ls[0]
    for element in ls:
        if element < min_number:
            min_number = element
    return min_number


def find_arifm_avg(ls):
    s = 0
    for element in ls:
        s += element
    return round(s / len(ls), 2)


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
    result_3 = find_arifm_avg(ls)

    msg = (f"Max number: {result_1}.\nMin number: {result_2}.\nArifmetic average: {result_3}.")

    print(ls)
    print(msg)


main()
