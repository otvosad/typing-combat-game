from database import engine
from sqlalchemy import text

class Logger:
    def __init__(self):
        self.filename = "game_data.csv"

    def save_attempt(
            self,
            game_number,
            game_id,
            encounter,
            attempt,
            enemy,
            enemy_length,
            typed_word,
            accuracy,
            time_taken,
            success,
            health,
    ):

        accuracy = round(accuracy, 2)
        time_taken = round(time_taken, 2)

        with engine.begin() as connection:
            connection.execute(
                text("""
                    INSERT INTO game_attempts
                    (
                        game_number,
                        game_id,
                        encounter,
                        attempt,
                        enemy,
                        enemy_length,
                        typed_word,
                        accuracy,
                        time_taken,
                        success,
                        health
                    )
                    VALUES
                    (
                        :game_number,
                        :game_id,
                        :encounter,
                        :attempt,
                        :enemy,
                        :enemy_length,
                        :typed_word,
                        :accuracy,
                        :time_taken,
                        :success,
                        :health
                    )
                """),
                {
                    "game_number": game_number,
                    "game_id": game_id,
                    "encounter": encounter,
                    "attempt": attempt,
                    "enemy": enemy,
                    "enemy_length": enemy_length,
                    "typed_word": typed_word,
                    "accuracy": accuracy,
                    "time_taken": time_taken,
                    "success": success,
                    "health": health,
                }
            )

    def get_next_game_number(self):
        with engine.connect() as connection:
            result = connection.execute(
                text("SELECT COALESCE(MAX(game_number), 0) FROM game_attempts")
            )

            return result.scalar() + 1