# CTI-110
# P4HW21 - Score List
# Tahj Merriman
# 04APR2022
#
#Start
#Request input from user for # of scores 
#define list, enduring score, and loop count
#loop for score input within int scope while input is les than loop count
#apend list
#remove lowest score
#create variable for Score average sum/len of Scores
#define scores
#if/else to define grade
#print requested reults
#end

def main():
    
    num_scores = int(input('Number of scores: '))
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

    low_scor = min(scor_list)
    scor_list.remove(low_scor)
    scor_avg = sum(scor_list)/ len(scor_list)

    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    F_score = 50

    if scor_avg >= A_score:
        scor_avg_l = 'A'
    elif scor_avg >= B_score:
        scor_avg_l = 'B'
    elif scor_avg >= C_score:
        scor_avg_l = 'C'
    elif scor_avg >= D_score:
        scor_avg_l = 'D'
    else:
        scor_avg_l = 'F'

    print ('---------Results---------')
    print (f'Lowest Score  : {low_scor:.2f}')
    print ('Modified List  :',scor_list)
    print (f'Scores Average: {scor_avg:.2f}')
    print (f'Grade         :',scor_avg_l)
    print ('--------------------------')
           
main()
