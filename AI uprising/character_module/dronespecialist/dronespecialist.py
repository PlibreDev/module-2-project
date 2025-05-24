from ..character_module import Character
import random
import time

# DroneSpecialist class inherits from Character
# This class represents a character that specializes in drone warfare
class DroneSpecialist(Character):
    def __init__(self, name):
        super().__init__(name, health=90, attack_power=30, character_type="DroneSpecialist")

    def drone_strike(self, opponent):
        # Primary attack: random 25-35 damage
        damage = random.randint(25, 35)
        print(f"{self.name} deploys a precision drone strike, bombing {opponent.name}'s MegaCorp server hubs. Neon City's skies buzz with activity.")
        print()
        super().attack(opponent, damage)

    def quick_drone(self, opponent):
        # Secondary attack: two shots, random 10-15 damage each
        for _ in range(2):
            if opponent.health > 0:
                damage = random.randint(10, 15)
                print(f"{self.name} sends a swift drone to harass {opponent.name}, targeting MegaCorp's relays. The attack disrupts the AI's network, fueling Neon City's digital rebellion.")
                print()
                super().attack(opponent, damage)
                if opponent.health <= 0:
                    break

    def drone_swarm(self, opponent):
        # Special ability: double random primary damage (50-70)
        if not self.special_used:
            damage = random.randint(25, 35) * 2
            print(f"{self.name} commands a relentless drone swarm, overwhelming {opponent.name}'s defenses. Neon City's servers plunge into chaos, as the resistance's tech onslaught cripples MegaCorp.")
            super().special_ability(opponent, damage)
        else:
            print(f"{self.name}'s drones are offline, their swarm grounded in Neon City's war. MegaCorp's fortified systems mock the resistance, commanding machines all over the city to malfunction. The city's people can't help but feel the weight of the AI's power as they discover their power diminishes without technology on their side.")
            time.sleep(2)