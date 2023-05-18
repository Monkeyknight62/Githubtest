import random
from time import sleep


class Player:
    def __init__(self, name):
        # Represents a player in the game.#

        self.name = name
        self.health = 200
        self.level = 1
        self.experience = 0
        self.power_up_sword = False
        self.power_up_shield = False


class Enemy:
    def __init__(self, name, health, attack):
        # Represents an enemy in the game.#

        self.name = name
        self.health = health
        self.attack = attack


class Puzzle:
    def __init__(self, question, answer):
        # Represents a puzzle in the game.#

        self.question = question
        self.answer = answer


class Room:
    def __init__(self, description, puzzle=None, enemy=None, power_up=None):
        # Represents a room in the game.#

        self.description = description
        self.puzzle = puzzle
        self.enemy = enemy
        self.power_up = power_up


def generate_enemy():
    # Generates a random enemy from a list of predefined enemies.#

    enemies = [
        Enemy("Goblin", 50, 10),
        Enemy("Orc", 75, 15),
        Enemy("Dragon", 100, 20),
        Enemy("Troll", 80, 12)
    ]
    return random.choice(enemies)


def generate_puzzle():
    # Generates a random puzzle from a list of predefined puzzles.#

    puzzles = [
        Puzzle("Solve for x '4(x + 3) = 5x - 6'", "x = 18"),
        Puzzle("Solve for x '3x + 7 = 22'", "x = 5"),
        Puzzle("What is the square root of 144?", "12"),
        Puzzle("Evaluate 3^4", "81"),
        Puzzle("Solve for x '2x + 5 = 17'", "x = 6"),
    ]
    return random.choice(puzzles)


def generate_power_up():
    # Generates a random power-up from a list of predefined power-ups.#

    power_ups = ["Power-Up Sword", "Power-Up Shield"]
    return random.choice(power_ups)


def start_game():
    # Starts the game and handles the gameplay loop.#

    print("Welcome to Mystic Quest: The Realm of Enigma!")
    name = input("Enter your name: ")
    player = Player(name)
    print(f"Welcome, {player.name}! Let the adventure begin!")

    current_room = 1
    while True:
        print("--------------")
        print(f"Current Room: {current_room}")
        print("--------------")

        room = get_room(current_room)
        print(room.description)

        if room.puzzle:
            solve_puzzle(player, room.puzzle)

        if room.enemy:
            battle_enemy(player, room.enemy)

        if room.power_up:
            collect_power_up(player, room.power_up)

        if current_room == 7:
            print("Congratulations! You have completed the Mystic Quest!")
            break

        current_room += 1


def get_room(room_number):
    # Returns the room corresponding to the given room number.#

    rooms = {
        1: Room("You enter a dark cave. You see a faint light at the end.", generate_puzzle()),
        2: Room("You find yourself in a lush forest. Birds are chirping.", generate_puzzle()),
        3: Room("You come across a raging river. There is a bridge ahead.", None, generate_enemy()),
        4: Room("You climb a steep mountain. The air is thin.", generate_puzzle(), generate_enemy()),
        5: Room("You reach a mysterious underground chamber. The walls are covered in ancient runes.",
                generate_puzzle(), generate_enemy()),
        6: Room("You enter a haunted castle. Shadows lurk in every corner.", generate_puzzle(), generate_enemy()),
        7: Room("You reach the legendary Temple of Enigma. The final challenge awaits.")
    }
    return rooms.get(room_number)


def solve_puzzle(player, puzzle):
    # Handles the puzzle-solving gameplay.#

    print("A puzzle lies before you. Solve it to proceed!")
    print(puzzle.question)
    answer = input("Your answer: ")
    if answer.lower() == puzzle.answer.lower():
        print("Congratulations! You solved the puzzle.")
        player.experience += 20
    else:
        print("Oops! That's incorrect.")


def battle_enemy(player, enemy):
    # Handles the enemy battle gameplay.#

    sleep(1)
    print(f"You encounter a fearsome {enemy.name}! Prepare for battle.")

    if player.power_up_sword:
        player_attack = random.randint(15, 30)
        player.health += 20  # Increase the player's health by 50 when using power-up sword
        print("You strike with your power-up sword!")
    else:
        player_attack = random.randint(5, 20)

    if player.power_up_shield:
        enemy_attack = random.randint(0, 5)
        enemy_attack -= 5  # Reduce the enemy's attack by 5 when the player has the power-up shield
        print("Your power-up shield blocks some of the enemy's attack!")
    else:
        enemy_attack = random.randint(5, 15)

    while player.health > 0 and enemy.health > 0:
        sleep(1)
        print(f"{player.name}: {player.health} HP\t{enemy.name}: {enemy.health} HP")
        player.health -= enemy_attack
        enemy.health -= player_attack

    if player.health <= 0:
        print("Game Over! You were defeated in battle.")
        exit()
    else:
        print(f"Victory! You defeated the {enemy.name}.")
        player.experience += 50
        if not player.power_up_shield:
            print("The enemy drops a power-up shield. You pick it up!")
            player.power_up_shield = True
        if not player.power_up_sword:
            print("The enemy drops a power-up sword. You pick it up!")
            player.power_up_sword = True


def collect_power_up(player, power_up):
    # Handles the power-up collection gameplay.#

    print(f"You found a {power_up}! It will aid you in your journey.")
    if power_up == "Power-Up Sword":
        player.power_up_sword = True
        player.health += 20  # Increase the player's health by 50#
    elif power_up == "Power-Up Shield":
        player.power_up_shield = True
        player.health += 20  # Increase the player's health by 50#


start_game()
