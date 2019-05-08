# Modules are used to better organize the code. Instead of writing all functions in main file we can divide the functions into different modules and then simply import to use them

import converter

weight = float(input('Weight: '))
print(f'{weight} lbs is {"{0:.2f}".format(converter.lbs_to_kg(weight))} kgs')
print(f'{weight} kgs is {"{0:.2f}".format(converter.kg_to_lbs(weight))} lbs')
