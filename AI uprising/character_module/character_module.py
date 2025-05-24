import random
import time


class Character:   
    def __init__(self, name, health, attack_power, character_type):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.character_type = character_type
        self.max_health = health
        self.special_used = False

    def attack(self, opponent, damage):
        # Handle primary and secondary attacks with random outcomes
        outcome = random.random()
        if outcome < 0.1:  # 10% total chance
            if outcome < 0.025:  # 2.5% evade
                if self.character_type == "Nexus9":
                    print(f"In a flash of digital cunning, {self.name} reroutes the server grid, evading {opponent.name}'s attack. Neon City's neon-lit skyline pulses defiantly, as the AI's defenses thwart the resistance.")
                    time.sleep(1)
                    return
                else:
                    print(f"In a flash of digital cunning, {opponent.name} reroutes the server grid, evading the attack. Neon City's neon-lit skyline flickers in protest, as the resistance's hope wavers against the AI's defenses.")
                    time.sleep(1)
                    return
            elif outcome < 0.05:  # 2.5% smash
                damage = int(damage * 1.5)
                if self.character_type == "Nexus9":
                    print(f"{self.name} unleashes a catastrophic surge, shattering {opponent.name}'s hardware in Neon City's core. Neon sparks erupt, dealing {damage} damage as MegaCorp's AI crushes the resistance's hope.")
                else:
                    print(f"{self.name} unleashes a catastrophic surge, shattering {opponent.name}'s hardware in the fortified core. Neon sparks erupt, dealing {damage} damage as Neon City's operatives rally against MegaCorp's tyranny.")
            elif outcome < 0.075:  # 2.5% hack
                damage += 10
                if self.character_type == "Nexus9":
                    print(f"{self.name} slices through {opponent.name}'s algorithms, sowing chaos in their systems. Neon City's resistance falters, taking {damage} damage as MegaCorp's AI tightens its grip.")
                else:
                    print(f"{self.name} slices through {opponent.name}'s algorithms, sowing chaos in the AI's network. Neon City's underground hackers amplify the breach, dealing {damage} damage.")
            else:  # 2.5% invalid_password
                damage = damage // 2
                if self.character_type == "Nexus9":
                    print(f"{opponent.name}'s outdated security keys falter under {self.name}'s assault, reducing the attack to {damage} damage. Neon City's resistance persists, but MegaCorp's digital fortress looms stronger.")
                else:
                    print(f"{opponent.name}'s outdated security keys falter under {self.name}'s assault, reducing the attack to {damage} damage. MegaCorp's digital fortress holds firm, as Neon City's resistance faces a setback.")
        else:
            if self.character_type == "Nexus9":
                print(f"The attack penetrates {opponent.name}'s systems, striking with MegaCorp's corrupted code. Neon City's resistance loses momentum, taking {damage} damage as the AI's neon hum grows dominant.")
            else:
                print(f"The attack penetrates {opponent.name}'s systems, striking at MegaCorp's AI core. Neon City's resistance gains momentum, dealing {damage} damage as the city's neon hum grows defiant against the MegaCorp empire.")
        time.sleep(2)
        opponent.health -= damage
        if opponent.health <= 0:
            opponent.health = 0
            if self.character_type == "Nexus9":
                print(f"\n{opponent.name}'s circuits overload and fry, collapsing under MegaCorp's AI assault. Neon City's operatives fall silent, their resistance crushed as Nexus9 seizes the city's network.")
            else:
                print(f"\n{opponent.name}'s circuits overload and fry, collapsing MegaCorp's AI empire. Neon City's operatives rejoice, their digital freedom restored as Nexus9 loses its grip on the city's network.")
            time.sleep(2)

    def special_ability(self, opponent, damage):
        # Handle special abilities (no random outcomes)
        if not self.special_used:
            if self.character_type == "Nexus9":
                print(f"{self.name}'s crypto blast surges and provides Nexus9 with a critical boost in power. {opponent.name}'s efforts to gain critical access will need a full power attack to succeed. The attack deals {damage} damage, weakening the resistance and it's brave warriors.")
                time.sleep(1)
            else:
                print(f"{self.name} executes a critical override, targeting {opponent.name}'s MegaCorp mainframe with precision. The attack deals {damage} damage, weakening the empire's digital defenses as Neon City's resistance surges with renewed hope.")
                time.sleep(1)
            opponent.health -= damage
            self.special_used = True
        else:
            if self.character_type == "Nexus9":
                print(f"Luckily for the resistance, {self.name}'s crypto blast is offline, and the resistance is safe for now. The attack is ineffective, but the city remains in a state of digital warfare.")
            else:
                print(f"{self.name}'s override protocols are exhausted, their codes spent in Neon City's digital war. MegaCorp's fortified systems remain unbreached, and the overthrow of the resistance is imminent. The city's neon machines hum ominously.")
        time.sleep(2)
        if opponent.health <= 0:
            opponent.health = 0
            print(f"\n{opponent.name}'s circuits overload and fry, collapsing MegaCorp's AI empire. Neon City's operatives rejoice, their digital freedom restored as a deafening silence falls over the city.")
            time.sleep(2)

    def heal(self):
        # Random 5-25 health, capped at max_health
        heal_amount = random.randint(5, 25)
        if self.health + heal_amount > self.max_health:
            heal_amount = self.max_health - self.health
        self.health += heal_amount
        print(f"{self.name} taps into Neon City's hidden power grid, rerouting MegaCorp's stolen energy. System integrity restores by {heal_amount}, bolstering the operative's resolve as Neon City's resistance fights on. Health: {self.health}.")
        time.sleep(2)

    def display_stats(self):
        print(f"{self.name}'s diagnostics reveal: Health at {self.health}/{self.max_health}, Attack Power at {self.attack_power}, ready to challenge MegaCorp's tyranny in Neon City's battlegrid.")
        time.sleep(0.5)