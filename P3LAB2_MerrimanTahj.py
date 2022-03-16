serv = {'Oil change': 35, 'Tire rotation': 19, 'Car wash': 7}

serv_ch = input('Enter desired auto service:\n')

if serv_ch not in serv:
    print (f'You entered: {serv_ch}')
    print ('Error: Requested service is not recognized')
else:
    print (f'You entered: {serv_ch}')
    lw_serv_ch = serv_ch.lower()
    print (f'Cost of {lw_serv_ch}: ${serv[serv_ch]}')
