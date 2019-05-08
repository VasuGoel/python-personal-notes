# We can also import just one specific function of a module like
from converter import lbs_to_kg

weight = float(input('Weight: '))
# Instead of calling the method like converter.lbs_to_kg() we can simply call lbs_to_kg() function since we only imported the lbs_to_kg() function from converter module
print(f'{weight} lbs is {"{0:.2f}".format(lbs_to_kg(weight))} kgs')
