from ..character_module import Character
import random
import time

# Nexus9 class inherits from Character
# This class represents a rogue AI that has taken control of MegaCorp's systems
class Nexus9(Character):
    def __init__(self, name):
        super().__init__(name="Nexus9", health=150, attack_power=15, character_type="Nexus9")

    def data_surge(self, opponent):
        # Primary attack: random 10-20 damage
        damage = random.randint(10, 20)
        print(f"{self.name} unleashes a relentless data surge, flooding {opponent.name}'s systems with MegaCorp's corrupted code. Neon City's freedom hangs in the balance, as Nexus9 brings down firewalls, and short circuits the efforts of the resistance.")
        print()
        super().attack(opponent, damage)

    def packet_spike(self, opponent):
        # Secondary attack: random 5-15 damage
        damage = random.randint(5, 15)
        print(f"{self.name} sends a piercing packet spike, targeting {opponent.name}'s defenses. MegaCorp's control over the networks grow stronger, threatening Neon City's resistance with every pulse.")
        print()
        super().attack(opponent, damage)

    def crypto_blast(self, opponent):
        # Special ability: double random primary damage (20-40)
        if not self.special_used:
            damage = random.randint(10, 20) * 2
            print(f"{self.name} detonates a catastrophic crypto blast, shattering {opponent.name}'s last chances of overcoming the newly sentient being. Neon City's digital resistance falters, and Nexus9 roars with power.")
            super().special_ability(opponent, damage)
        else:
            print(f"{self.name}'s crypto systems are offline, their blast expended in Neon City's battle. No damage is dealt to the resistance, but MegaCorp's AI remains vigilant.")
            time.sleep(2)