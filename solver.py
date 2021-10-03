# Project 3 - Calcudoku
#
# Name: Kelsey Nguyen
# Instructor: Workman

from solverFuncs import *



def main():
    row = 0
    col = 0
    check = 0
    backtrack = 0

    puzzle = [[0,0,0,0,0],
              [0,0,0,0,0],
              [0,0,0,0,0],
              [0,0,0,0,0],
              [0,0,0,0,0]]
   
    cages = get_cages()

    while row < 5:
        puzzle[row][col] += 1 
        value = check_valid(puzzle, cages)
        check += 1
        if value == True:
            if col >= 4:
                col = 0
                row += 1
            else:
                col += 1
        else:
            while puzzle[row][col] >= 5:
                puzzle[row][col] = 0
                col -= 1
                if col < 0: 
                    col = 4 
                    row -= 1
                backtrack += 1


    print("\n---Solution---\n")
    
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            print(puzzle[i][j], end=' ')
        print()

    print("\nchecks: " + str(check) + " backtracks: " + str(backtrack))




            
if __name__ == '__main__':
   main()




