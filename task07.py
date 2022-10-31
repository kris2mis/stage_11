# Написать программу, которая подсчитывает количество только
# чётных/нечётных элементов вектора.

def calc_even_elements(ls):
    count = 0
    for element in range(len(ls) - 1):
        if ls[element] % 2 == 0:
            count += 1
    return count


def main():
    ls = []
    print("Input elements of list. For exit input '-1'.")

    while True:
        number = float(input("element: "))
        if number == -1:
            break
        ls.append(int(number))

    result = calc_even_elements(ls)

    msg = (f"The count of even elements  is {result}.")

    print(ls)
    print(msg)


main()
