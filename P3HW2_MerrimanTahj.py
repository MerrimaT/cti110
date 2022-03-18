# CTI-110
# P3HW2 - Pizza Order
# Merriman, Tahj
# 17MAR2022

#Start
#Request input from user for how many students
#Request sharing value input
#if sharing value = true
    #print amounts, price and tax (tax is 6%)
#else inform user of error and request start over
#end

def main():
    import math

    stu_num = int(input('How Many Students would like Pizza?  '))
    stu_shr = float(input(f'Enter number of people per pizza (1.5, 2, or 3):'))
    
    if stu_shr in(1.5, 2, 3):
        piz_num = math.ceil(stu_num/stu_shr)
        cost = ((piz_num * 5) * .06) + (piz_num * 5)
        print()
        print('--------Pizza Order--------')
        print('Number of Student:',stu_num)
        print('Number of Pizzas Needed:',piz_num)
        print(f'Total Price with Tax: ${cost:.2f}')
        print('---------------------------')
    else:
        print('\n')
        print('INVALID ENTRY!!!!\nShould have entered 1.5, 2, or 3')
        print('\n')
        print('Run Program again')
main()


   
    



