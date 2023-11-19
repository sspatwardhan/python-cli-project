import os
import src.zin_input_methodHandlers as mh
import src.zin_juice_calculator as zjc

def getJuicePartyReqs():
    global results  # for adding all the results and displaying at the end
    results = []
    # Get no. of friends
    noOfFriends = False
    while noOfFriends == False:
        noOfFriends = mh.handleFriendsCount(input(mh.userInputMsg_noOfFriends))
    
    friendCounter = 1

    # Get no. of friends
    while friendCounter <= noOfFriends:
        print("\n--------------- Getting requirements for Friend: ", friendCounter)
        
        # Get calorie stats for the available calories > validate > go ahead
        calStatsPerJuice = False
        while calStatsPerJuice == False:
            calStatsPerJuice = mh.handleCalorieStats(input(mh.userInputMsg_caloriesPerJuice))
        
        # Get available juice names > validate > go ahead
        juiceNames = False
        while juiceNames == False:
            juiceNames = mh.handleJuiceNameSequene(calStatsPerJuice[0],input(mh.userInputMsg_juiceNames))

        # Get calorie intake for friends > validate > go ahead
        friendsCalReq = False
        while friendsCalReq == False:
            friendsCalReq = mh.handleCalorieIntakeForFriend(input(mh.userInputMsg_caloriesForFriend))

        # Increase friend the count once everything looks good
        friendCounter += 1

        # Go on appending the results for every friend
        results.append(zjc.findJuiceMix(juiceNames, calStatsPerJuice, friendsCalReq))


# Call methods
os.system('clear') # Clean the console
print(mh.welcome("ZINO")) # Greet the user
getJuicePartyReqs() # Get the requirements
mh.showResults(results) # Print the results