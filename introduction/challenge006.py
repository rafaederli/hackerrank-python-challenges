# Write a function
def is_leap(year):
    leap = False
    if (year % 4 == 0):
        if (year % 100 != 0):
            leap = True
        if (year % 100 == 0) & (year % 400 == 0):
            leap = True
    return leap
year = int(input())
print(is_leap(year))