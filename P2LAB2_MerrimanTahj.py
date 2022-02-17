current_price = int(input())
last_months_price = int(input())

change_price = current_price - last_months_price
month_morg = (current_price * 0.051) / 12
month_morg_p = f'{month_morg:.2f}'

current_price_str = chr(36) + str(current_price) + '.'
change_price_str = chr(36) + str(change_price)
month_morg_str = chr(36) + str(month_morg_p) +'.'

print('This house is', current_price_str, 'The change is', change_price_str,'since last month.')
print('The estimated monthly mortgage is', month_morg_str)

#This house is $200000. The change is $-10000 since last month.
#The estimated monthly mortgage is $850.00.