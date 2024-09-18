import random

#blueprint for player objects
#class definition
class Player:
    name = None
    race = None
    strength = 0
    health = 0

    #constructor
    def __init__(self, name, race, strength=100, health=20):
        self.name = name
        self.race = race
        self.strength = strength
        self.health = health

    def print_stats(self):
        print(f'{self.name} the {self.race} has {self.health} health and {self.strength} strength.')

    def roll_dice(self):
        print(f'Rolling strength dice... 1d{self.strength}')
        roll = random.randint(1, self.strength)
        print(f'Rolled a {roll}')
        return roll

    def attack(self, target):
        print(f'{self.name} attacks {target.name}!')

        self_roll = self.roll_dice()
        target_roll = target.roll_dice()

        if self_roll > target_roll:
            print(f'{self.name} damages {target.name}!!')
            target.health -= 10
        else:
            print(f'{target.name} is too strong! {target.name} damages {self.name}!!')
            self.health -= 10
        
        if self.strength > target.strength:
            print(f'{self.name} damages {target.name}')
            target.health -= 10
            print('-----------------')
            mainPlayer.print_stats()
            secondPlayer.print_stats()
        else:
            print(f'{target.name} is too strong! {target.name} damages {self.name}!!')
            self.health -= 10
            print('-----------------')
            mainPlayer.print_stats()
            secondPlayer.print_stats()

def do_battle(firstPlayer, secondPlayer):
    print('-----------------')
    firstPlayer.attack(secondPlayer)
    secondPlayer.attack(firstPlayer)
    print('-----------------')
    print('Battle Results:')
    firstPlayer.print_stats()
    secondPlayer.print_stats()


#create an instance of the player class
mainPlayer = Player('Bob', 'Elf', strength=200)
mainPlayer.print_stats()

#creates a second player with added health
secondPlayer = Player('Frank', 'Dwarf', health=1000)
secondPlayer.print_stats()

#battle sequence
# mainPlayer.attack(secondPlayer)
# secondPlayer.attack(mainPlayer)
do_battle(mainPlayer, secondPlayer)