import logging as jpLogger
import datetime
generalErr = "Error: Invalid input. Try again."
userInputMsg_noOfFriends = "\n~ No. of friends (between 1 to 200): "
userInputMsg_caloriesPerJuice = "\n~ Number of unique fruit juices followed by their calorie content\n E.g. If 2(juices) then input 2 9 34: "
userInputMsg_juiceNames = "\n~ Sequence of lower case alphabets representing the NAME of the fruit juice\n (E.g. abzzepnpp): "
userInputMsg_caloriesForFriend = "\n~ Number of calories allowed for friend:\n E.g. 1 to any +ve number: "

"""
parameter(s) - numberOfFriends : type - string
Example: handleFriendsCount('5')
returns - validated integer value
Example: handleFriendsCount(5)
"""
def handleFriendsCount(numberOfFriends):
    try:
        if 1 <= int(numberOfFriends) <= 200:
            return int(numberOfFriends)
        else:
            return False
    except ValueError:
        return False


"""
parameter(s) - calorieStats : type - list of strings
Example: handleCalorieStats(['3','15','9','34'])
returns - validated list of integers
Example: handleCalorieStats([3,15,9,34])
"""
def handleCalorieStats(calorieStats):
    calStatInstructions = ''' Instructions:
--- If 2(juices) then input 2 9 34 | Separated by a space | Only positive numbers allowed | No. of juices <= 26 | Calorie content per juice <= 100
    '''
    try:
        calorieStats = calorieStats = list(map(int, calorieStats.split()))
        # here
        # -- map(input().split()): applies ^^ to all elements in the list returning (unreadable) map object
        # -- list(map(input().split())): converts ^^ to readable list
        if calorieStats[0] <= 26 and calorieStats[0] == len(calorieStats) - 1 and not any(item < 1 or item > 100 for item in calorieStats[1:]):
            return calorieStats
        else:
            print(calStatInstructions)
            return False
    except ValueError:
        print(calStatInstructions)
        return False

"""
parameter(s)
    - expectedNumberOfUniqueJuices : type - integer
    - juiceNameSequence : type - list of strings
Example: handleJuiceNameSequene(3,['a','c','b','b','c','a','c'])
returns - sorted list of juice names
Example: ['a','a','a','b','b','c','c']
"""
def handleJuiceNameSequene(expectedNumberOfUniqueJuices, juiceNameSequence):
    juiceNameSequencingInstructions = ''' Instructions:
--- If previous input was 2 9 4, that means you have only 2 juices available but you entered less/more alphabets | Only alphabets are allowed
    '''

    try:
        juiceNameSequence = juiceNameSequence.replace(" ","") # remove spaces
        juiceNameSequenceForValidation = ''.join(set(filter(str.isalpha, juiceNameSequence.lower())))
        # here
            # filter(str.isalpha, juiceNameSequence.lower())
            # -- str.isalpha returns True if all characters in the string are alphabets
            # -- filter creates iteratable object
            # -- set() creates unsorted list of alphabets
            # -- join - joins all the alphabets
        if len(juiceNameSequenceForValidation) == expectedNumberOfUniqueJuices:
            return sorted(list(juiceNameSequence))
        else:
            print(juiceNameSequencingInstructions)
            return False
    except ValueError:
        print(juiceNameSequencingInstructions)
        return False

"""
parameter(s) - calorieIntake : type - string
Example: handleCalorieIntakeForFriend('56')
returns - validated integer
Example: handleCalorieIntakeForFriend(56)
"""
def handleCalorieIntakeForFriend(calorieIntake):
    try:
        calorieIntake = int(calorieIntake)
        if calorieIntake > 0:
            return calorieIntake
        else:
            return False
    except:
        return False

"""
parameter(s) - botName : type - string
returns - greeting message
"""
def welcome(botName):
    return f"""
===========================================================================
|                                                                         |
|           \O___.____ /   I am {botName}!!                                    |
|             \   .  /     Let's make your Juice Party a big hit :-)      |
|               \ ,/                                                      |
|                []                                                       |
|                []                                                       |
|                []                                                       |
|             --------                                                    |
===========================================================================
        """
    

"""
parameter(s) - results : type - list of strings
returns - nothing, just prints the results
"""
def showResults(results):
    print("\nPossible juice mixes you can offer to\n---------------------------------------------------------")
    for r in range(0, len(results)):
        if len(results[r]) > 0:
            print(f"[Friend {r+1}] {results[r]}")
        else:
            print(f"[Friend {r+1}] SORRY, YOU JUST HAVE WATER..")
    print("---------------------------------------------------------")