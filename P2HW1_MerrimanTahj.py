
# Build an interactive shopping budget for user to assess total cost
# 24MAR2022
# CTI-110 P2HW1 - Total Purchases
# Tahj Merriman
#
#Start
#Request input from user for prices on 5 items seperatly
    #5 print functions with inputs, set as float
#print results line
#print subtotal line w/calulations
#print sales tax w/ calculations
#print total of all
#end


Item_1 = float(input('Enter the price of item #1:'))
Item_2 = float(input('Enter the price of item #2:'))
Item_3 = float(input('Enter the price of item #3:'))
Item_4 = float(input('Enter the price of item #4:'))
Item_5 = float(input('Enter the price of item #5:'))

print ('-------Results-------')
print (f'Subtotal: ${Item_1 + Item_2 + Item_3 + Item_4 + Item_5:.2f}')
print (f'Sales Tax: ${(Item_1 + Item_2 + Item_3 + Item_4 + Item_5) * .07:.2f}')
print (f'Total: ${((Item_1 + Item_2 + Item_3 + Item_4 + Item_5) * .07) + (Item_1 + Item_2 + Item_3 + Item_4 + Item_5):.2f}')
