weight = float(input('Weight: '))
unit = input('(L)bs or (K)g: ')
if unit.upper() == 'L':
    print(f'You are {weight * 0.45} kilos')
elif unit.upper() == 'K':
    # ":.2f".format(var) is used to format floating point output upto 2 decimal places. While ":10.2f".format(var) adds 10 empty space and then display floating point number upto 2 decimal places
    print(f'You are {"{:.2f}".format((weight / 0.45))} pounds')
else:
    print('Invalid choice. Choose either (L)bs or (K)g.')
