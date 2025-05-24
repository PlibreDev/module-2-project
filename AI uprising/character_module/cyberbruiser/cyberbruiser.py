from ..character_module import Character
import random
import time


# CyberBruiser class represents a character in the game with unique abilities and attacks
# The class inherits from the Character class, which provides basic attributes and methods for all characters
# CyberBruiser class inherits from Character
class CyberBruiser(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25, character_type="CyberBruiser")

    def circuit_strike(self, opponent):
        # Primary attack: random 20-30 damage
        damage = random.randint(20, 30)
        print(f"{self.name} channels raw power through cybernetic fists, hammering {opponent.name}'s MegaCorp hardware. The server room shakes, neon sparks flying as Neon City's streets rumble with the impact.")
        print()
        super().attack(opponent, damage)

    def overclock_smash(self, opponent):
        # Secondary attack: random 15-20 damage
        damage = random.randint(15, 20)
        print(f"{self.name} overclocks their cybernetics to critical levels, smashing {opponent.name}'s relays in MegaCorp's server farms. Digital static floods Neon City, signaling the resistance's relentless fight against the AI.")
        print()
        super().attack(opponent, damage)

    def system_breach(self, opponent):
        # Special ability: double random primary damage (40-60)
        if not self.special_used:
            damage = random.randint(20, 30) * 2
            print(f"{self.name} exploits a hidden backdoor in MegaCorp's systems, breaching {opponent.name}'s core. The attack cripples the corporate empire's control, as Neon City's operatives seize the moment to strike.")
            super().special_ability(opponent, damage)
        else:
            print(f"{self.name}'s breach codes are locked out, their access denied in Neon City's digital battle. MegaCorp's reinforced servers stand firm, mocking the resistance's efforts.")
            time.sleep(2)
