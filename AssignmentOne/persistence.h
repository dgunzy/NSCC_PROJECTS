//
// Created by d_b_g on 2023-09-14.
//

#ifndef ASSIGNMENTONE_PERSISTENCE_H
#define ASSIGNMENTONE_PERSISTENCE_H

#include <string>

struct Player {
    std::string playerName;
    int coins;
};

Player loadOrCreatePlayer (std::string inputName);
void saveInfo (const Player& player);
Player createNewPlayer(std::string name);
std::string checkName();

#endif //ASSIGNMENTONE_PERSISTENCE_H
