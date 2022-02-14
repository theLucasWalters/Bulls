startingLineup = [
    {
        "playerName": "Ron Harper",
        "jerseyNumber": 9,
        "college": "Miami University",
        "position": "Guard",
        "captain": False,
    },
    {
        "playerName": "Tony Kukoc",
        "jerseyNumber": 7,
        "college": "Croatia",
        "position": "Forward",
        "captain": False,
    },
    {
        "playerName": "Dennis Rodman",
        "jerseyNumber": 91,
        "college": "Southeastern Oklahoma State University",
        "position": "Forward",
        "captain": False,
    },
    {
        "playerName": "Scottie Pippen",
        "jerseyNumber": 33,
        "college": "Central Arkansas",
        "position": "Forward",
        "captain": False,
    },
    {
        "playerName": "Michael Jordan",
        "jerseyNumber": 23,
        "college": "North Carolina",
        "position": "Guard",
        "captain": True,
    },
]

for player in startingLineup:
    position = player["position"]
    jerseyNumber = player["jerseyNumber"]
    college = player["college"]
    playerName = player["playerName"]
    
    playerString = "At " + position + ", number " + str(jerseyNumber) + ", from " + college
    
    if player["captain"] == True:
        playerString += ", your captain"
    playerString += ", " + playerName.upper() + "!"
    
    print(playerString)
