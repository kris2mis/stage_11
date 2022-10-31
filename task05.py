# Необходимо разработать программу, которая проверяет, что все элементы
# вектора расположены в зеркальном виде относительно его середины.


def mirror_sequence(ls_1):
    ls_2 = ls_1[:]
    ls_2.reverse()

    print(ls_1, ls_2)

    return True if ls_1 == ls_2 else False


def main():
    ls_1 = []
    print("Input elements of list. For exit input 'q'.")

    while True:
        number = input("element: ")
        if number == "q":
            break
        ls_1.append(int(number))

    result = mirror_sequence(ls_1)

    msg = (f"It is {result}.")

    print(msg)


main()