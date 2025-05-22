import random

# Base Character class
class Character:
    def __init__(self, name, health, attack_power, character_type):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.character_type = character_type
        self.max_health = health
        self.special_used = False  # Track special ability usage

    def attack(self, opponent, damage):
        # Handle primary and secondary attacks with random outcomes
        outcome = random.random()
        if outcome < 0.2:  # 20% total chance
            if outcome < 0.05:  # 5% evade
                print(f"{opponent.name} evades the attack with a system reroute.")
                return
            elif outcome < 0.1:  # 5% smash
                damage = int(damage * 1.5)
                print(f"{self.name} lands a smashing blow on {opponent.name} for {damage} damage.")
            elif outcome < 0.15:  # 5% hack
                damage += 10
                print(f"{self.name} hacks {opponent.name}'s systems for {damage} damage.")
            else:  # 5% invalid_password
                damage = damage // 2
                print(f"{opponent.name}'s invalid password reduces damage to {damage}.")
        else:
            print(f"{self.name} strikes {opponent.name} for {damage} damage.")
        opponent.health -= damage
        if opponent.health <= 0:
            opponent.health = 0
            print(f"{opponent.name} has been shut down. System secure.")

    def special_ability(self, opponent, damage):
        # Handle special abilities (no random outcomes)
        if not self.special_used:
            print(f"{self.name} executes a special ability on {opponent.name} for {damage} damage.")
            opponent.health -= damage
            self.special_used = True
        else:
            print(f"{self.name}'s special ability is offline. No effect.")
        if opponent.health <= 0:
            opponent.health = 0
            print(f"{opponent.name} has been shut down. System secure.")

    def heal(self):
        # Random 5-25 health, capped at max_health
        heal_amount = random.randint(5, 25)
        if self.health + heal_amount > self.max_health:
            heal_amount = self.max_health - self.health
        self.health += heal_amount
        print(f"{self.name} restores {heal_amount} system integrity. Current health: {self.health}.")

    def display_stats(self):
        print(f"{self.name}'s Diagnostics - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

# CyberBruiser class
class CyberBruiser(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25, character_type="CyberBruiser")

    def circuit_strike(self, opponent):
        # Primary attack: random 20-30 damage
        damage = random.randint(20, 30)
        super().attack(opponent, damage)

    def overclock_smash(self, opponent):
        # Secondary attack: random 15-20 damage
        damage = random.randint(15, 20)
        super().attack(opponent, damage)

    def system_breach(self, opponent):
        # Special ability: double random primary damage (40-60)
        if not self.special_used:
            damage = random.randint(20, 30) * 2
            super().special_ability(opponent, damage)
        else:
            print(f"{self.name}'s systems are offline. System Breach already used.")

# Codebreaker class
class Codebreaker(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35, character_type="Codebreaker")

    def code_injection(self, opponent):
        # Primary attack: random 30-40 damage
        damage = random.randint(30, 40)
        super().attack(opponent, damage)

    def malware_shot(self, opponent):
        # Secondary attack: fixed 30 damage
        damage = 30
        super().attack(opponent, damage)

    def data_corrupt(self, opponent):
        # Special ability: double random primary damage (60-80)
        if not self.special_used:
            damage = random.randint(30, 40) * 2
            super().special_ability(opponent, damage)
        else:
            print(f"{self.name}'s code is exhausted. Data Corrupt already used.")

# DroneSpecialist class
class DroneSpecialist(Character):
    def __init__(self, name):
        super().__init__(name, health=90, attack_power=30, character_type="DroneSpecialist")

    def drone_strike(self, opponent):
        # Primary attack: random 25-35 damage
        damage = random.randint(25, 35)
        super().attack(opponent, damage)

    def quick_drone(self, opponent):
        # Secondary attack: two shots, random 10-15 damage each
        for _ in range(2):
            if opponent.health > 0:
                damage = random.randint(10, 15)
                super().attack(opponent, damage)
                if opponent.health <= 0:
                    break

    def drone_swarm(self, opponent):
        # Special ability: double random primary damage (50-70)
        if not self.special_used:
            damage = random.randint(25, 35) * 2
            super().special_ability(opponent, damage)
        else:
            print(f"{self.name}'s drones are offline. Drone Swarm already used.")

# SystemAdmin class
class SystemAdmin(Character):
    def __init__(self, name):
        super().__init__(name, health=160, attack_power=20, character_type="SystemAdmin")

    def security_patch(self, opponent):
        # Primary attack: random 15-25 damage
        damage = random.randint(15, 25)
        super().attack(opponent, damage)

    def crypto_strike(self, opponent):
        # Secondary attack: random 20-30 damage
        damage = random.randint(20, 30)
        super().attack(opponent, damage)

    def lockout(self, opponent):
        # Special ability: double random primary damage (30-50)
        if not self.special_used:
            damage = random.randint(15, 25) * 2
            super().special_ability(opponent, damage)
        else:
            print(f"{self.name}'s protocols are offline. Lockout already used.")

# Nexus9 class
class Nexus9(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15, character_type="Nexus9")

    def data_surge(self, opponent):
        # Primary attack: random 10-20 damage
        damage = random.randint(10, 20)
        super().attack(opponent, damage)

    def packet_spike(self, opponent):
        # Secondary attack: random 5-15 damage
        damage = random.randint(5, 15)
        super().attack(opponent, damage)

    def crypto_blast(self, opponent):
        # Special ability: double random primary damage (20-40)
        if not self.special_used:
            damage = random.randint(10, 20) * 2
            super().special_ability(opponent, damage)
        else:
            print(f"{self.name}'s systems are offline. Crypto Blast already used.")

# Create player character
def create_character():
    print("Select a cyber-operative to neutralize Nexus9:")
    print("1. CyberBruiser - High-damage melee specialist")
    print("2. Codebreaker - Precision hacker")
    print("3. DroneSpecialist - Drone-based combatant")
    print("4. SystemAdmin - Defensive system expert")
    
    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your operative's codename: ")

    if class_choice == '1':
        return CyberBruiser(name)
    elif class_choice == '2':
        return Codebreaker(name)
    elif class_choice == '3':
        return DroneSpecialist(name)
    elif class_choice == '4':
        return SystemAdmin(name)
    else:
        print("Invalid selection. Assigning CyberBruiser.")
        return CyberBruiser(name)

# Battle function
def battle(player, opponent):
    while opponent.health > 0 and player.health > 0:
        print("\n--- Operative's Turn ---")
        if isinstance(player, CyberBruiser):
            print("1. Circuit Strike")
            print("2. Overclock Smash")
            print("3. System Breach (one-time use)")
        elif isinstance(player, Codebreaker):
            print("1. Code Injection")
            print("2. Malware Shot")
            print("3. Data Corrupt (one-time use)")
        elif isinstance(player, DroneSpecialist):
            print("1. Drone Strike")
            print("2. Quick Drone")
            print("3. Drone Swarm (one-time use)")
        elif isinstance(player, SystemAdmin):
            print("1. Security Patch")
            print("2. Crypto Strike")
            print("3. Lockout (one-time use)")
        print("4. Heal - Restore system integrity")
        print("5. View Stats - System diagnostics")
        
        choice = input("Select an action: ")

        if choice == '1':
            if isinstance(player, CyberBruiser):
                player.circuit_strike(opponent)
            elif isinstance(player, Codebreaker):
                player.code_injection(opponent)
            elif isinstance(player, DroneSpecialist):
                player.drone_strike(opponent)
            elif isinstance(player, SystemAdmin):
                player.security_patch(opponent)
        elif choice == '2':
            if isinstance(player, CyberBruiser):
                player.overclock_smash(opponent)
            elif isinstance(player, Codebreaker):
                player.malware_shot(opponent)
            elif isinstance(player, DroneSpecialist):
                player.quick_drone(opponent)
            elif isinstance(player, SystemAdmin):
                player.crypto_strike(opponent)
        elif choice == '3':
            if isinstance(player, CyberBruiser):
                player.system_breach(opponent)
            elif isinstance(player, Codebreaker):
                player.data_corrupt(opponent)
            elif isinstance(player, DroneSpecialist):
                player.drone_swarm(opponent)
            elif isinstance(player, SystemAdmin):
                player.lockout(opponent)
        elif choice == '4':
            player.heal()
        elif choice == '5':
            player.display_stats()
            continue  # Reload menu after stats
        else:
            print("Invalid selection. Nexus9 gains processing power.")
            continue

        # Nexus9's turn
        if opponent.health > 0:
            move = random.random()
            if opponent.special_used:
                if move < 0.48:  # 48% primary
                    opponent.data_surge(player)
                elif move < 0.84:  # 36% secondary
                    opponent.packet_spike(player)
                else:  # 16% heal
                    opponent.heal()
            else:
                if move < 0.4:  # 40% primary
                    opponent.data_surge(player)
                elif move < 0.7:  # 30% secondary
                    opponent.packet_spike(player)
                elif move < 0.9:  # 20% special
                    opponent.crypto_blast(player)
                else:  # 10% heal
                    opponent.heal()

        if player.health <= 0:
            print(f"System Failure: {player.name} was neutralized by {opponent.name}. Nexus9 controls the network.")
            break

    if opponent.health <= 0:
        print(f"Victory: {player.name} terminated {opponent.name}. Network secure.")

# Main game function
def main():
    print("Rogue AI Uprising: Neutralize Nexus9 to secure the network.")
    player = create_character()
    opponent = Nexus9("Nexus9")
    print(f"\n{player.name} engages {opponent.name} in a critical system showdown.")
    battle(player, opponent)

if __name__ == "__main__":
    main()