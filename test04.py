# Необходимо разработать программу, которая проверяет, что все элементы
# вектора находятся в упорядоченном виде, т.е. отсортированы по возрастанию
# или убыванию.


def is_ls_sequense(ls):
    for i in range(len(ls) - 1):
        if ls[i] < ls[i + 1]:
            return True
        else:
            return False


def main():
    ls = []
    print("Input elements of list. For exit input '-1'.")

    while True:
        number = float(input("element: "))
        if number == -1:
            break
        ls.append(int(number))

    result = is_ls_sequense(ls)

    msg = (f"It is {result}.")

    print(ls)
    print(msg)


main()
