#include "persistence.h"
#include <iostream>
#include <fstream>
#include <string>

Player loadOrCreatePlayer(std::string inputName) {
    Player currentPlayer{ std::string {""}, int { 100 }};
    std::string savedName;
    int savedCoins;
    std::ifstream inputStream("data.txt");
    if (inputStream.is_open()){
        inputStream.seekg(0, inputStream.beg);
        if (inputStream.good()) {
            while (!inputStream.eof()) {
                std::getline(inputStream, savedName);
                inputStream >> savedCoins;
            }
        }
        if (inputName == savedName) {
            std::cout << "Welcome back " <<  inputName << "!\n";
            currentPlayer.playerName = savedName;
            currentPlayer.coins = savedCoins;
        } else {
            currentPlayer = createNewPlayer(inputName);
            inputStream.close();
            return currentPlayer;
        }
    } else {
        currentPlayer = createNewPlayer(inputName);
        inputStream.close();
        return currentPlayer;
    }
    inputStream.close();
    return currentPlayer;
}

Player createNewPlayer(std::string name) {
    std::cout << "Player not found! New player being created." << "\n";
    Player newPlayer{ std::string {name}, int { 100 }};
    std::ofstream outputStream("data.txt");
    outputStream.close();
    saveInfo(newPlayer);
    return newPlayer;
}

void saveInfo (const Player& player) {
    try {
        std::ofstream outputStream("data.txt");
        outputStream << player.playerName << "\n";
        outputStream << player.coins;
        outputStream.close();
        std::cout << "Game Saved!" << "\n";
    } catch (...) {
        std::cout << "Error Saving Game!" << "!\n";
    }
}
std::string checkName() {
    std::cout << "Hello! Welcome to the Casino" << std::endl;
    std::cout << "What is your name player?"<< std::endl;
    while (true) {
        std::string name;
        std::getline(std::cin, name);

        if (name.size() > 2) {
            return name;
        } else {
            std::cout << "That name is too short! " << std::endl;
            continue;
        }
    }
}
