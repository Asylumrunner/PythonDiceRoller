import random
import statistics

def diceRoller (dice):
	dice = dice.split("d")
	result = 0
	for i in range(int(dice[0])):
		result += random.randint(1, int(dice[1]))
	return result

print("What do you wanna do?")
print("A. XdX dice roller")
print("B. Asphyxia dice tester")
print("C. Blackmarked dice tester")
print("D. new Blackmarked dice tester")
choice = input("Please enter your choice: ")

if choice == "A":
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
elif choice == "B":
    attribute = int(input("Enter the character's attribute score: "))
    skill = int(input("Enter the character's skill rank: "))
    if skill == 0:
        tn = int(attribute) - 1
    else:
        tn = int(attribute) + int(skill)
    #disadvantageDice = int(input("How many disadvantage dice?: "))
    repetitions = int(input("How many repetitions of this roll?"))

    for q in range(0, 20):
        disadvantageDice = q
        successes = 0
        failures = 0
        for z in range(repetitions):
            succeeded = False
            lowestValue = 11

            for y in range(0, 2):
                result = diceRoller("1d10") - 1
                if result < tn:
                    succeeded = True
                if result < lowestValue:
                    lowestValue = result;

            for x in range(0, disadvantageDice):
                disResult = diceRoller("1d6")
                if disResult < lowestValue:
                    succeeded = False

            if succeeded:
                successes += 1
            else:
                failures += 1

        percentage = (successes/(successes + failures))
        print("For %s Disadvantage Dice, there were %s successes and %s failures, with an overal success percentage of %s" %(disadvantageDice, successes, failures, percentage))

elif choice == "C":
    #modifier = int(input("Enter the modifier for the test: "))
    #skillOrInnate = int(input("Enter the Skill or Innate: "))
    #difficultyNumber = int(input("Enter the difficulty number: "))
    repetitions = int(input("How many repetitions of this roll?"))

    f = open("BlackmarkedDataFile", 'w')
    for skill in range(0, 6):
        for difficultyNumber in range(0, 6):
            f.write("For skill %s and difficulty number %s \n" %(skill, difficultyNumber))
            for modifier in range(-3, 4):
                dice = 2 + modifier + skill
                victories = 0
                failures = 0
                for g in range(repetitions):
                    successes = 0
                    for i in range(0, dice):
                        result = diceRoller("1d6")
                        if result > 3:
                            successes += 1
                    if successes >= difficultyNumber+1:
                        victories += 1
                    else:
                        failures += 1

                percentage = (victories/(victories + failures))
                f.write("For a modifier %s, there were %s victories and %s failures, with an overall success percentage of %s \n" %(modifier, victories, failures, percentage))
    f.close()

elif choice == "D":
    repetitions = int(input("How many repetitions of these rolls?"))

    f = open("newBlackmarkedDataFile", 'w')
    for skill in range(1, 7):
        f.write("For skill %s \n" %(skill))
        for x in range(0, 11):
            victories = 0
            failures = 0
            dice = 2 + x
            for g in range(repetitions):
                succeeded = False
                for i in range(0, dice):
                    result = diceRoller("1d6")
                    if result <= skill:
                        succeeded = True
                if succeeded:
                    victories += 1
                else:
                    failures += 1
            percentage = (victories/(victories + failures))
            f.write("For %s Stamina Dice, there were %s victories and %s failures, with an overall success percentage of %s \n" %(x, victories, failures, percentage))

    f.close()

elif choice == "E":
    TN = int(input("How high is the target number?: "))
    repetitions = int(input("How many repetitions?: "))

    for bonusDice in range(0, 21):
        successes = 0
        failures = 0
        dice = 2 + bonusDice
        for x in range(repetitions):
            result = diceRoller(str(dice) + "d6")
            if result >= TN:
                successes += 1
            else:
                failures += 1
        percentage = (successes/(successes+failures))
        print("With %s dice added, there were %s successes and %s failures, with an overall success percentage of %s" %(bonusDice, successes, failures, percentage))



