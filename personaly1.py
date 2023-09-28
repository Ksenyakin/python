import itertools

# Функция для проверки, является ли строка симметричной
def is_symmetric(number_str):
    return number_str == number_str[::-1]

# Функция для поиска максимального симметричного числа из входной строки
def find_max_symmetric_number(input_str):
    digits = []
    for char in input_str:
        if char.isdigit():
            digits.append(char)

    if not digits:
        return "NO"

    # Генерируем все возможные перестановки цифр
    permutations = itertools.permutations(digits)

    max_symmetric_number = None
    for perm in permutations:
        num_str = "".join(perm)
        if is_symmetric(num_str):
          # Если найдено симметричное число, сравниваем его с текущим максимальным
            if max_symmetric_number is None or num_str > max_symmetric_number:
                max_symmetric_number = num_str

    if max_symmetric_number:
        return f"YES {max_symmetric_number}"
    else:
        return "NO"

# Ваш входной набор символов
input_str = input()

# Удаляем точку в конце, если она есть
input_str = input_str.rstrip('.')

result = find_max_symmetric_number(input_str)
print(result)
