# ДЗ Урок4 ДЭДЛАЙН 18.05.2023 23 59
# ДЗ: Добавить в проект уникальную реализацию суперспособности  5х героев

import random
from enum import Enum


class Ability(Enum):
    CRITICAL_DAMAGE = 1
    HEAL = 2
    BOOST = 3
    BLOCK_DAMAGE_AND_REVERT = 4


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} | Health: {self.__health} | Damage: {self.__damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    def choose_defence(self, heroes):
        random_hero = random.choice(heroes)
        self.__defence = random_hero.super_ability

    def hit(self, heroes):
        for hero in heroes:
            if hero.health > 0:
                hero.health -= self.damage

    def __str__(self):
        return f'BOSS ' + super().__str__() + f'| Defence: {self.__defence}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, super_ability):
        super().__init__(name, health, damage)
        self.__super_ability = super_ability

    @property
    def super_ability(self):
        return self.__super_ability

    def hit(self, boss):
        boss.health -= self.damage

    def apply_super_power(self, boss, heroes):
        pass


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, Ability.CRITICAL_DAMAGE)

    # 1. Warrior, помимо своего стандартного удара наносит боссу крит,
    # то есть стандартный урон умножается на случайный коэффициент.

    def apply_super_power(self, boss, heroes):
        coefficient = random.randint(2, 5)  # 2,3,4,5
        if boss.health > 0:
            boss.health -= coefficient * self.damage
            print(f'Warrior hits critically {coefficient * self.damage}')


class Magic(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, Ability.BOOST)

    # 3. Magic должен увеличивать атаку каждого героя после
    # каждого раунда на n-ное количество
    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            hero.damage *= random.randint(2, 10)


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, Ability.HEAL)
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0 and self != hero:
                hero.health += self.__heal_points


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, Ability.BLOCK_DAMAGE_AND_REVERT)
        self.__blocked_damage = 0

    @property
    def blocked_damage(self):
        return self.__blocked_damage

    @blocked_damage.setter
    def blocked_damage(self, value):
        self.__blocked_damage = value

    # 2. Berserk, блокирует часть удара босса по себе
    # и прибавляет заблокированный урон к своему урону и возвращает его боссу
    def apply_super_power(self, boss, heroes):
        if boss.health > 0:
            blocked_damage = (self.blocked_damage // 2)
            boss.health -= (blocked_damage + self.damage)


# 5. Golem, который имеет увеличенную жизнь но слабый удар.
# Может принимать на себя 1/5 часть урона исходящего от босса по другим игрока
class Golem(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, Ability.HEAL)
        self.health = health * 2
        self.damage = damage * 0.5

    def apply_super_power(self, boss, heroes):
        self.health -= (boss.damage * len(heroes)) * 0.2


round_number = 1
# 4. Thor, удар по боссу имеет шанс оглушить босса на 1 раунд,
# вследствие чего босс пропускает 1 раунд и не наносит урон героям
boss_stun_posibility = 1 in random.sample(list(range(1, 11)), 5)


def start():
    boss = Boss('Thor', 1000, 50)
    warrior = Warrior('Ahiles', 290, 10)
    doc = Medic('Aged Doc', 250, 5, 15)
    magic = Magic('Druid', 280, 15)
    berserk = Berserk('Max', 270, 10)
    assistant = Medic('Young', 300, 5, 5)
    erjan = Golem('Erjan', 250, 10)
    heroes_list = [warrior, doc, magic, berserk, assistant, erjan]

    show_stats(boss, heroes_list)
    while not is_game_finished(boss, heroes_list):
        if boss_stun_posibility:
            continue
        play_round(boss, heroes_list)


def show_stats(boss, heroes):
    print(f'\nROUND {round_number} --------------')
    print(boss)
    for hero in heroes:
        print(hero)


def is_game_finished(boss, heroes):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True

    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print('Boss won!!!')
    return all_heroes_dead


def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss.choose_defence(heroes)
    boss.hit(heroes)
    for hero in heroes:
        if hero.health > 0 and boss.health > 0 \
                and boss.defence != hero.super_ability:
            hero.hit(boss)
            hero.apply_super_power(boss, heroes)
    show_stats(boss, heroes)


start()
