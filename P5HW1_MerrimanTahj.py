# P5HW1 - Score List for student grades using functions
# 26APR2022
# Tahj Merriman
# CTI-110 - Score List
#
#Start
#define functions for retrieving values, calculations, and options print 
#define function for score list
#define function for low and average scores
#define function for grade
#define function for menu
#execute main program
#define scores
#set list to zero
#print menu
#set while parameters for list being zero to execute request to fill
#set while loop for option 1 fill list and execute function
# call remaining functions
#set while loop for option 2 execute print values
#set while loop for option 3 to quit program
#end
   
def num_list():
    num_scores = int(input('Number of scores: '))
    global scor_list
    scor_list = []
    score = 0
    lc = 1
    while num_scores > len(scor_list):
        score = int(input(f'Enter Score #{lc:}: '))
        if (score >= 0) and (score < 101):
            scor_list.append(score)
            lc += 1
        else:
            print('INVALID SCORE! Please enter a value between 0 and 100')
    return scor_list

def scor2(scores):
        low_scor = min(scor_list)
        scor_list.remove(low_scor)
        scor_avg = sum(scor_list)/ len(scor_list)
        return scor_avg, low_scor

def letter_grade ():
    global scor_avg_a
    if scor_avg >= A_score:
        scor_avg_a = 'A'
    elif scor_avg >= B_score:
        scor_avg_a = 'B'
    elif scor_avg >= C_score:
        scor_avg_a = 'C'
    elif scor_avg >= D_score:
        scor_avg_a = 'D'
    else:
        scor_avg_a = 'F'
    return scor_avg_a
    
def print_menu():
    print ("----------MENU----------")
    print ("1) Create Score List")
    print ("2) Display Results")
    print ("3) Exit")
    print ("------------------------")
    global choz
    choz = int(input("Type 1, 2, or 3 for selection: "))
    return choz
    
if __name__ == '__main__':
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    F_score = 50
    scor_list = 0
    print_menu ()

    while (choz is 2 and scor_list == 0):
        print ('No list has NOT been appended, please choose #1 and fill list')
        print_menu ()
    
    while choz == 1:
        num_list()
        scor_avg, low_scor = scor2(scor_list)
        letter_grade ()
        print_menu ()
        
    while choz == 2:
            print ('---------Results---------')
            print (f'Lowest Score  : {low_scor:.2f}')
            print ('Modified List  :',scor_list)
            print (f'Scores Average: {scor_avg:.2f}')
            print (f'Grade         :',scor_avg_a)
            print ('--------------------------')
            print_menu ()

    while choz ==3:
        quit ()

