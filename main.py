import random
import uuid


from logger import Logger
from player import Player
from enemy import enemies
from combat import Combat

logger = Logger()

game_number = logger.get_next_game_number()

game_id = str(uuid.uuid4())

# Create the player
player = Player()

# Main game loop
while player.health > 0
    # Choose a random enemy
    current_enemy = random.choice(enemies)

    # Start combat
    combat = Combat(player, current_enemy, game_id, game_number, logger)
    combat.combat()

print("\nGame Over!")
print(f"Final Score: {player.score}")
print(f"Encounters Completed: {player.encounter_number}")