from modules.printutils import *

class Character:

    def __init__(self, name, hp=16, level=1):
        self.name = name
        self.hp = hp
        self.level = level


class NPC( Character ):

    def __init__(self, name, hp, level, speech):
        super().__init__(name, hp, level)
        self.speech = speech
    
    def speak(self):
        return f"{self.speech}"

alexan = Character('Alexan', 24, 1)
gnarioul = Character('Gnar\'ioul', 83, 5)
fellis = NPC('Fellis', 29, 3, 'I know not of these thieves, now please excuse me.')
marion = NPC('Marion', 8, 1, 'Mother told me to stay outside until dinner, so that\'s what I\'m doing!')

pl(fellis.speak())
pl(marion.speak())