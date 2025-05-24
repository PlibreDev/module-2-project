from ..character_module import Character
import random
import time



# CodeBreaker class inherits from Character
class CodeBreaker(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35, character_type="Codebreaker")

    def code_injection(self, opponent):
        # Primary attack: random 30-40 damage
        damage = random.randint(30, 40)
        print(f"{self.name} slips a torrent of malicious code into {opponent.name}'s systems, destabilizing MegaCorp's AI. Neon City's underground hackers amplify the chaos, their cheers echoing through the streets.")
        print()
        super().attack(opponent, damage)

    def malware_shot(self, opponent):
        # Secondary attack: fixed 30 damage
        damage = 30
        print(f"{self.name} fires a pinpoint malware shot, corrupting {opponent.name}'s servers. The attack weakens MegaCorp's grip, as Neon City's resistance sabotages the AI's dominion.")
        print()
        super().attack(opponent, damage)

    def data_corrupt(self, opponent):
        # Special ability: double random primary damage (60-80)
        if not self.special_used:
            damage = random.randint(30, 40) * 2
            print(f"{self.name} unleashes a data corruption cascade, crashing {opponent.name}'s systems. Neon City's networks tremble, as the resistance's hackers dismantle the rogue AI's digital throne.")
            super().special_ability(opponent, damage)
        else:
            print(f"{self.name}'s corruption algorithms are depleted, their hacks exhausted in Neon City's fight. MegaCorp's AI laughs, as coffee machines throughout the city hum with unchecked power.")
            time.sleep(2)