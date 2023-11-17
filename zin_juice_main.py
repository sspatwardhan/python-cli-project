import os
import src.zin_input_methodHandlers as mh
import src.zin_juice_calculator as zjc


def getJuicePartyReqs():
    global results  # for adding all the results and displaying at the end
    results = []
    # Get user input with prompts
    noOfFriends = mh.handleFriendsCount(input("\n~ No. of friends (between 1 to 200): "))
    friendCounter = 1
    while friendCounter < noOfFriends+1:
        print("\n--------------- Getting requirements for Friend: ", friendCounter)
        calStatsPerJuice = mh.handleCalorieStats(input("\n~ Number of unique fruit juices followed by their calorie content\n E.g. If 2(juices) then input 2 9 34: "))
        
        # Params - juice count, (ask for) juice name sequence
        juiceNames = mh.handleJuiceNameSequene(calStatsPerJuice[0],input("\n~ Sequence of lower case alphabets representing the NAME of the fruit juice\n (E.g. abzzepnpp): ").strip())
        friendsCalReq = mh.handleCalorieIntakeForFriend(friendCounter, input(f"\n~ Number of calories allowed for Friend: {friendCounter}\n E.g. 1 to any +ve number: "))
        friendCounter += 1
        results.append(zjc.findJuiceMix(juiceNames, calStatsPerJuice, friendsCalReq))

os.system('clear') # this will clean the console
mh.welcome()
getJuicePartyReqs()
mh.showResults(results)