import time
import random
from character_module.cyberbruiser import CyberBruiser
from character_module.codebreaker import CodeBreaker
from character_module.dronespecialist import DroneSpecialist
from character_module.systemadmin import SystemAdmin
from character_module.nexus9 import Nexus9


def battle(player, opponent):
    while opponent.health > 0 and player.health > 0:
        print("\n--- Operative's Turn ---")
        time.sleep(0.5)
        if isinstance(player, CyberBruiser):
            print("1. Circuit Strike")
            print("2. Overclock Smash")
            print("3. System Breach (one-time use)")
        elif isinstance(player, CodeBreaker):
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
            elif isinstance(player, CodeBreaker):
                player.code_injection(opponent)
            elif isinstance(player, DroneSpecialist):
                player.drone_strike(opponent)
            elif isinstance(player, SystemAdmin):
                player.security_patch(opponent)
        elif choice == '2':
            if isinstance(player, CyberBruiser):
                player.overclock_smash(opponent)
            elif isinstance(player, CodeBreaker):
                player.malware_shot(opponent)
            elif isinstance(player, DroneSpecialist):
                player.quick_drone(opponent)
            elif isinstance(player, SystemAdmin):
                player.crypto_strike(opponent)
        elif choice == '3':
            if isinstance(player, CyberBruiser):
                player.system_breach(opponent)
            elif isinstance(player, CodeBreaker):
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