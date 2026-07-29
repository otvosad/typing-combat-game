class Enemy:
    def __init__(self, name, damage, ):
        self.name = name
        self.damage = damage
        self.enemy_length = len(name)

Goblin = Enemy("Goblin",20)
Skeleton = Enemy("Skeleton",65)
Sniper = Enemy("Sniper", 28)
Tank = Enemy ("Tank", 15)
Dragon = Enemy("Dragon", 45)
Soldier = Enemy("Soldier", 38)
Rat = Enemy("Rat", 5)
Bat = Enemy("Bat", 5)
Imp = Enemy("Imp", 8)
Orc = Enemy("Orc", 10)
Wolf = Enemy("Wolf", 12)
Troll = Enemy("Troll", 18)
Archer = Enemy("Archer", 22)
Bandit = Enemy("Bandit", 25)
Raider = Enemy("Raider", 30)
Hunter = Enemy("Hunter", 32)
Pirate = Enemy("Pirate", 35)
Knight = Enemy("Knight", 40)
Wizard = Enemy("Wizard", 50)
Vampire = Enemy("Vampire", 55)
Reaper = Enemy("Reaper", 60)
Necromancer = Enemy("Necromancer", 70)
Spellcaster = Enemy("Spellcaster", 75)
Crossbowman = Enemy("Crossbowman", 80)


enemies = [
    Rat,
    Bat,
    Imp,
    Orc,
    Wolf,
    Tank,
    Troll,
    Goblin,
    Archer,
    Bandit,
    Sniper,
    Raider,
    Hunter,
    Pirate,
    Soldier,
    Knight,
    Dragon,
    Wizard,
    Vampire,
    Reaper,
    Necromancer,
    Spellcaster,
    Crossbowman
]