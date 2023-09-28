#include "games.h"
#include "persistence.h"
#include "gameController.h"
#include <iostream>
#include <random>
#include <chrono>

void redOrBlack (int wager, Player& player) {
    std::cout << "Press 1 for red 2 for black "<< std::endl;
    int redBlack = generateRandom(1,2);
    int pick = checkSelection( 1, 2);
    if (redBlack == 1) {
        std::cout << "It was red" << std::endl;
    } else {
        std::cout << "It was black" << std::endl;
    }
    if (pick == redBlack ) {
        std::cout << "You won!!! " << std::endl;
        player.coins += wager;
    } else {
        std::cout << "Sorry! You lost :( " << std::endl;
        player.coins -= wager;
    }
    saveInfo(player);
}

void roulette(int wager, Player& player ) {
    std::cout << "Enter a number between 1 and 36 "<< std::endl;
    int rouletteRoll = generateRandom(0,36);
    int pick = checkSelection( 1, 36);
    std::cout << "The roulette roll was " << rouletteRoll<< std::endl;
    if (pick == rouletteRoll ) {
        std::cout << "You won!!! " << std::endl;
        player.coins += (wager * 36);
    } else {
        std::cout << "Sorry! You lost :( " << std::endl;
        player.coins -= wager;
    }
    saveInfo(player);
}

void dice(int wager, Player& player ) {
    std::cout << "Enter a number between 1 and 6"<< std::endl;
    int diceRoll = generateRandom(1,6);
    int pick = checkSelection( 1, 6);
    std::cout << "The dice rolled  " << diceRoll<< std::endl;
    if (pick == diceRoll ) {
        std::cout << "You won!!! " << std::endl;
        player.coins += (wager * 6);
    } else {
        std::cout << "Sorry! You lost :( " << std::endl;
        player.coins -= wager;
    }
    saveInfo(player);
}

int generateRandom(int lowerBound, int upperBound) {
    long long clockTime { std::chrono::steady_clock::now().time_since_epoch().count() };
    std::mt19937::result_type seed { static_cast<std::mt19937::result_type>(clockTime) };
    std::mt19937 seededPRNG { seed };
    std::uniform_int_distribution randomResult { lowerBound, upperBound };
    return randomResult(seededPRNG);
}

int checkSelection(int selectionLowerBound, int selectionUpperBound) {
    int selection {0};
    while (true) {
        std::cin >> selection;
        if (checkInput() && selection >= selectionLowerBound && selection <= selectionUpperBound) {
                return selection;
            }
        else {
            std::cout << "Please enter a number in the range given above " << std::endl;
            continue;
        }
    }
}