
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def parler(self):
        return "cri animal"

class Chien(Animal):
    def parler(self):
        return "Woof! Woof!"

class Chat(Animal):
    def parler(self):
        return "Meow! Meow!"
