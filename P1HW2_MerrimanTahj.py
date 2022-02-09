#Basic code for a Pizza order
# 01FEB2022
# CTI-110 P1HW2 - Pizza Order
# Merriman, Tahj

#Start
#Request input from user for how many students
#define variables
#if 1 student will eat 3 slices of pizza
#and one pizza yeilds 6 slices of pizza
#then then the number of pizzas will be the number of total slices divided by slices in a single pizza
#print outputs
#end

StuNum=int(input('How Many Students would like Pizza?  '))
StuSlc=StuNum * 3
PizzaWhl=StuSlc / 6

print()
print('----Pizza Order--------')
print('Number of Student:',StuNum)
print('Number of Slices:',StuSlc)
print('Number of Pizzas Needed:',PizzaWhl)
print('---------------------------')







