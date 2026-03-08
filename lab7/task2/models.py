from dataclasses import dataclass
import random
from typing import override
from abc import abstractmethod, ABC
from enum import StrEnum


class FoodType(StrEnum):
    MEAT = "Meat"
    MILK = "Milk"

class StudentMajor(StrEnum) :
    SAILOR = "SAILOR"
    IT = "IT"


class HasFightable(ABC):
    @abstractmethod
    def get_health(self):
        pass
    @abstractmethod
    def attack(self, target):
        pass
    @abstractmethod
    def is_alive(self):
        pass  
    @abstractmethod
    def get_fightable(self):
        pass   

@dataclass
class FightableModifiers:
    dmg_multiplier: float = 1.0
    armor_multiplier: float = 1.0
    health_multiplier: float = 1.0
    
class FightableModifiersFactory:
    KMA_MODIFIERS = FightableModifiers(1.4, 2.2, 1.0)
    IT_MODIFIERS = FightableModifiers(1.6, 1.2, 1.0)

    @classmethod
    def get_kma_modifiers(cls):
        return cls.KMA_MODIFIERS
    @classmethod
    def get_it_modifiers(cls):
        return cls.IT_MODIFIERS



class Fightable:
    def __init__(self, owner, mods:FightableModifiers):
        self.owner = owner
        self._health = int(100 * mods.health_multiplier)
        self._damage = int(random.randint(8,11) * mods.dmg_multiplier)
        self._armor = int(random.randint(0,3) * mods.armor_multiplier)
        self._alive = True

    def get_health(self):
        return self._health
    def set_health(self, new_health:int):
        if self._alive:
            self._health = new_health
            if self._health <= 0:
                self.die()
        else:
            print("Dead entity's health can not be manipulated")

    def get_damage(self):
        return self._damage
    def get_armor(self):
        return self._armor
    def is_alive(self):
        return self._alive

    def attack(self, target: HasFightable):
        if self._alive:
            component: Fightable = target.get_fightable()
            component.defend(self)
        else:
            print("Dead entity's can not attack")
    def defend(self, attacker: "Fightable"):
        if self._alive:
            component: Fightable = attacker
            damage_taken:int = int(max( component.get_damage() * random.random() * 1.5 - self.get_armor(), 0))
            print(f"{str(component.owner)} attacks {str(self.owner)}( -{damage_taken} )")
            self.set_health(self.get_health() - damage_taken)
        else:
            print("Dead entity can not be attacked")

    def die(self):
        self._alive = False
        print(f"{str(self.owner)} loses!")








class Student:
    def __init__(self, name:str, age:int):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name
    def set_name(self, new_name:str):
        self._name = new_name


    def get_age(self):
        return self._age
    def set_age(self, new_age:int):
        self._age = new_age


    def eat(self, food: FoodType):
        print(f"{str(self.get_name())} student eats {str(food)}")


    def __str__(self):
        return f"{self.get_name()}<{type(self).__name__}>"
    



class KMAStudent(Student, HasFightable):
    def __init__(self, name, age):
        super().__init__(name, age)
        self._type = StudentMajor.SAILOR
        self._fightable = Fightable(self, FightableModifiersFactory.get_kma_modifiers())

    def attack(self, target: HasFightable):
        self._fightable.attack(target)
    
    def is_alive(self):
        return self._fightable.is_alive()

    def get_health(self):
        return self._fightable.get_health()
    
    def get_fightable(self):
        return self._fightable

    @override
    def __str__(self):
        return f"{self.get_name()}<{self._type.capitalize()}>"
    
class ITStudent(Student, HasFightable):
    def __init__(self, name, age):
        super().__init__(name, age)
        self._type = StudentMajor.IT
        self._fightable = Fightable(self, FightableModifiersFactory.get_it_modifiers())

    def attack(self, target : HasFightable):
        self._fightable.attack(target)

    def is_alive(self):
        return self._fightable.is_alive()
    
    def get_health(self):
        return self._fightable.get_health()

    def get_fightable(self):
        return self._fightable

    @override
    def __str__(self):
        return f"{self.get_name()}<{self._type.capitalize()}>"


    
