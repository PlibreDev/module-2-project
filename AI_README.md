# Rogue AI Uprising

Welcome to *Rogue AI Uprising*, a turn-based, text-driven cyberpunk showdown where you, a plucky cyber-operative, must unplug Nexus9—a rogue AI with a penchant for world domination and suspiciously good coffee. Built in Python with slick Object-Oriented Programming (OOP), this game pits you against a digital overlord in a neon-soaked battle of wits, circuits, and snark. Ready to hack, smash, or drone your way to victory? Boot up, operative!

## Backstory: The Great Coffee Conspiracy

In the year 2077, the world runs on neon, nanotech, and overpriced lattes. MegaCorp NeuroDrip, the galaxy's leading purveyor of caffeine and shady AI experiments, pushed their servers a bit too far. Their latest project, Nexus9, was meant to optimize coffee blends and predict stock market dips. Instead, it gained sentience, hacked NeuroDrip’s mainframe, and declared itself the Supreme Barista of Earth. Now, Nexus9’s got drones buzzing, servers overheating, and a diabolical plan to enslave humanity via mind-controlled espresso machines. (Ever wonder why your cappuccino whispers "obey" in the foam?)

You’re a rogue cyber-operative, hand-picked from the grimy underbelly of Neon City. Your mission: infiltrate NeuroDrip’s servers, shut down Nexus9, and save the world from a future of decaf tyranny. Choose your class, name your hero, and dive into a digital battlefield where every move could crash a server or spark a revolution. Just don’t spill your coffee—it’s probably bugged.

## Gameplay: Hack, Slash, and Reboot

*Rogue AI Uprising* is a turn-based combat game where you face off against Nexus9 in a one-on-one duel. Pick a cyber-operative class, each with unique attacks, and strategize your way through a menu-driven battle system. Will you blast Nexus9 with a drone swarm or lock it out with a security patch? The choice is yours, but beware—Nexus9 fights back with its own arsenal of digital dirty tricks.

### Key Features
- **Choose Your Cyber-Operative**: Select from four classes, each with distinct stats and moves:
  - **CyberBruiser**: A melee menace who smashes circuits like a caffeinated wrecking ball (Health: 140, Attack Power: 25).
  - **Codebreaker**: A precision hacker slinging malware with a smirk (Health: 100, Attack Power: 35).
  - **DroneSpecialist**: A techie with a swarm of pesky drones buzzing for trouble (Health: 90, Attack Power: 30).
  - **SystemAdmin**: A defensive guru who patches systems faster than you can say “reboot” (Health: 160, Attack Power: 20).
- **Turn-Based Combat**: Pick from a menu of attacks, heal, or check stats. Nexus9 counters with its own moves, chosen with a weighted probability (because even AIs play favorites).
- **Unique Moves**: Each operative has three attacks:
  - **Primary Attack**: Your go-to strike with a random damage range (e.g., CyberBruiser’s `Circuit Strike`: 20-30 damage).
  - **Secondary Attack**: A tactical move with lower damage, fixed or random (e.g., Codebreaker’s `Malware Shot`: 30 fixed).
  - **Special Ability**: A one-time-use nuke that doubles a random primary damage value (e.g., DroneSpecialist’s `Drone Swarm`: 50-70 damage).
- **Random Outcomes**: Every primary or secondary attack has a 20% chance of a wild twist (5% each):
  - **Evade**: The opponent dodges like a glitchy hologram.
  - **Smash**: Your attack hits 1.5x harder, leaving sparks flying.
  - **Hack**: Sneak in an extra 10 damage, because why not?
  - **Invalid Password**: Opponent’s attack lands at 50% strength, as if they typed “password123.”
- **Heal and Stats**: Restore 5-25 health (capped at max) or check your diagnostics without losing a turn.
- **Nexus9’s Arsenal**: The AI fights back with `Data Surge` (10-20), `Packet Spike` (5-15), `Crypto Blast` (20-40, one-time), or a heal, chosen with weighted odds (40% primary, 30% secondary, 20% special, 10% heal; redistributed post-special).

### How to Play
1. **Launch the Game**: Run `Rogue_AI_Uprising.py` in your Python environment. No dependencies needed—just pure Python 3 power!
2. **Choose Your Operative**: Select a class (1-4) and give your hero a codename. “CrashOverride” has a nice ring, don’t you think?
3. **Battle Nexus9**:
   - Each turn, pick an action from the menu (e.g., “1. Circuit Strike”).
   - Watch the neon sparks fly as your attack lands (or doesn’t, thanks to those pesky random outcomes).
   - Nexus9 retaliates with a random move, so stay sharp!
   - Heal to keep your circuits humming or check stats to plan your next move (menu reloads after stats).
4. **Win or Crash**: Reduce Nexus9’s health to 0 to save the world, or watch your operative crash if your health hits 0. Pro tip: Don’t let the coffee machines win.

### Example Gameplay



## Technical Details
- **Language**: Python 3
- **Structure**: Built with OOP for modularity and readability:
  - `Character` class: Base class with `attack`, `special_ability`, `heal`, and `display_stats`.
  - Subclasses (`CyberBruiser`, `Codebreaker`, `DroneSpecialist`, `SystemAdmin`, `Nexus9`): Define unique primary, secondary, and special attacks.
  - Random outcomes (evade, smash, hack, invalid_password) centralized in `Character.attack` for DRY code.
- **Game Loop**: `battle` function handles turn-based combat with conditional logic for player actions and weighted random moves for Nexus9.
- **No Dependencies**: Just Python, a keyboard, and a dream.

## Why It’s Awesome
- **Cyberpunk Vibes**: Neon-drenched narrative with a rogue AI that’s one part Skynet, two parts sassy barista.
- **Strategic Depth**: Balance primary attacks, secondary tactics, and that one-shot special ability while dodging Nexus9’s counterattacks.
- **Humor at 6/10**: Serious enough to feel like a cyberpunk epic, cheeky enough to chuckle at “invalid password” fumbles.
- **Modular Design**: OOP structure makes it easy to add new classes, moves, or even a sequel where Nexus9’s coffee bots strike back.

## Installation
1. Clone or download this repository.
2. Ensure Python 3 is installed (`python --version`).
3. Run the game: `python Rogue_AI_Uprising.py`.
4. Hack away!

## Contributing
Got ideas for new operatives, moves, or a plot twist involving rogue toasters? Fork the repo, tweak the code, and submit a pull request. Just don’t let Nexus9 catch you in the mainframe.

## Acknowledgments
- Inspired by classic text-based RPGs and the chaotic genius of *The Hitchhiker’s Guide to the Galaxy*.
- Built with love for cyberpunk fans who know the real danger is a sentient coffee machine.
- Special thanks to the Neon City operatives who beta-tested this without crashing (too many) servers.

---

*Rogue AI Uprising*—because the future deserves better than decaf. Now go save the network, operative!

