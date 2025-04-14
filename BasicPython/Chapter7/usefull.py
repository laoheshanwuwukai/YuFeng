'''
7.4
    Local -> Enclose -> Global -> Buidin

'''


def func_map():
    number1 = [1, 2, 3, 4, 5]
    number2 = [4, 5, 6, 7]

    new_number = map(lambda x, y: x+y, number1, number2)
    print(list(new_number))


if __name__ == "__main__":
    func_map()
    pass
