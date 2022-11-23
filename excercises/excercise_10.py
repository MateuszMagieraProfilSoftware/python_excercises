print("1. Create a list with the names of friends and colleagues. Calculate the average length of the names.")
friends = ['Sam','Dean','Wednesday','Yoh','Geralt']
letters_count = 0
for friend in friends:
    for letter in friend:
        letters_count += 1
print(letters_count/len(friends))

print(20* '*')

print('2. Create a list with the names of friends and colleagues. Search for the name John using \
a for loop. Print not found if you didn’t find it. (Hint: use else).')

friends_and_colleagues = ['Sam','Dean','Wednesday','Yoh','Geralt','Sarah','Jessica']

for friend in friends_and_colleagues:
    if friend in ['John']:
        print('John found')
    else:
        print('Not found')
        break


print(20* '*')


print('Create a list of tuples of first name, last name, and age for your friends and colleagues.\
If you don’t know the age, put in None. Calculate the average age, skipping over any\
None values. Print out each name, followed by old or young if they are above or below\
the average age.')
my_friends = [('John','Wincheser',None),('Sam','Podolski',27),('Michael','Modric',37),('Dean','Z mordoru',58),('Emily','Something',55),
              ('Danny','Idk',None)]
age_count = 0
age_total = 0
for friend in my_friends:
    age_count += 1
    if friend[2] == None:
        continue
    else:
        age_total += friend[2]
print(age_total/age_count)

