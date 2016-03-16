# PythonDiceRoller
A simple tool for calculating the experimental average of dice rolls in Python

## An Introduction to Dice Notation
In the realm of tabletop gaming, especially in tabletop role-playing games, design has evolved past the simple six-sided die which is frequently associated with the word "dice". Instead, dice of all sorts of shapes and sizes have been developed so as to generate different numbers, probability densities, and ranges of results.

As a way to easily notate what dice, and how many of those dice, are used for any one action in a game, *dice notation* was developed and standardized. 

Dice notation is actually extremely simple. All statements follow the format

	XdY

Where X represents the number of dice rolled, and Y represents the number of sides on those dice. For example,

	4d6

Means to roll four, six-sided dice, while

	1d12

means to roll one, twelve-sided die. The results of these dice are usually added together, although there are also "dice pool" systems, in which every die is judged as success or failure individually.

There is a notable excpetion, which is for any die sizes which are a power of ten greater than ten, such as

	Xd100
	Xd1000
	Xd10000
	etc

While a one-hundred sided die exists, it is hilariously impractical, and so commonly, for these sorts of rolls, people will use d10s, simply designating beforehand a digit of the result to each die. For example, to roll 1d100, I would roll 2d10, with one die designated as the tens digit, and one as the ones digit. Were my results a 7 on the tens die and a 9 on the ones die, my overall total would be 79.

## Why Build This?
In designing tabletop games, it is my goal to try and ensure that my mechanics and narrative elements are as closely intertwined as possible. In doing so, I usually find that I want a dice roll resolution system which will match the tone and theme of the game.

For example, *Dungeons and Dragons* uses a d20 resolution system, in which players roll a twenty-sided die, adding and subtractic modifiers as needed, attempting to beat a certain number representing the difficulty of the task at hand. Every result has a 1/20 odds of appearing, including a 1, which represents automatic failure, and a 20, which represents automatic success. This fits the theme of D&D, where heroes are meant to always be trying heroic and amazing things knowing, at worst, they always have a 1/20 chance of success. Heroic victory, dismal failure, and barely squeaking by have roughly equal probability.

Other systems with less heroic goals might instead use a system like 4d6. When rolling four, six-sided dice and adding them, the probability curve is more of a bell-curve, with average, middling rolls becoming much more probable than grandiose failure or success, leading to more mundane actions.

As a result of this importance of dice rolls, I built this simple simulator to calculate the experimental average of certain dice rolls, to try and figure out where the probability of more unique dice rolls.
