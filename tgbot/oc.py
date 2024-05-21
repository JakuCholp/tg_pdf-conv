
import random

class Character:
    def __init__(self,name,health,attack_power,defence_power):
        self.name=name
        self.health=health
        self.attack_power=attack_power
        self.defence_power=defence_power
    def attack(self,target):
        damage=self.attack_power-target.defence_power
        if damage>0:
            print(f'{self.name}атакует {target.name} и наносит {damage} урон')
            target.health-=damage
        else:
            print(f'атака {self.name} не пробила защиту {target.name}')
    def heal(self,amount=0):
        self.health+=amount
        print(f'{self.name} восстанавливает {amount}здоровья')
class Warrior(Character):
    def __init__(self, name, health=100, attack_power=20, defence_power=5):
        super().__init__(name, health, attack_power, defence_power)
    def attack(self,target):
        super().attack(target)
        if random.random()<0.8:
            print(f'{self.name} оглушает {target.name}')
            target.defense_power //=2
    def heal(self):
        print(f'{self.name} не умеет лечится')
class Mage(Character):
    def __init__(self, name, health=75, attack_power=15, defence_power=10):
        super().__init__(name, health, attack_power, defence_power)
    def attack(self, target):
        super().attack(target)
        if random.random()<0.3:
            print(f'{self.name} создает  маг щит')
            self.defense_power +=5
    def heal(self, amount=10):
        self.health+=amount    
        print(f'{self.name} восстанавливает {amount}здоровья с помощью магии')
class Archer(Character):
    def __init__(self, name, health=75, attack_power=15, defence_power=10):
        super().__init__(name, health, attack_power, defence_power)
    def attack(self, target):
        super().attack(target)
        if random.random()<0.4:
            print(f'{self.name} делпет залп из двух стрел')
            self.attack(target)
    def heal(self, amount=5):
        self.health+=amount    
        print(f'{self.name} использует целебную траву чтобы восстановить {amount} здоровья')
warrior=Warrior('marat')
mage=Mage('anton') 
archer=Archer('chika')  
def main():
    heroes=[warrior, mage ,archer]      
    while len(heroes)>1:
        random.shuffle(heroes)
        attacker=heroes[0]
        defender=heroes[1]
        action=random.choice(['attack','heal'])
        if action=='attack':
            attacker.attack(defender)
        else:
            attacker.heal()
        if defender.health<=0:
            print('{defender.name} погибает в бою от рук {attacker.name}')
            heroes.remove(defender)
    winner=heroes[0]
    print(f'победитель {winner.name}')
main()

