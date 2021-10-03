# Project 3 - Calcudoku
#
# Name: Kelsey Nguyen
# Instructor: Workman


import math


def get_cages():
    fullCage = [] 
    totalCages = int(input("Number of cages: "))

    count = 0
    while count < totalCages:
        eachCage = input("Cage number " + str(count) + ": ")
        x = eachCage.split()
        for i in range(len(x)):
            x[i] = int(x[i])
        fullCage.append(x)
        count += 1
    return (fullCage)

def check_rows_valid(puzzle):
    for row in range(5):
        seenList = []
        for col in range(5):
            if puzzle[row][col] != 0:              
                if puzzle[row][col] in seenList:
                    return False
                else:
                    seenList.append(puzzle[row][col])
    return True
                
            
def check_columns_valid(puzzle):
    for col in range(5):
        seenList = []
        for row in range(5):
            if puzzle[row][col] != 0:
                if puzzle[row][col] in seenList:
                    return False               
                else:
                    seenList.append(puzzle[row][col])
    return True


def check_cages_valid(puzzle, cages):
    for eachCage in cages:
        sumNums = []
        sum = 0
        count = 0
        for i in range(2, len(eachCage), 1):
            col = eachCage[i] % 5
            row = (eachCage[i]-col) // 5
            sumNums.append(puzzle[row][col])
        while count < len(sumNums):
            sum = sum + sumNums[count]
            count += 1   
        if sum < eachCage[0] and (0 in sumNums):
            continue
        elif (sum > eachCage[0]) and (0 in sumNums):
            return False
        elif (sum == eachCage[0]) and (0 in sumNums):
            return False
        elif (sum != eachCage[0]) and not (0 in sumNums):
            return False
    return True
            
def check_valid(puzzle, cages):
    if (check_cages_valid(puzzle, cages) and check_columns_valid(puzzle) and check_rows_valid(puzzle) == True):
        return True
    else:
        return False








