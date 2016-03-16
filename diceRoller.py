import random
import statistics

def diceRoller (dice):
	dice = dice.split("d")
	result = 0
	for i in range(int(dice[0])):
		result += random.randint(1, int(dice[1]))
	return result

roll = input("Enter a dice roll to calculate, using the format 'XdX': ")
results = []
repetitions = input("Enter a number of times to run the trial: ")
trialResults = []
for y in range(int(repetitions)):	
	for i in range(1000):
		a = diceRoller(roll)
		results.append(a)

	total = 0
	for x in results:
		total += x
	tmean = total/len(results)
	trialResults.append(tmean)
total = 0
for z in trialResults:
	total += z
mean = total/len(trialResults)



print ("The mean of %s over %s trials, each including 1000 dice rolls is %s" %(roll, repetitions, mean))
input()

