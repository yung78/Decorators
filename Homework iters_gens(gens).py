from Homework_decorator import logger
NESTED_LIST = [['a', 'b', 'c'], ['d', 'e', 'f', 'h', False], [1, 2, None]]


# 2.Генераторы

@logger('E:\Учеба\Python proffwork\Hw5 decorators')
def flat_generator_var1(nested_list: list):
    unpack_list = [element for elements in nested_list for element in elements]
    return unpack_list


@logger('E:\Учеба\Python proffwork\Hw5 decorators')
def flat_generator_var2(nested_list: list):
    unpack_gen = (element for elements in nested_list for element in elements)
    return unpack_gen


@logger('E:\Учеба\Python proffwork\Hw5 decorators')
def flat_generator_var3(nested_list: list):
    for elements in nested_list:
        for element in elements:
            yield element


def run2():
    for item in flat_generator_var1(NESTED_LIST):
        print(item, end='  ')
    print()
    for item in flat_generator_var2(NESTED_LIST):
        print(item, end='  ')
    print()
    for item in flat_generator_var3(NESTED_LIST):
        print(item, end='  ')
    print()


run2()

