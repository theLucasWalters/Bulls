// import std library
use std::fmt;

// create a player struct
struct Player {
    name:String,
    number:u8,
    college:String,
    position:String,
    captain:bool
}

// implement player struct
impl Player {
    // create a new player
    fn new (name:&str, number:u8, college:&str, position:&str, captain:bool) -> Player {
        Player {
            name:name.to_string(),
            number:number,
            college:college.to_string(),
            position:position.to_string(),
            captain:captain
        }
    }
}

// allow player struct to display in console
impl fmt::Display for Player {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(
            f,
            "({}, {}, {}, {}, {})",
            self.name,
            self.number,
            self.college,
            self.position,
            self.captain
        )
    }
}

// run
pub fn run() {

    // create the 5 players
    let player1:Player = Player::new(
        "Ron Harper",
        9,
        "Miami University",
        "Guard",
        false
    );
    
    let player2:Player = Player::new(
        "Tony Kukoc",
        7,
        "Croatia",
        "Forward",
        false
    );

    let player3:Player = Player::new(
        "Dennis Rodman",
        91,
        "Southeastern Oklahoma State University",
        "Forward",
        false
    );

    let player4:Player = Player::new(
        "Scottie Pippen",
        33,
        "Central Arkansas",
        "Forward",
        false
    );

    let player5:Player = Player::new(
        "Michael Jordan",
        23,
        "North Carolina",
        "Guard",
        true
    );

    // create an array to iterate through
    let lineup:[Player; 5] = [player1, player2, player3, player4, player5];

    // iterate and print each Player
    for player in lineup.iter() {
        if !player.captain {
            println!(
                "Playing {}, number {}, from {}, {}!",
                player.position,
                player.number.to_string(),
                player.college,
                player.name.to_uppercase()
            );
        } else {
            println!(
                "Playing {}, number {}, from {}, your captain, {}!",
                player.position,
                player.number.to_string(),
                player.college,
                player.name.to_uppercase()
            );
        }
    }
}
