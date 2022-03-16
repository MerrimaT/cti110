
# Debug and Finish grading program
# 16MAR2022
# CTI-110 P3HW1 - Debugging
# Tahj Merriman

#Start
#Define grades
#Request grade input
#if/elif/through grading gates
#anything NOT over 90 and remaining defaults to "F"
#end

def main():
    # This program takes a number grade and outputs a letter grade.
    # system uses 10-point grading scale
    
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    F_score = 50

    score = int(input('Please enter score: '))

    if score >= A_score:
        print('Your grade is: A')
    elif score >= B_score:
        print('Your grade is: B')
    elif score >= C_score:
        print('Your grade is: C')
    elif score >= D_score:
        print('Your grade is: D')
    elif score >= F_score:
        print('Your grade is: F')
    else:
        print('Your grade is: F')
    
# program start
main()
