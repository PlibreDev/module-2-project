import random

# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  # Max health for healing cap
        self.evade = False  # For Archer's dodge
        self.shield = False  # For Paladin's shield

    def attack(self, opponent): 
        # Random damage within ±5 of base attack power
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        # Check for evade or shield
        if opponent.evade:
            print(f"{opponent.name} nimbly dodges while sticking out their tongue!")
            opponent.evade = False
        elif opponent.shield:
            print(f"{opponent.name}'s shiny shield says 'Nope!' to the attack!")
            opponent.shield = False
        else:
            opponent.health -= damage
            print(f"{self.name} whacks {opponent.name} for {damage} damage! Ouch!")
        if opponent.health <= 0:
            opponent.health = 0
            print(f"{opponent.name} flops dramatically to the ground, defeated!")

    def heal(self):
        # Heal 20 health, don't go over max
        heal_amount = 20
        if self.health + heal_amount > self.max_health:
            heal_amount = self.max_health - self.health
        self.health += heal_amount
        print(f"{self.name} chugs a health potion for {heal_amount} health! Feeling spry!")

    def display_stats(self):
        print(f"{self.name}'s Vibe Check - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

# Warrior class
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)

    def power_attack(self, opponent):
        # Big hit with 1.5x damage
        damage = int(self.attack_power * 1.5)
        opponent.health -= damage
        print(f"{self.name} swings a mighty Power Attack, dealing {damage} damage to {opponent.name}!")
        if opponent.health <= 0:
            opponent.health = 0
            print(f"{opponent.name} is toast!")
    
    def battle_cry(self):
        # Boost attack power
        self.attack_power += 5
        print(f"{self.name} roars a Battle Cry, scaring nearby squirrels! Attack power now {self.attack_power}!")

# Mage class
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

    def cast_spell(self, opponent):
        # High damage, might miss
        if random.random() < 0.8:  # 80% hit chance
            damage = 50
            opponent.health -= damage
            print(f"{self.name} hurls a sparkly Fireball at {opponent.name} for {damage} damage! Boom!")
            if opponent.health <= 0:
                opponent.health = 0
                print(f"{opponent.name} is a crispy critter!")
        else:
            print(f"{self.name}'s Fireball fizzles out! Embarrassing...")

    def mana_surge(self):
        # Heal a bit, boost attack
        self.health = min(self.health + 10, self.max_health)
        self.attack_power += 10
        print(f"{self.name} glows with Mana Surge, healing 10 health and boosting attack to {self.attack_power}! Magic vibes!")

# Archer class
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=90, attack_power=30)

    def quick_shot(self, opponent):
        # Two fast shots
        for _ in range(2):
            if opponent.health > 0:
                damage = random.randint(10, 15)
                opponent.health -= damage
                print(f"{self.name} fires a Quick Shot at {opponent.name} for {damage} damage! Pew pew!")
        if opponent.health <= 0:
            opponent.health = 0
            print(f"{opponent.name} looks like a pincushion! Defeated!")

    def evade(self):
        # Dodge next attack
        self.evade = True
        print(f"{self.name} does a fancy roll to Evade! Tripped a bit, but it worked!")

# Paladin class
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=160, attack_power=20)

    def holy_strike(self, opponent):
        # Bonus damage
        damage = self.attack_power + 15
        opponent.health -= damage
        print(f"{self.name} smites {opponent.name} with Holy Strike for {damage} damage! Divine justice!")
        if opponent.health <= 0:
            opponent.health = 0
            print(f"{opponent.name} regrets their life choices! Defeated!")

    def divine_shield(self):
        # Block next attack
        self.shield = True
        print(f"{self.name} raises a Divine Shield, sparkling like a disco ball!")

# EvilWizard class
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        self.health += 5
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} cackles and regenerates 5 health! Current health: {self.health}")

    def attack(self, opponent):
        # Wizard's attack with flair
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        if opponent.evade:
            print(f"{opponent.name} nimbly dodges while sticking out their tongue!")
            opponent.evade = False
        elif opponent.shield:
            print(f"{opponent.name}'s shiny shield says 'Nope!' to the attack!")
            opponent.shield = False
        else:
            opponent.health -= damage
            print(f"{self.name} tosses a sparkly fireball at {opponent.name} for {damage} damage! Muahaha!")
        if opponent.health <= 0:
            opponent.health = 0
            print(f"{opponent.name} flops dramatically to the ground, defeated!")

# Create player character
def create_character():
    print("Pick your hero, you brave (or slightly confused) adventurer!")
    print("1. Warrior - Beefy and shouty")
    print("2. Mage - Throws sparkly stuff")
    print("3. Archer - Pew pew from afar")
    print("4. Paladin - Shiny and smite-y")
    
    class_choice = input("Enter the number of your class choice: ")
    name = input("What's your hero's name? No pressure, just their legacy: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Uh-oh, bad choice! Here's a Warrior to save the day.")
        return Warrior(name)

# Battle function
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn, Hero! ---")
        print("1. Attack - Smack that wizard!")
        print("2. Use Special Ability - Do something cool!")
        print("3. Heal - Chug a potion!")
        print("4. View Stats - Check your awesomeness!")
        
        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            # Special abilities by class
            if isinstance(player, Warrior):
                ability_choice = input("Pick: 1. Power Attack  2. Battle Cry: ")
                if ability_choice == '1':
                    player.power_attack(wizard)
                elif ability_choice == '2':
                    player.battle_cry()
                else:
                    print("Oops, wrong move! Try again.")
            elif isinstance(player, Mage):
                ability_choice = input("Pick: 1. Cast Spell  2. Mana Surge: ")
                if ability_choice == '1':
                    player.cast_spell(wizard)
                elif ability_choice == '2':
                    player.mana_surge()
                else:
                    print("Spell misfired! Pick again.")
            elif isinstance(player, Archer):
                ability_choice = input("Pick: 1. Quick Shot  2. Evade: ")
                if ability_choice == '1':
                    player.quick_shot(wizard)
                elif ability_choice == '2':
                    player.evade()
                else:
                    print("Arrow missed the mark! Try again.")
            elif isinstance(player, Paladin):
                ability_choice = input("Pick: 1. Holy Strike  2. Divine Shield: ")
                if ability_choice == '1':
                    player.holy_strike(wizard)
                elif ability_choice == '2':
                    player.divine_shield()
                else:
                    print("Shield dropped! Pick again.")
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice, hero! Focus up!")
            continue

        # Wizard's turn
        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"Oh no! {player.name} was zapped by {wizard.name}! Better luck next time!")
            break

    if wizard.health <= 0:
        print(f"BOOM! {player.name} sent {wizard.name} to wizard detention! You win!")

# Main game function
def main():
    print("Welcome to Defeat the Evil Wizard! Prepare for epic shenanigans!")
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    print(f"\n{player.name} squares up against {wizard.name}, who’s twirling his mustache menacingly!")
    battle(player, wizard)

if __name__ == "__main__":
    main()