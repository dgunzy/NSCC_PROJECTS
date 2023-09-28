//
// Created by d_b_g on 2023-09-18.
//

#ifndef ASSIGNMENTONE_GAMECONTROLLER_H
#define ASSIGNMENTONE_GAMECONTROLLER_H

#include "persistence.h"

void runMenu (Player& player);
void displayCoins(Player& player);
bool checkInput();
int placeWager (Player& player);
void restockCoins(Player& player);
int isValidOption();
void runGame(int userOption, Player& player);
#endif //ASSIGNMENTONE_GAMECONTROLLER_H
