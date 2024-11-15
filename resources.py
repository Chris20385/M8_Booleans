# Cristian Garcia
# 11/12/24

# This program shows you the weaponds and weaknesses of a character


class character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses

def get_model(self):
    return self.nickname

def get_year(self):
    return self.weapons

def get_color(self):
    return self. weaknesses

def profile(self):
    return self.nickname, self.weapons, self. weaknesses


# End of class, beginning of test code
player1 = character('','','')
player1.nickname = 'Dragon Slayer'
player1.weapons = ['pan', 'paper', 'idea', 'rope', 'groceries']
player1.weaknesses = ['slow']

player2 = character('','','')
player2.nickname = 'Cristian'
player2.weapons = ['rope', 'pen', 'paper', 'idea']
player2.weaknesses = ['small', 'confusion']


print("player1: Dragon Slayer")
for item in player1.weapons:
    print("Item: ", item)
for debuff in player1.weaknesses:
    print("Debuff: ", debuff)

print("Player2: Cristian")
for item in player2.weapons:
    print("Item: ", item)
for debuff in player2.weaknesses:
    print("Debuff: ", debuff)
