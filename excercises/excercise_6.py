import math
from pprint import pprint

sleep_time = [6,2,7,8,5,6.5,7.1,8.5]

print(sum(sleep_time)/len(sleep_time))

print("******************************")

print(297 % 3)

print("*******************************")

print(2**10)

print("********************************")

def is_yearleap(year):
    if year % 4 == 0:
        if year % 400 ==0:
            year_str = str(year)
            print("The year " + year_str + " is a centurial year, and is divisble by 400 hence it is a leap year")
        else:
            year_str = str(year)
            print("The " + year_str + " is a centurial year and is not divisible by 400 hence, it is not a leap year")
    else:
        year_str = str(year)
        print("The " + year_str + " year is not a leap year")


is_yearleap(1600)


school = "my elementary school"
pprint(dir(school))
country = 'usa'
correct_country = country.upper()
print(correct_country)
filename = 'hello.py'
print(filename.endswith('.java'))
print(filename.find('.py'))
print(filename.startswith('world'))