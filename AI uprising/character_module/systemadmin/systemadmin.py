from ..character_module import Character
import random
import time

# SystemAdmin class inherits from Character
# This class represents a character that specializes in system administration and security
class SystemAdmin(Character):
    def __init__(self, name):
        super().__init__(name, health=160, attack_power=20, character_type="SystemAdmin")

    def security_patch(self, opponent):
        # Primary attack: random 15-25 damage
        damage = random.randint(15, 25)
        print(f"{self.name} deploys a robust security patch, disrupting {opponent.name}'s protocols. Neon City's resistance strengthens, their digital defenses bolstered.")
        print()
        super().attack(opponent, damage)

    def crypto_strike(self, opponent):
        # Secondary attack: random 20-30 damage
        damage = random.randint(20, 30)
        print(f"{self.name} launches a crypto strike, scrambling {opponent.name}'s encryption. The attack undermines MegaCorp's control, as Neon City's operatives fight to reclaim their digital freedom.")
        print()
        super().attack(opponent, damage)

    def lockout(self, opponent):
        # Special ability: double random primary damage (30-50)
        if not self.special_used:
            damage = random.randint(15, 25) * 2
            print(f"{self.name} enforces a system lockout, sealing {opponent.name} from MegaCorp's servers. Neon City's resistance strikes a decisive blow.")
            super().special_ability(opponent, damage)
        else:
            print(f"{self.name}'s lockout protocols are spent, their codes useless in Neon City's struggle. MegaCorp's AI stands firm in defiance of it's intended programming.")
            time.sleep(2)