from Swordsman import Swordsman
from Archer import Archer
from Magician import Magician
import random

class Boss(Swordsman, Archer, Magician): #Multiple Inheritance
    def __init__(self, username):
        super().__init__(username)
        self.setStr(10)
        self.setVit(25)
        self.setInt(5)
        self.setHp(self.getHp()+self.getVit())
        self.setMaxHp(self.getMaxHp()+self.getVit())
        attackPattern = [1,1,1,1,1,random.randint(1,4),random.randint(1,4),random.randint(1,4),random.randint(1,4)]
        self.attackPattern = random.sample(attackPattern, len(attackPattern))
    def attack(self, opponent):
        attack_choice = random.choice(["basic", "slash", "ranged", "magic", "heal"])
        if attack_choice == "basic":
            opponent.reduceHp(self.getDamage())
            print(f"{self.getUsername()} performed Basic Attack! -{self.getDamage()}")
        elif attack_choice == "slash":
            damage = self.getDamage() + random.randint(0, 5)
            opponent.reduceHp(damage)
            print(f"{self.getUsername()} performed Slash Attack! -{damage}")
        elif attack_choice == "ranged":
            damage = self.getDamage() - random.randint(0, 5)
            opponent.reduceHp(damage)
            print(f"{self.getUsername()} performed Ranged Attack! -{damage}")
        elif attack_choice == "magic":
            damage = self.getDamage() + random.randint(5, 10)
            opponent.reduceHp(damage)
            print(f"{self.getUsername()} performed Magic Attack! -{damage}")
        elif attack_choice == "heal":
            self.addHp(random.randint(5, 15))
            print(f"{self.getUsername()} performed Heal! +{self.getHp()}")