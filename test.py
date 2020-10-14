n = int(input("Введите количество чисел: "))
#numbers = list(range(0, n))
#print(len(numbers))

#слишком сложно!
numbers = list()
for n in numbers:
    input("Введите число: ")
    numbers.append(n)

print(numbers)


degree = int(input("Введите степень: "))

for i in numbers:
    numbers_raise = numbers[i] ** degree
    print(numbers_raise)
