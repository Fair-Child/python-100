""""
check the input year is leap or not
"""

year = int(input("Please input year to check leap: "))
result = (year % 4 == 0 and year % 100 != 0 or
          year % 400 == 0)
print("Is this year a leap year? ", result)