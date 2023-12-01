экземпляр класса инициируются с аргументами: количество деревьев, количество животных. Класс должен реализовывать методы add_trees(value) - добавить указанное количество деревьев к текущему количеству;
remove_trees (value) - удаляет указанное количество деревьев из текущего количества, не может быть меньше нуля. add_animals (value) добавляет указанное количество животных к текущему количеству. 
Remove_animals (value) - удаляет указанное количество животных из текущего количества, не может быть меньше нуля. Get_information() -  возвращает список из значений:[ количество деревьев, количество животных]. 
__str()__возвращает строку вида:”Magic Forest has <количество деревьев> trees and <количество животных> animals”.  экземпляры класса можно сравнивать между собой: сначала по количеству животных, затем по количеству деревьев. 
создать класс наследник от класса “магический лес”, например, “магический лес и с погодой” обязательно использование конструктора. Декораторов и метода __str__


def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"Executing method: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Method {func.__name__} executed successfully")
        return result
    return wrapper

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

    @log_execution
    def enhanced_str(self):
        return f"Enhanced: {super().__str__()} with {self.weather} weather"

# Пример использования с кастомным декоратором
forest = WeatherMagicForest(40, 90, "sunny")
print(forest.enhanced_str())

# Пример использования сравнения
forest1 = MagicForest(20, 60)
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

#Определение декоратора:

# log_execution - это функция-декоратор, которая принимает другую функцию в качестве аргумента (func).
# Определение обёртки:

# wrapper - это внутренняя функция-обёртка, которая вызывает исходную функцию func.
# *args, **kwargs позволяют передавать любое количество позиционных и именованных аргументов.
# Логирование:

# Перед вызовом func, декоратор выводит сообщение о том, что метод будет выполнен.
# После выполнения func, выводится сообщение об успешном выполнении метода.
# Возврат обёртки:

# return wrapper - возвращается обёртка wrapper в качестве результата декоратора.
