
# CTI-110
# P2HW2 - Score Avg
# Tahj Merriman
# 24MAR2022
#
#Start
#Request input from user for scores on 7 times seperatly
    #7 print functions with inputs, set as float
#Create list
#assign variable for lowest score
#remove lowest score
#create variable for Score average sum/len of Scores
#print requested reults
#end


Scor_1 = float(input('Enter the score #1:'))
Scor_2 = float(input('Enter the score #2:'))
Scor_3 = float(input('Enter the score #3:'))
Scor_4 = float(input('Enter the score #4:'))
Scor_5 = float(input('Enter the score #5:'))
Scor_6 = float(input('Enter the score #6:'))
Scor_7 = float(input('Enter the score #7:'))

Scor_List = [Scor_1, Scor_2, Scor_3, Scor_4, Scor_5, Scor_6, Scor_7]
Low_Scor = min(Scor_List)
Scor_List.remove(Low_Scor)
Scor_Avg = sum(Scor_List)/ len(Scor_List)

print ('-------Results-------')
print (f'Lowest Score  : {Low_Scor:.2f}')
print ('Modified List :',Scor_List)
print (f'Scores Average: {Scor_Avg:.2f}')
print ('----------------------')
