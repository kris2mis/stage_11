# Необходимо разработать программу, которая проверяет, что все элементы
# вектора различны/одинаковы/

def check_the_same_elements(ls):
    for element in range(len(ls) - 1):
        if ls[element] == ls[element + 1]:
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

    result = check_the_same_elements(ls)

    msg = (f"All elements of list are the same - {result}.")

    print(ls)
    print(msg)


main()
