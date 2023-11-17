import pytest
from zin_input_methodHandlers import handleCalorieIntakeForFriend, handleCalorieStats, handleFriendsCount, handleJuiceNameSequene

def test_handleFriendsCount_positive():
    assert handleFriendsCount("5") == 5

# def test_handleFriendsCount_negative():
#     stdout = handleFriendsCount("-5")

def test_handleCalorieStats_valid_input():
    user_input = "3 10 20 30"
    assert handleCalorieStats(user_input) == [3, 10, 20, 30]

# def test_handleCalorieStats_invalid_input():
#     user_input = "invalid input"
#     assert handleCalorieStats(user_input)

def test_handleJuiceNameSequene_valid_input():
    user_input = "abc"
    assert handleJuiceNameSequene(3, user_input) == ['a', 'b', 'c']

# def test_handleJuiceNameSequene_invalid_input():
#     user_input = "123"
#     assert handleJuiceNameSequene(3, user_input)

def test_handleCalorieIntakeForFriend_valid_input():
    user_input = "50"
    assert handleCalorieIntakeForFriend(1, user_input) == 50

# def test_handleCalorieIntakeForFriend_invalid_input():
#     user_input = "invalid"
#     assert handleCalorieIntakeForFriend(1, user_input)