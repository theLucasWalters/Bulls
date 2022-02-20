// setup
#include <string>
#include <iostream>
using namespace std;

// player class
class Player {
public:
    string name;
    int number;
    string college;
    string position;
    bool isCaptain;

    // constructor
    Player(string _name, int _number, string _college, string _position, bool _isCaptain) {
        name      = _name;
        number    = _number;
        college   = _college;
        position  = _position;
        isCaptain = _isCaptain;
    }
};

// function stubs
string playerString(Player player);

int main()
{
    // initialize all 5 players
    Player p1("RON HARPER", 9, "Miami University", "Guard", false);
    Player p2("TONY KUKOC", 7, "Croatia", "Forward", false);
    Player p3("DENNIS RODMAN", 91, "Southeastern Oklahoma State University", "Forward", false);
    Player p4("SCOTTIE PIPPEN", 33, "Central Arkansas", "Forward", false);
    Player p5("MICHAEL JORDAN", 23, "North Carlina", "Guard", true);

    // array of players
    Player players[5] = { p1, p2, p3, p4, p5 };

    // print them all out
    for (int i = 0; i < 5; i++) {
        cout << playerString(players[i]) << endl;
    }

    return 0;
}

// build the player string
string playerString(Player player) {
    string output;

    // there's probably a better way to do this, but I don't know what it is :/
    output += "Playing ";
    output += player.position;
    output += ", number ";
    output += to_string(player.number);
    output += ", from ";
    output += player.college += ", ";

    if (player.isCaptain) {
        output += ", your captain, ";
    }

    output += player.name += "!";

    return output;
}
