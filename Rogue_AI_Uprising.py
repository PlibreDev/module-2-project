import random
import time

# Base Character class
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

# CyberBruiser class
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

# Codebreaker class
class Codebreaker(Character):
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

# DroneSpecialist class
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

# SystemAdmin class
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

# Nexus9 class
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

# Create player character
def create_character():
    print("\nSelect a cyber-operative to dismantle Nexus9 and eliminate the threat of MegaCorp's rogue AI empire in Neon City:\n")
    print("1. CyberBruiser - Smashes servers with unrelenting force")
    print("2. Codebreaker - Hacks systems with surgical precision")
    print("3. DroneSpecialist - Commands drones to swarm the enemy")
    print("4. SystemAdmin - Fortifies defenses with unbreakable patches")
    time.sleep(0.5)
    
    try:
        print()
        class_choice = input("Enter the number of your class choice: ")
        print()
        name = input("Enter your operative's codename: ")
        print("\n" * 5)
    except EOFError:
        print("Input interrupted. Assigning default CyberBruiser operative.")
        time.sleep(0.5)
        print()
        return CyberBruiser("DefaultOperative")
    
    print()
    if class_choice == '1':
        return CyberBruiser(name)
    elif class_choice == '2':
        return Codebreaker(name)
    elif class_choice == '3':
        return DroneSpecialist(name)
    elif class_choice == '4':
        return SystemAdmin(name)
    else:
        print("Invalid selection. The city's resistance calls for CyberBruiser to lead the fight.")
        time.sleep(0.5)
        print()
        return CyberBruiser(name)

# Battle function
def battle(player, opponent):
    while opponent.health > 0 and player.health > 0:
        print("\n--- Operative's Turn ---")
        time.sleep(0.5)
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
        print("6. Quit - Abandon mission")
        time.sleep(0.5)
        print()
        
        choice = input("Select an action: ")
        print()

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
            print()
        elif choice == '5':
            player.display_stats()
            print()
            continue
        elif choice == '6':
            print(f"{player.name} retreats from Neon City's digital battleground, abandoning the fight. Nexus9 will continue its plan to enslave the city.\n")
            time.sleep(2)
            break
        else:
            print("Invalid selection. Neon City needs a hero to lead the resistance.")
            time.sleep(0.5)
            print()
            continue

        # Nexus9's turn
        if opponent.health > 0:
            print(f"\n--- {opponent.name}'s Turn ---")
            time.sleep(0.5)
            move = random.random()
            if opponent.special_used:
                if move < 0.48:  # 48% primary
                    opponent.data_surge(player)
                elif move < 0.84:  # 36% secondary
                    opponent.packet_spike(player)
                else:  # 16% heal
                    opponent.heal()
                    print()
            else:
                if move < 0.4:  # 40% primary
                    opponent.data_surge(player)
                elif move < 0.7:  # 30% secondary
                    opponent.packet_spike(player)
                elif move < 0.9:  # 20% special
                    opponent.crypto_blast(player)
                else:  # 10% heal
                    opponent.heal()
                    print()
            print(f"{opponent.name} Status: Health at {opponent.health}/{opponent.max_health}")
            time.sleep(0.5)
            print()

        if player.health <= 0:
            print(f"System Failure: {player.name} succumbs to {opponent.name}'s relentless onslaught. Another hero must lead the resistance now.")
            time.sleep(2)
            break

    if opponent.health <= 0:
        print(f"Victory: {player.name} obliterates {opponent.name}, freeing Neon City from MegaCorp's AI tyranny. The machines fall silent, and the streets of Neon City glow with a new light.")
        time.sleep(2)

# Main game function
def main():
    print("\n" * 10)
    print("Rogue AI Uprising: Infiltrate MegaCorp's servers to halt Nexus9's plan to enslave Neon City, and then globalize it's power.")
    time.sleep(1)
    print()
    player = create_character()
    opponent = Nexus9("Nexus9")
    print(f"{player.name} ventures into Neon City's newfound war zone, facing {opponent.name} to end it's reign of terror.")
    time.sleep(1)
    print()
    battle(player, opponent)

if __name__ == "__main__":
    main()