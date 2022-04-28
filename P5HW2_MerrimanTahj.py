#
# Addition Subtraction Game
# 28ARP2022
# CTI-110 P5HW2 - Math Quiz
# Merriman Tahj
#
#import random
#def random addition and subtraction functions
#   set two separate random numbers
#   request the user do math
#   set global variable for program answer
#def response function
#   set loop for correct or incorrect response
#def menu display
#   print GUI options and set input int to global variable
#def menu options loop
#   set menu choz to options
#   request user response
#run main function
#   define global variables to 1
#   run while loop to cycle function unless user enters 3 to exit
#start "main function"


import random

def num (num):
    choz = random.randint(1,10)
    choz_2 = random.randint(1,10)
    print(f"Please add these numbers: \n  {choz} \n +{choz_2}")
    global prg_ans
    prg_ans = choz + choz_2
    return prg_ans

def num_sub (num):
    choz = random.randint(1,10)
    choz_2 = random.randint(1,10)
    print(f"Please add these numbers: \n  {choz} \n -{choz_2}")
    global prg_ans
    prg_ans = choz - choz_2
    return prg_ans

def user_rsp (ans1):
    if  ans1 == prg_ans:
        print ('you are a winner!! Seriously so smart.\nPat yourself on the back, you handsome devil you.')
    else:
        print (f'you definatly lost this round.\nThe answer was: {prg_ans}, please try your luck again.')

def print_menu ():
    global choz
    print()
    print(f'  MAIN MENU  ')
    print(f'-----------------------')
    print(f'1. Adding Random Numbers')
    print(f'2. Substracting Random Numbers')
    print(f'3. Exit')
    print()
    print('Please choose one of the Menu options')
    choz = int(input(f'Please select: '))
    return choz

def options ():
    if choz == 1:
        num(num)
        ans = int(input(f'what is your answer: '))
        user_rsp(ans)
    elif choz == 2:
        num_sub(num)
        ans = int(input(f'what is your answer: '))
        user_rsp(ans)
    else:
        print()
        print('Sorry, you didnt select an option, please choose 1, 2, or 3.')
        
def main ():
    print_menu ()
    prg_ans = 1
    prg_ans_sub = 1
    while choz != 3:
        if (choz==1)or(choz==2):
            options()
            print_menu()
        else:
            options()
            print_menu()
    else:
        quit        

main()
