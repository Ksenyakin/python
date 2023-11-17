def count_descendants(tree, node):
    # Рекурсивная функция для подсчета числа потомков у узла дерева
    if node not in tree:
        return 0
    descendants = 0
    for child in tree[node]:
        descendants += 1 + count_descendants(tree, child)
    return descendants


def main():
    # Ввод количества элементов в генеалогическом древе
    n = int(input("Введите число элементов в генеалогическом древе N: "))
    tree = {}  # Словарь для представления генеалогического древа

    # Ввод родителей для каждого элемента, кроме родоначальника
    for _ in range(n - 1):
        child, parent = input().split()
        tree.setdefault(parent, []).append(child)

    # Вывод числа потомков для каждого элемента древа
    for node in tree:
        descendants_count = count_descendants(tree, node)
        print(f"У элемента {node} количество потомков: {descendants_count}")

    # Добавление информации о тех, у кого нет потомков
    all_people = set(tree.keys()).union(set(child for children in tree.values() for child in children))
    childless_people = all_people - set(tree.keys())

    for person in childless_people:
        print(f"У элемента {person} нет потомков.")


if __name__ == "__main__":
    main()
