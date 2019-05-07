tempDegree = float(input('What\'s the temperature (in degrees)? '))

if tempDegree > 50:
    print('Bone melting hot!!!')
elif tempDegree < 50 and tempDegree > 30:
    print('It\'s a hot day!')
elif tempDegree <= 30 and tempDegree >= 0:
    print('It\'s freezing cold!')
elif tempDegree < 0:
    print('Bone chilling cold!!!')


# != (not equals) is another comparison operator to check is something is not equal to something
