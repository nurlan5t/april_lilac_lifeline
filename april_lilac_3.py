from enum import Enum


# 1. Создать класс Computer (компьютер) с приватными атрибутами cpu и memory
class Computer:
    def __init__(self, cpu: float, memory: int):
        self.__cpu = cpu
        self.__memory = memory

    def __str__(self):
        return f'Центральный процессор компьютера (производительность): {self.__cpu} ' \
               f'GHz, оперативная память: {self.__memory}Гб'

    def __gt__(self, other):
        return self.__memory > other.__memory

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory

    def __eq__(self, other):
        return self.__memory == other.__memory

    def __ne__(self, other):
        return self.__memory != other.__memory


# 2. Добавить сеттеры и геттеры к существующим атрибутам
    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

# 3. Добавить в класс Computer метод make_computations, в котором бы выполнялись
# арифметические вычисления с атрибутами объекта cpu и memory.
    def make_computations(self):
        return self.__memory + self.__cpu


# sim cards list to choose
class SimCards(Enum):
    O_NurTelecom = 'O!'
    MEGA = 'MEGA'
    BEELINE = 'BEELINE'


# 4. Создать класс Phone (телефон) с приватным полем sim_cards_list (список симкард)
class Phone:
    def __init__(self, name: str, sim_cards_list: list):
        self.name = name
        if isinstance(sim_cards_list, list) and len(sim_cards_list) in (1, 2):
            self.__sim_cards_list = sim_cards_list
        else:
            raise Exception('sim card list must be "list" type and length 1-2!')

# 5. Добавить сеттеры и геттеры к существующему атрибуту.
    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

# 6. Добавить в класс Phone метод call с входящим параметром sim_card_number и call_to_number,
# в котором бы распечатывалась симуляция звонка в зависимости от переданного номера сим-карты
# (например: если при вызове метода передать число 1 и номер телефона, распечатывается текст
# “Идет звонок на номер +996 777 99 88 11” с сим-карты-1 - Beeline).
    def call(self, sim_card_number: SimCards, call_to_number: str):
        if call_to_number[1:].strip().isnumeric():
            return f'"Идет звонок на номер {call_to_number}" с сим-карты - "{sim_card_number}"'
        raise Exception('phone number is incorrect')

    def __str__(self):
        return f'model: "{self.name}" sim cards available: {len(self.sim_cards_list)} {self.sim_cards_list}'


# 7. Создать класс SmartPhone и наследовать его от 2-х классов Computer и Phone.
class SmartPhone(Computer, Phone):
    def __init__(self, name, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, name, sim_cards_list)
        self.__cpu = cpu
        self.__memory = memory
        self.sim_cards_list = sim_cards_list

# 8. Добавить метод в класс SmartPhone use_gps с входящим параметром location,
# который бы распечатывал симуляцию проложения маршрута до локации.
    def use_gps(self, location):
        return f'Маршрут до адреса {location} построен'

    def __str__(self):
        return f'model: {self.name} ' \
               f'Центральный процессор смартфона (производительность): {self.__cpu} ' \
               f'GHz, оперативная память: {self.__memory}Гб ' \
               f'sim cards available: 2 {self.sim_cards_list}'

# 9. В каждом классе переопределить магический метод str которые бы возвращали полную информацию об объекте. (DONE)

# 10. Перезаписать все магические методы сравнения в классе Computer (6 шт.),
# для того чтоб можно было сравнивать между собой объекты, по атрибуту memory. (DONE)


# 11. Создать 1 объект компьютера, 1 объект телефона и 2 объекта смартфона
asus_rog = Computer(4.7, 32)
nokia6233 = Phone(name='Nokia 6233', sim_cards_list=[SimCards.O_NurTelecom.value])
iphone13_pro_max = SmartPhone('iPhone 13 Pro Max', 3.23, 6, [SimCards.MEGA.value, SimCards.O_NurTelecom.value])
redmi_note8pro = SmartPhone('Redmi Note 8 Pro', 2.05, 8, [SimCards.BEELINE.value, SimCards.MEGA.value])
#
# # 12. Распечатать информацию о созданных объектах
# print(asus_rog)
# print(nokia6233)
print(iphone13_pro_max)
# print(redmi_note8pro)
#
# # 13. Опробовать все возможные методы каждого объекта
# # (например: use_gps, make_computations, call, а также магические методы)
# print(iphone13_pro_max > redmi_note8pro)
# print(iphone13_pro_max < redmi_note8pro)
# print(iphone13_pro_max >= redmi_note8pro)
print(iphone13_pro_max <= redmi_note8pro)
# print(iphone13_pro_max == redmi_note8pro)
print(iphone13_pro_max != redmi_note8pro)
print(redmi_note8pro.use_gps('Tokmok'))
print('make computation iPhone13 (cpu + memory):', iphone13_pro_max.make_computations())
print(nokia6233.call(nokia6233.sim_cards_list[0], '+996500449444'))
