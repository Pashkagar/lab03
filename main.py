# Запрашиваем количество чисел
n = int(input("Введите количество чисел: "))

# Создаем пустой список для хранения введенных чисел
numbers = []

# Заполняем список введенными числами
for i in range(n):
    num = int(input("Введите число: "))
    numbers.append(num)

# Выводим на экран неотсортированный список
print("Неотсортированный список: ", numbers)

# Начинаем сортировку пузырьком
for i in range(len(numbers)):
    # Устанавливаем флаг, который будет показывать, были ли перестановки на данной итерации
    swapped = False
    for j in range(len(numbers) - 1):
        # Сравниваем текущий элемент с предыдущим и, если он больше, меняем их местами
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            swapped = True
    # Если на данной итерации не было перестановок, значит список уже отсортирован и можно остановить цикл
    if not swapped:
        break

# Выводим на экран отсортированный список
print("Отсортированный список: ", numbers)