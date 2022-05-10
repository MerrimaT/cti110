# CTI-110
# P4HW2 - Pizza Order
# Merriman, Tahj
# 5APR2022

#Start
#define constant for loop
#set while for loop for continuing code
#ask user for inputs
#set while loop for valid input
#set else to execute pizza order
#initiate loop to continue code
#set last loop to end code option vs continue initial loop
#end

def main():
    import math

    chose = 'y'
    while chose == 'y':
        while chose == 'y':
            stu_num = int(input('How Many Students would like Pizza?  '))
            stu_shr = float(input(f'Enter number of people per pizza (1.5, 2, or 3):'))
            
            while stu_shr not in (1.5, 2, 3):
                print('INVALID ENTRY!!!!\nShould have entered 1.5, 2, or 3')
                stu_shr = float(input(f'Enter number of people per pizza again.(1.5, 2, or 3):'))
            else:
                piz_num = math.ceil(stu_num/stu_shr)
                cost = ((piz_num * 5) * .06) + (piz_num * 5)
                print()
                print('--------Pizza Order--------')
                print('Number of Student:',stu_num)
                print('Number of Pizzas Needed:',piz_num)
                print(f'Total Price with Tax: ${cost:.2f}')
                print('---------------------------\n')
                chose = str(input('Would you like to run program again (y for YES, n for NOT):'))
        while (chose != 'y') and (chose != 'n'):
            print('INVALID ENTRY!')
            chose = str(input('Would you like to run program again (y for YES, n for NOT):'))
        if chose == 'n':
            print('Good Bye')
        else:
            chose = 'y'

main()


   
    



