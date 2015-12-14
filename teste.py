from lib import game_class

rpg = game_class.Game("rpg", ["roll", "reroll", "next"])

print rpg.name
print rpg.game_arguments
