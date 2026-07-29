import difflib
import time
import msvcrt
from logger import Logger

class Combat:
    def __init__(self, player, enemy,game_id, game_number, logger):
        self.player = player
        self.enemy = enemy
        self.game_id = game_id
        self.logger = logger
        self.game_number = game_number


    def typing_attempt(self):

        typed_word = ""
        time_limit = 5

        print(f"\nEnemy: {self.enemy.name}")
        print(f"You have {time_limit} seconds to type the word.\n")

        start_time = time.time()

        while True:

            # Check timer
            elapsed_time = time.time() - start_time

            if elapsed_time >= time_limit:
                accuracy = self.calculate_accuracy(typed_word)

                print("\nTime's up!")
                print(f"Accuracy: {accuracy:.1f}%")

                return False, accuracy, elapsed_time, typed_word

            # Read keyboard
            if msvcrt.kbhit():

                key = msvcrt.getwche()

                # ENTER = submit
                if key == "\r":

                    elapsed_time = time.time() - start_time

                    accuracy = self.calculate_accuracy(typed_word)

                    success = (typed_word == self.enemy.name)

                    print(f"\nAccuracy: {accuracy:.1f}%")
                    print(f"Time: {elapsed_time:.2f} seconds")

                    return success, accuracy, elapsed_time, typed_word

                # BACKSPACE = remove last character
                elif key == "\b":

                    if len(typed_word) > 0:
                        typed_word = typed_word[:-1]

                        # Erase the character from the console
                        print("\b \b", end="", flush=True)

                # Normal character
                else:
                    typed_word += key


    def combat(self):

        while self.player.health > 0:

            success, accuracy, time_taken, typed_word = self.typing_attempt()
            self.logger.save_attempt(
                game_number=self.game_number,
                game_id=self.game_id,
                encounter=self.player.encounter_number,
                attempt=self.player.attempt_number,
                enemy=self.enemy.name,
                enemy_length=len(self.enemy.name),
                typed_word=typed_word,
                accuracy=accuracy,
                time_taken=time_taken,
                success=success,
                health=self.player.health
                )

            if success:
                print(f"\nYou defeated the {self.enemy.name}!")
                self.player.add_score()
                self.player.next_encounter()

                # We'll log these values to CSV later
                print(f"Typed: {typed_word}")
                print(f"Accuracy: {accuracy:.1f}%")
                print(f"Time: {time_taken:.2f}s")

                break

            print(f"\nThe {self.enemy.name} attacks!")

            self.enemy_attack()
            self.player.attempt_number += 1

            print(f"Player Health: {self.player.health}")

    def enemy_attack(self):
        print(f"\n{self.enemy.name} attacks!")

        self.player.take_damage(self.enemy.damage)

        print(f"You lose {self.enemy.damage} health.")
        print(f"Current Health: {self.player.health}")

    def log_attempt(self, success, accuracy, time_taken, typed_word):
        print("\n----- Attempt Summary -----")
        print(f"Enemy: {self.enemy.name}")
        print(f"Typed Word: {typed_word}")
        print(f"Success: {success}")
        print(f"Accuracy: {accuracy:.1f}%")
        print(f"Time Taken: {time_taken:.2f} seconds")
        print(f"Player Health: {self.player.health}")
        print("---------------------------\n")

    def calculate_accuracy(self, typed_word):

        correct_letters = 0

        for typed, actual in zip(typed_word, self.enemy.name):
            if typed == actual:
                correct_letters += 1

        accuracy = (correct_letters / len(self.enemy.name)) * 100

        return round(accuracy, 2)
