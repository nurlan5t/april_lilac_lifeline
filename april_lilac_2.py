# 1. Создать класс Figure (фигура) с атрибутом уровня класса unit (единица измерения
# величин) и присвоить ему значение cm (сантиметры) или mm (миллиметры)

class Figure:
    unit = 'cm'

    # 2. Создать приватный атрибут perimeter в классе Figure, который бы по умолчанию в
    # конструкторе присваивался к нулю.

    # 3. В конструкторе класса Figure должен быть только 1 входящий параметр self
    def __init__(self):
        self.__perimeter = 0

    # Создать в классе Figure геттер и сеттер для атрибута perimeter.
    @property
    def perimeter(self):
        return self.__perimeter

    @perimeter.setter
    def set_perimeter(self, value):
        self.__perimeter = value

    # 5. Добавить в класс Figure нереализованный публичный метод calculate_area (подсчет
    # площади фигуры)
    def calculate_area(self):
        pass

    # 6. Добавить в класс Figure нереализованный публичный метод calculate_perimeter (подсчет
    # периметра фигуры)
    def calculate_perimeter(self):
        pass

    # 7. Добавить в класс Figure нереализованный публичный метод info (вывод полной
    # информации о фигуре)
    def info(self):
        print(f"unit={self.unit} perimeter={self.__perimeter}")


# 8. Создать класс Square (квадрат), наследовать его от класса Figure
class Square(Figure):

    # 9. Добавить в класс Square атрибут side_length (длина одной стороны квадрата), атрибут
    # должен быть приватным
    def __init__(self, side_length):
        super().__init__()
        self.__side_length = side_length
        # 10. В конструкторе класса Square должен высчитываться периметр квадрата, посредством
        #     вызова метода calculate_perimeter и возвращаемый результат метода задавался бы атрибуту perimeter
        self.__perimeter = self.calculate_perimeter()

    # 11. В классе Square переопределить метод calculate_area, который бы считал и возвращал
    # площадь квадрата.
    def calculate_area(self):
        return self.__side_length ** 2

    # 12. В классе Square переопределить метод calculate_perimeter, который бы считал и
    # возвращал периметр квадрата.
    def calculate_perimeter(self):
        return self.__side_length * 4

    # 13. В классе Square переопределить метод info, который бы распечатывал всю
    # информацию о квадрате следующим образом:
    # Например - Square side length: 5cm, perimeter: 20cm, area: 25cm.
    def info(self):
        print(f"Square side length: {self.__side_length}{self.unit},\n"
              f"perimeter: {self.__perimeter}{self.unit},\n"
              f"area: {self.calculate_area()}{self.unit}.\n")


# 14. Создать класс Rectangle (прямоугольник), наследовать его от класса Figure
class Rectangle(Figure):

    # 15. Добавить в класс Rectangle атрибут length (длина) и width (ширина), атрибуты должны
    # быть приватными.

    # 16. В конструкторе класса Rectangle должен высчитываться периметр прямоугольника,
    # посредством вызова метода calculate_perimeter и возвращаемый результат метода задавался
    # бы атрибуту perimeter
    def __init__(self, length, width):
        super().__init__()
        self.__length = length
        self.__width = width
        self.__perimeter = self.calculate_perimeter()

    # 17. В классе Rectangle переопределить метод calculate_area, который бы считал и
    # возвращал площадь прямоугольника
    def calculate_area(self):
        return self.__length * self.__width

    # 18. В классе Rectangle переопределить метод calculate_perimeter, который бы считал и
    # возвращал периметр прямоугольника.
    def calculate_perimeter(self):
        return (self.__width + self.__length) * 2

    # 19. В классе Rectangle переопределить метод info, который бы распечатывал всю
    # информацию о прямоугольнике следующим образом:
    # Например - Rectangle length: 5cm, width: 8cm, perimeter: 26cm, area: 40cm.
    def info(self):
        print(f"Rectangle length: {self.__length} {self.unit},\n"
              f"Rectangle width: {self.__width} {self.unit},\n"
              f"perimeter: {self.__perimeter} {self.unit},\n"
              f"area: {self.calculate_area()} {self.unit}.\n")


# 20. В исполняемом файле создать список из 2-х разных квадратов и 3-х разных
# прямоугольников
figures_list = [
    Square(3), Square(5),
    Rectangle(5, 8), Rectangle(9, 2), Rectangle(5, 7)
]

# 21. Затем через цикл вызвать у всех объектов списка метод info
for figure in figures_list:
    figure.info()
