a = 10
b = 3

print('Add -', a + b)
print('Subtract -', a - b)
print('Multiply -', a * b)
print('Divide (with floating point) -', a / b)
print('Divide (ignoring floats) -', a // b)

# With interactive python
# >>> 10 / 3
# 3.3333333333333335
# >>> 10.0 / 3
# 3.3333333333333335
# >>> 10 // 3
# 3
# >>> 10 // 3.0
# 3.0

print('Remainder or Modulus -', a % b)
print('a raised to power b -', a ** b)


# Augmented assignment operator or enhanced assignment operator

# Increment
a += b      # Means, a = a + b
print('a incremented by b -', a);

# Decrement
a -= b
print('a decremented by b -', a)

# Multiply, Divide (floating point & integer), Modulo
a *= b
print(a)

a /= b
print(a)

a //= b
print(a)

a %= b
print(a)
