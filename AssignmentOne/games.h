//
// Created by d_b_g on 2023-09-19.
//

#ifndef ASSIGNMENTONE_GAMES_H
#define ASSIGNMENTONE_GAMES_H
#include "persistence.h"
void redOrBlack (int wager, Player& player);
void roulette(int wager, Player& player );
void dice(int wager, Player& player );
int generateRandom(int lowerBound, int upperBound);
int checkSelection(int selectionLowerBound, int selectionUpperBound);
#endif //ASSIGNMENTONE_GAMES_H
