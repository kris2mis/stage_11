# Дана некоторая последовательность вещественных чисел. Необходимо
# написать приложение, которое эффективным способом:
# подсчитывает количество положительных, отрицательных и равных нулю
# элементов последовательности

def calc_positive_numbers(ls):
    count_positive = 0
    for number in ls:
        if number > 0:
            count_positive += 1
    return count_positive


def calc_negative_numbers(ls):
    count_negative = 0
    for number in ls:
        if number < 0:
            count_negative += 1
    return count_negative


def calc_numbers(ls):  # равных нулю
    count_0 = 0
    for number in ls:
        if number == 0:
            count_0 += 1
    return count_0


def main():
    ls = []
    print("Input elements of list. For exit input 'q'.")

    while True:
        number = (input("element: "))
        if number == "q":
            break
        ls.append(int(number))

    result_1 = calc_positive_numbers(ls)
    result_2 = calc_negative_numbers(ls)
    result_3 = calc_numbers(ls)

    msg = (f"Count of positive numbers: {result_1}.\nCount of negative numbers: {result_2}."
           f"\nCount of number [0]: {result_3}.")

    print(ls)
    print(msg)


main()
