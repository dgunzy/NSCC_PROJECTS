#include <iostream>
#include "persistence.h"
#include "gameController.h"

int main() {
    std::string inputName =  checkName();
    Player currentPlayer { loadOrCreatePlayer(inputName) };
    runMenu(currentPlayer);
    return 0;
}
