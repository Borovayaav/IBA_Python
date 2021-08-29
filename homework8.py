a = int(input('Введите сторону а: '))
b = int(input('Введите сторону b: '))
count = 0
size = []
def square(a, b, count):
    if a == b:
        size.append(a)
        return a, count + 1
    elif a < b:
        size.append(a)
        return square(a, b - a, count + 1)
    else:
        size.append(b)
        return square(b, a - b, count + 1)
ic = square(a, b, count)
branch = " ".join(str(size))
print("Длины отрезанных сторон:"+branch)
print("Всего отрезанных квадратов: " + str(ic[-1]))
