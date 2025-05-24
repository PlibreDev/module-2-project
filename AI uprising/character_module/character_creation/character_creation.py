from ..cyberbruiser import CyberBruiser
from ..codebreaker import CodeBreaker
from ..dronespecialist import DroneSpecialist
from ..systemadmin import SystemAdmin
import time

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
        return CodeBreaker(name)
    elif class_choice == '3':
        return DroneSpecialist(name)
    elif class_choice == '4':
        return SystemAdmin(name)
    else:
        print("Invalid selection. The city's resistance calls for CyberBruiser to lead the fight.")
        time.sleep(0.5)
        print()
        return CyberBruiser(name)