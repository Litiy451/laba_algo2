def factorial(n):
    """
    Вычисляет факториал числа n.

    :param n: целое число, факториал которого нужно вычислить
    :return: факториал числа n
    """
    if n < 0:
        raise ValueError("Факториал определен только для неотрицательных чисел.")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
n=5
print(factorial(5))