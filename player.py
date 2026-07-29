class Player:
    def __init__(self):
        self.health = 100
        self.score = 0
        self.encounter_number = 1
        self.attempt_number = 1

    def take_damage(self, damage):
        self.health -= damage

    def add_score(self):
        self.score += 1

    def next_encounter(self):
        self.encounter_number += 1
        self.attempt_number = 1