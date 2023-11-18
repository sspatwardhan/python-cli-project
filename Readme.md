# Juice Party Project

This application helps you plan a juice party by determining the juice combinations based on the calorie requirements of your friends.

## Table of Contents

- [Workflow](#workflow)
- [Project files](#project-files)
- [Thought Process](#thought-process)
- [Install] (#install)
- [Usage](#usage)
- [Sample Output](#sample-output)

## Workflow

![Alt text](Zinrelo_Juice_Problem.png?raw=true "Workflow")

## Project Files
```
-- Main file:
zin_juice_main.py
-- Supporting files:
src/zin_input_methodHandlers.py
src/zin_juice_calculator.py
```

## Thought Process

1. Assumptions (as per [requirements](requirement_docs/Problem1.pdf))
    - Ask availibile juices for every friend
    - Do not share available juices
    - Do not eliminate juices from single list
2. Structural break down
    - Logical division of the methods and files for
        - Better testability
        - Error Handling
3. Good to have
    - API backed web-application
    - OOPing
    - Enhanced code coverage through unit tests
    - Enhanced optimization for further unit-testing
    - Logging


## Install

1. Install python3 - https://www.python.org/downloads/
2. Install pip - 
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
```
3. Clone the repository to your local machine, go to cloned dir
4. Install required packages
```
pip install -r pypackages.txt
```

## Usage

4. To run project - execute following command from the root dir
```
python3 zin_juice_main.py
```
3. Run unitTests - execute following command from the root dir
```
pytest
```
    

## Sample Output
```
===========================================================================
|                                                                         |
|           \O___.____ /   I am ZINO!!                                    |
|             \   .  /     Let's make your Juice Party a big hit :-)      |
|               \ ,/                                                      |
|                []                                                       |
|                []                                                       |
|                []                                                       |
|             --------                                                    |
===========================================================================

~ No. of friends (between 1 to 200): 2 

--------------- Getting requirements for Friend:  1

~ Number of unique fruit juices followed by their calorie content
 E.g. If 2(juices) then input 2 9 34: 2 4 2

~ Sequence of lower case alphabets representing the NAME of the fruit juice
 (E.g. abzzepnpp): acaaccacacaaaccac

~ Number of calories allowed for Friend: 1
 E.g. 1 to any +ve number: 16

--------------- Getting requirements for Friend:  2

~ Number of unique fruit juices followed by their calorie content
 E.g. If 2(juices) then input 2 9 34: 3 87 40 30 

~ Sequence of lower case alphabets representing the NAME of the fruit juice
 (E.g. abzzepnpp): ytuytuyyyyty

~ Number of calories allowed for Friend: 2
 E.g. 1 to any +ve number: 30

Possible juice mixes you can offer to
---------------------------------------------------------
[Friend 1] aaaa
[Friend 2] y
---------------------------------------------------------
```