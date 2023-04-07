"""
Convert the temperature from F to C
"""

f = float(input("Please type in the temperature in F: "))
c = (f-32) / 1.8
print("%.1f F = %.1f C" %(f, c))