import random
import time

# Base Character class can be found in character_module
# CyberBruiser class
from character_module.cyberbruiser import CyberBruiser
# Codebreaker class
from character_module.codebreaker import CodeBreaker
# DroneSpecialist class
from character_module.dronespecialist import DroneSpecialist
# SystemAdmin class
from character_module.systemadmin import SystemAdmin
# Nexus9 class
from character_module.nexus9 import Nexus9
# Create player character
from character_module.character_creation import create_character

# Battle function
from game_logic.game_logic import battle

# Program execution
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