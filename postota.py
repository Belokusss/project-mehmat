# написание функции
def prostota(x):  # называем функцию как нам нравится
    prostoe = round(x ** 0.5)  # для наибыстрейшей работы кода,берём корень от числа
    for d in range(2, prostoe + 1):  # создаем промежуток от 2-ух до корень из x и с пмощью числа d ищем простые числа
        if x % d == 0:  # если проверяемое число x поделится на d, то число нам не подходит
            return False  # возвращаем False
    return True  # возвращаем True

