
# Задача 26:

def sqr_ab (a, b):
    if b == 0:
        return 1
    return a * sqr_ab(a, b - 1)
x1 = int(input("Введите a: "))
n1 = int(input("Введите b: "))
print("a в степени b = ",sqr_ab(x1, n1))

# Задача 28
def sum_ab (a, b):
    if b == 0:
        return a
    return sum_ab(a + 1, b - 1)

x2 = int(input("Введите a: "))
n2 = int(input("Введите b: "))
print("a + b = ", sum_ab(x2, n2))
