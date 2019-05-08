# Packages are basically another way to organize our code. We don't wanna put all out modules inside the project directory, rather put them in a package. Package is a container for multiple modules. Package is essentially a file or folder.
# To make a directory a package, we simply create a '__init__.py' file in that directory. When python interpreter sees this __init__.py file it treats that directory as Python Package.


# Importing the module inside a package (to access all methods inside that package)
import ecommerce.shipping, ecommerce.tax
# package.module.method()
ecommerce.shipping.shipping_cost(50)
ecommerce.tax.calc_tax(2000)


# Importing specific function from a module inside a package
from ecommerce.shipping import shipping_cost
from ecommerce.tax import calc_tax
# function()
shipping_cost(10)
calc_tax(4000)


# What if we wanna import multiple functions inside a module instead of doing something like 'from ecommerce.shipping import shipping_cost, shipping_place(), something()'
# Import module form a Package (it is different from first approach cuz here 'shipping' and 'tax' are objects instead of 'ecommerce.shipping' and 'ecommerce.tax' objects)
from ecommerce import shipping
from ecommerce import tax
# module.function()
shipping.shipping_cost(20)
tax.calc_tax(6000)
