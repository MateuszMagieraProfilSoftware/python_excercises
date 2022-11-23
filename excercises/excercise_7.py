age = 26
old = 18

print(bool(age > old))

print("*******************************************")

name = "Mateusz"
name_first_letter = name[0].lower()
second_half = ['m','n','o','p','r','s','t','u','v','w','x','y','z']

print(name_first_letter in second_half)
print("*********************************************")

names = ['Sam']

if names:
    print("There are some names in the list")
else:
    print('The list is empty')


print("**************************************")


car = None

if car:
    print('You have a car!')
else:
    print('Taxi for you!')