[![UT - Juice Party Project](https://github.com/sspatwardhan/zin_juice_party_project/actions/workflows/ut_pipeline_zin_juice_party.yml/badge.svg)](https://github.com/sspatwardhan/zin_juice_party_project/actions/workflows/ut_pipeline_zin_juice_party.yml)

# Juice Party Project

This application helps you plan a juice party by determining the juice combinations based on the calorie requirements of your friends.

## Table of Contents

- [Workflow](#workflow)
- [Project files](#project-files)
- [Thought Process](#thought-process)
- [Unit Testing](#unit-testing)
- [Install](#install)
- [Usage](#usage)
- [Sample Output](#sample-output)

## Workflow

![Alt text](requirement_docs/juice_party_project_workflow.png?raw=true "Workflow")

## Project Files
```
-- Main file:
zin_juice_main.py
-- Supporting files:
src/zin_input_methodHandlers.py
src/zin_juice_calculator.py
-- Unit Test files:
src/test_zin_input_methodHandlers.py
```

## Thought Process

1. Intuitive, well guided for the end user
2. Assumptions (as per [requirements](requirement_docs/Problem1.pdf))
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

## Unit Testing

Prototyped UTs with positive and negative scenarios covered 

```
-- Unit Test files:
src/test_zin_input_methodHandlers.py
```

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

### Normal flow

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

---------------------------------------------------------
Possible juice mixes you can offer to
---------------------------------------------------------
[Friend 1]: aaaa
[Friend 2]: y
---------------------------------------------------------
```

### Error handling

```
~ No. of friends (between 1 to 200): -1
Error: Invalid input. Try again.

~ No. of friends (between 1 to 200): abc
Error: Invalid input. Try again.
```

```
~ Number of unique fruit juices followed by their calorie content
 E.g. If 2(juices) then input 2 9 34: 2 3 4 5
Error: Invalid input. Try again.
Instructions:
--- If 2(juices) then input 2 9 34
--- Separated by a space
--- Only positive numbers allowed
--- No. of juices <= 26
--- Calorie content per juice <= 100
    

~ Number of unique fruit juices followed by their calorie content
 E.g. If 2(juices) then input 2 9 34: abcd
Error: Invalid input. Try again.
Instructions:
--- If 2(juices) then input 2 9 34
--- Separated by a space
--- Only positive numbers allowed
--- No. of juices <= 26
--- Calorie content per juice <= 100
```

```
~ Sequence of lower case alphabets representing the NAME of the fruit juice
 (E.g. abzzepnpp): abc       
Error: Invalid input. Try again.
Instructions:
--- If previous input was 2 9 4, that means you have only 2 juices available
but you entered less/more alphabets
--- Only alphabets are allowed
    

~ Sequence of lower case alphabets representing the NAME of the fruit juice
 (E.g. abzzepnpp): 8888
Error: Invalid input. Try again.
Instructions:
--- If previous input was 2 9 4, that means you have only 2 juices available
but you entered less/more alphabets
--- Only alphabets are allowed
```

```
~ Number of calories allowed for friend:
 E.g. 1 to any +ve number: - 
Error: Invalid input. Try again.

~ Number of calories allowed for friend:
 E.g. 1 to any +ve number: -500
Error: Invalid input. Try again.

~ Number of calories allowed for friend:
 E.g. 1 to any +ve number: ab
Error: Invalid input. Try again.
```
