import os
import src.zin_input_methodHandlers as mh
import src.zin_juice_calculator as zjc

def getJuicePartyReqs():
    global results  # for adding all the results and displaying at the end
    results = []
    # Get user input with prompts
    noOfFriends = mh.handleFriendsCount(input(mh.userInputMsg_noOfFriends))
    friendCounter = 1
    while friendCounter < noOfFriends+1:
        print("\n--------------- Getting requirements for Friend: ", friendCounter)
        calStatsPerJuice = mh.handleCalorieStats(input(mh.userInputMsg_caloriesPerJuice))
        
        # Params - juice count, (ask for) juice name sequence
        juiceNames = mh.handleJuiceNameSequene(calStatsPerJuice[0],input(mh.userInputMsg_juiceNames).strip())
        friendsCalReq = mh.handleCalorieIntakeForFriend(input(mh.userInputMsg_caloriesForFriend))
        friendCounter += 1
        results.append(zjc.findJuiceMix(juiceNames, calStatsPerJuice, friendsCalReq))


os.system('clear') # Clean the console
print(mh.welcome("ZINO")) # Greet the user
getJuicePartyReqs() # Get the requirements
mh.showResults(results) # Print the results