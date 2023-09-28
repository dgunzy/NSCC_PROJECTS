#include "gameController.h"
#include "persistence.h"
#include "games.h"
#include <iostream>

void runMenu(Player& player) {
    while (true) {
        restockCoins(player);
        displayCoins(player);
        runGame(isValidOption(), player);
    }
}

int isValidOption() {
    while (true) {
    int gameChoice {0};
    std::cout << "\n\nPress 1 for Red or Black, 2 for Roulette, 3 for Dice, 4 to quit\n" << std::endl;
    std::cout << "Enter selection here: " << std::endl;
    std::cin >> gameChoice;
    if (checkInput() && gameChoice > 0 && gameChoice < 5) {
        return gameChoice;
    } else {
        continue;
    }
    }
}

void runGame(int userOption, Player& player) {
    switch (userOption) {
        case 1:
            std::cout << "You picked Red or Black! \n";
            redOrBlack(placeWager(player),  player);
            break;
        case 2:
            std::cout << "You picked Roulette! \n";
            roulette(placeWager(player),  player );
            break;
        case 3:
            std::cout << "You picked Dice! \n";
            dice(placeWager(player),  player );
            break;
        case 4:
            saveInfo(player);
            std::cout << "Thanks for playing!  \n";
            std::exit(0);
        default:
            std::cout << "Something went wrong, please enter a number between 1-4  \n";
    }
}

void displayCoins(Player& player) {
    std::cout << "You have " << player.coins << " coins remaining. \n";
}

void restockCoins(Player& player) {
    if (player.coins <= 0) {
        std::cout << "You went bust! Luckily this is a charity casino. Have some free money!" << std::endl;
        player.coins = 100;
        saveInfo(player);
    }
}

int placeWager(Player& player) {
    int wager { 0 };
    while (true) {
        displayCoins(player);
        std::cout << "Enter the amount you want to bet between 1 and 50 coins: \n" << std::endl;
        std::cin >> wager;
        if (checkInput() && player.coins >= wager) {
            if (wager <= 0 || wager > 50) {
                continue;
            } else {
                return wager;
            }
        }
    }
}

bool checkInput() {
    std::cin.clear();
    std::cin.ignore(1000, '\n');
    if (std::cin.good()) {
        return true;
    } else {
        return false;
    }
}

