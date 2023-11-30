class MagicForest:
    def __init__(self, num_trees, num_animals): #Инициализация атрибутов
        self.num_trees = num_trees
        self.num_animals = num_animals

    def add_trees(self, value):
        self.num_trees += value

    def remove_trees(self, value):
        self.num_trees = max(0, self.num_trees - value)

    def add_animals(self, value):
        self.num_animals += value

    def remove_animals(self, value):
        self.num_animals = max(0, self.num_animals - value)

    def get_information(self):
        return [self.num_trees, self.num_animals]

    def __str__(self): #позволяет определить строковое представление объекта
        return f"In the Magic Forest, there are {self.num_trees} trees and {self.num_animals} animals"

    def compare(self, other, key='animals'):
        if key == 'animals':
            return self.num_animals - other.num_animals
        elif key == 'trees':
            return self.num_trees - other.num_trees
        else:
            raise ValueError("Неверный ключ для сравнения")

class WeatherMagicForest(MagicForest):
    def __init__(self, num_trees, num_animals, weather):
        super().__init__(num_trees, num_animals)
        self.weather = weather

    def set_weather(self, new_weather):
        self.weather = new_weather

    def __str__(self):
        return f"Magic Forest with {self.weather} weather contains {self.num_trees} trees and {self.num_animals} animals"


# Пример использования сравнения
forest1 = MagicForest(50, 100)
forest2 = MagicForest(30, 80)

comparison_key = str(input("animals or trees: "))  # Выбираем параметр сравнения

if forest1.compare(forest2, key=comparison_key) == 0:
    print(f"The number of {comparison_key} in forest 1 is equal to forest 2.")
elif forest1.compare(forest2, key=comparison_key) > 0:
    print(f"Forest 1 has more {comparison_key} than forest 2.")
else:
    print(f"Forest 2 has more {comparison_key} than forest 1.")


# Человеческий вывод
forest1 = MagicForest(50, 100)
print(forest1)  # Magic Forest содержит 50 деревьев и 100 животных


# Инфа о кол-во деревьев и животных
forest2 = MagicForest(30, 80)
print(forest2.get_information())  # [30, 80]


# Добавление/удаление
forest1.add_trees(20)
forest1.remove_animals(30)
print(forest1)  # Magic Forest содержит 70 деревьев и 70 животных


#Работа с наследнком
weather_forest = WeatherMagicForest(40, 90, "sunny")
weather_forest.add_trees(20)
print(weather_forest)  # Magic Forest с солнечной погодой содержит 40 деревьев и 90 животных

weather_forest.set_weather("rainy")
print(weather_forest)  # Magic Forest с дождливой погодой содержит 40 деревьев и 90 животных
