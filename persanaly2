from collections import defaultdict

def count_descendants(tree, node):
    # Рекурсивно подсчитываем число потомков для заданного узла
    descendants = 0
    for child in tree[node]:
        descendants += 1 + count_descendants(tree, child)
    return descendants

def main():
    # Ввод количества элементов в генеалогическом древе
    N = int(input("Введите количество элементов в генеалогическом древе: "))

    # Инициализация структуры данных для хранения родственных отношений
    tree = defaultdict(list)
    all_people = set()

    # Ввод родителей для каждого элемента древа, кроме родоначальника
    for _ in range(N - 1):
        child, parent = input().split()
        tree[parent].append(child)
        all_people.add(child)
        all_people.add(parent)

    # Определение числа потомков для каждого элемента и вывод результата
    for node in all_people:
        descendants = count_descendants(tree, node)
        if descendants == 0:
            print(f"Элемент {node} не имеет потомков.")
        else:
            print(f"Элемент {node} имеет {descendants} потомков.")

if __name__ == "__main__":
    main()

# Alexei Peter_1
# Anna Peter_1
# Elizabeth Peter_1
# Petrer_2 Alexei
# Peter_3 Anna
# Paul_1 Peter_3
# Alexander_1 Paul_1
# Nucholaus_1 Paul_1
