# Hangman Game 
This repository contains a Hangman game recreation built with Pygame, developed as part of my final project for SSW 215 - Individual Software Engineering at Stevens Institute of Technology.
The project is a completed interactive Hangman game featuring a custom graphical interface, multiple difficulty levels, and structured game state management.

## Project Overview
This Hangman game is a fully interactive GUI application featuring:
* A main menu screen
* Difficulty selection (Easy, Medium, Hard)
* Word lists loaded from external text files
* Hangman character drawing that updates with each incorrect guess
* Win/loss end screen with replay and return to menu options

The game is designed to resemble a standard Hangman game with custom-drawn graphics and a polished visual interface created with Pygame.

## Features
* Complete menu and game flow
* Difficulty-based word selection and guess limits
* Keyboard input letter guessing
* Real-time visual updates for correct and incorrect guesses

## How It Works
### Game Logic
1) Menu Screen -> Choose "Computer"
2) Difficulty Screen -> Easy / Medium / Hard
3) Game Screen
   * User's keyboard input to guess letters
   * Wrong guesses draw the hangman
   * Correct guesses reveal letters
4) Win/Lose Screen
   * Replay
   * Return to menu
###  Word Loading
Words come from external .txt files 

### Difficulty Behavior
| Difficulty | Word Length | Guesses |
|-----------|-------------|---------|
| Easy      | 3–4 chars   | 10      |
| Medium    | 5–6 chars   | 7       |
| Hard      | 7–10 chars  | 5       |


## Running The Game
### Requirements
* Python 3.x
* Pygame  

Install Pygame with:
```bash
pip install pygame
```
Run Game with:
```bash
python hangman.py
```

## Why This Project Is Useful
* Demonstrates GUI development using Pygame
* Shows game state management and rendering loops
* Implements clickable buttons, text rendering and collision detection
* Foundation for larger Pygame applications

## Contributors
Developer: Madison Parente  
Course: SSW 215 - Individual Software Engineering  
Institution: Stevens Institute of Technology  


