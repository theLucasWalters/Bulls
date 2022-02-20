class Player():
    def __init__(self, name, number, college, position, captain: bool):
        self.name = name
        self.number = number
        self.college = college
        self.position = position
        self.captain = captain

lineup = [
    Player(
        'Ron Harper',
        9,
        'Miami University',
        'Guard',
        False,
    ),
    Player(
        'Tony Kukoc',
        7,
        'Croatia',
        'Forward',
        False,
    ),
    Player(
        'Dennis Rodman',
        91,
        'Southeastern Oklahoma State University',
        'Forward',
        False,
    ),
    Player(
        'Scottie Pippen',
        33,
        'Central Arkansas',
        'Forward',
        False,
    ),
    Player(
        'Michael Jordan',
        23,
        'North Carolina',
        'Guard',
        True,
    ),
]

for player in lineup:
    announce = f'Playing {player.position}, number {player.number}, from {player.college}'

    if player.captain:
        announce += f', your captain'
    
    announce += f', {player.name.upper()}!'

    print(announce)
