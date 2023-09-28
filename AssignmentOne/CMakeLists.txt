cmake_minimum_required(VERSION 3.26)
project(AssignmentOne)

set(CMAKE_CXX_STANDARD 17)

add_executable(AssignmentOne casino.cpp
        persistence.cpp
        persistence.h
        gameController.cpp
        gameController.h
        games.cpp
        games.h)
