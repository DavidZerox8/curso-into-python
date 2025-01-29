from abc import ABC, abstractmethod
from typing import List, Optional
import random

# Abstract base classes
class Character(ABC):
    def __init__(self, name: str, health: int, attack: int, defense: int):
        self.name = name
        self.health = health
        self.max_health = health
        self.attack = attack
        self.defense = defense

    @property
    def is_alive(self) -> bool:
        return self.health > 0

    def take_damage(self, damage: int) -> None:
        self.health = max(0, self.health - max(0, damage))

class Equipment(ABC):
    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value

# Character classes
class Human(Character):
    def __init__(self, name: str, health: int, attack: int, defense: int, mana: int):
        super().__init__(name, health, attack, defense)
        self.mana = mana
        self.max_mana = mana

class Warrior(Human):
    def __init__(self, name: str, health=100, attack=20, defense=10, mana=0):
        super().__init__(name, health, attack, defense, mana)
        self.rage = 0

    def calculate_damage(self, weapon: 'Weapon') -> int:
        if self.rage >= 100:
            self.rage = 0
            return self.attack + weapon.value * 2
        self.rage += 10
        return self.attack + weapon.value

class Wizard(Human):
    def __init__(self, name: str, health=80, attack=15, defense=5, mana=100):
        super().__init__(name, health, attack, defense, mana)
        self.intelligence = 10

    def calculate_damage(self, weapon: 'Weapon') -> int:
        if self.mana >= 50:
            self.mana -= 50
            return self.attack + weapon.value * 2
        self.mana += 10
        return self.attack + weapon.value

class Monster(Character):
    def __init__(self, name: str, health: int, attack: int, defense: int, special_damage: int):
        super().__init__(name, health, attack, defense)
        self.special_damage = special_damage

    def calculate_damage(self) -> int:
        return self.attack + self.special_damage

class Dragon(Monster):
    def __init__(self, name="Dragon", health=200, attack=25, defense=15):
        super().__init__(name, health, attack, defense, special_damage=15)

class Demon(Monster):
    def __init__(self, name="Demon", health=150, attack=30, defense=10):
        super().__init__(name, health, attack, defense, special_damage=20)

# Equipment classes
class Weapon(Equipment):
    pass

class Armor(Equipment):
    pass

# Combat System
class CombatSystem:
    @staticmethod
    def attack(attacker: Character, defender: Character, weapon: Optional[Weapon] = None) -> int:
        if isinstance(attacker, (Warrior, Wizard)):
            damage = attacker.calculate_damage(weapon)
        else:
            damage = attacker.calculate_damage()
        
        defender.take_damage(damage - defender.defense)
        return damage

# Game Manager
class GameManager:
    def __init__(self):
        self.players: List[Human] = []
        self.monsters: List[Monster] = []
        self.player_weapons: List[Weapon] = []
        self.player_armors: List[List[Armor]] = []
        self.combat_system = CombatSystem()

    def setup_game(self):
        self._setup_players()
        self.monsters = [Dragon(), Demon()]

    def _setup_players(self):
        for i in range(2):
            player = self._create_player(i + 1)
            weapon = self._select_weapon(i + 1)
            self.players.append(player)
            self.player_weapons.append(weapon)

    def _create_player(self, player_num: int) -> Human:
        print(f"\nPlayer {player_num} select your class:")
        print("1. Warrior")
        print("2. Wizard")
        choice = input("Select an option: ")
        name = input("Enter your name: ")
        return Warrior(name) if choice == "1" else Wizard(name)

    def _select_weapon(self, player_num: int) -> Weapon:
        print(f"\nPlayer {player_num} select your weapon:")
        print("1. Sword")
        print("2. Staff")
        print("3. Axe")
        choice = input("Select an option: ")
        weapons = {
            "1": Weapon("Sword", 10),
            "2": Weapon("Staff", 5),
            "3": Weapon("Axe", 15)
        }
        return weapons.get(choice, weapons["1"])

    def get_valid_target(self) -> Monster:
        while True:
            print("1. Attack Dragon")
            print("2. Attack Demon")
            print("3. Pass")
            option = input("Select an option: ")
            
            if option == "3":
                return None
            
            target = self.monsters[0] if option == "1" else self.monsters[1]
            if target.is_alive:
                return target
            print(f"\nThe {target.name} is already defeated! Choose another target.")

    def play_turn(self, player: Human, weapon: Weapon):
        if not player.is_alive:
            return

        print(f"\n{player.name}'s turn:")
        target = self.get_valid_target()
        if target:
            damage = self.combat_system.attack(player, target, weapon)
            print(f"{player.name} attacks {target.name} with {weapon.name} for {damage} damage!")

    def monster_turn(self):
        alive_players = [p for p in self.players if p.is_alive]
        if not alive_players:
            return
            
        for monster in self.monsters:
            if monster.is_alive:
                target = random.choice(alive_players)
                damage = self.combat_system.attack(monster, target)
                print(f"{monster.name} attacks {target.name} for {damage} damage!")

    def print_status(self):
        print("\nStatus:")
        for character in self.players + self.monsters:
            print(f"{character.name} - Health: {character.health}")

    def check_game_over(self) -> bool:
        if not any(monster.is_alive for monster in self.monsters):
            print("\nYou defeated all monsters!")
            return True
        if not any(player.is_alive for player in self.players):
            print("\nAll players have been defeated!")
            return True
        return False

    def play(self):
        self.setup_game()
        while True:
            for i, player in enumerate(self.players):
                self.play_turn(player, self.player_weapons[i])
            
            self.monster_turn()
            self.print_status()
            
            if self.check_game_over():
                break

if __name__ == "__main__":
    game = GameManager()
    game.play()
