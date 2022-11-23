from pprint import pprint

print ('1. Create a dictionary, info, that holds your first name, last name, and age.')
me = {'fname': 'Mateusz', 'lname' : 'Magiera', 'age': 26}

print(20 * '*')

print('2. Create an empty dictionary, phone, that will hold details about your phone. Add the\
screen size, memory, OS, brand, etc. to the dictionary.')

phone = {}
phone['sceen size'] = 5.6
phone['memory'] = 128
phone['OS'] = 'Android'
phone['brand'] = 'Xiaomi'
phone['color'] = 'black'
phone['age'] = 1.5

print(phone)

print(20 * '*')

print('3. Write a paragraph in a triple-quoted string. Use the .split method to create a list of\
words. Create a dictionary to hold the count for every word in the paragraph.')

paragraph = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis ligula leo, suscipit ac odio at, 
sodales lacinia est. Maecenas viverra suscipit suscipit. Fusce tincidunt rutrum ligula, sed viverra erat semper sed. 
Proin ultricies, mauris vel laoreet pretium, dolor nisl euismod nulla, euismod luctus lacus tortor et odio. 
Integer in nisl et odio volutpat egestas eget at dolor. Mauris dignissim, est nec mattis pharetra, sem lorem pulvinar 
est, nec egestas risus neque nec enim. Quisque eget nulla sit amet dolor bibendum placerat. Maecenas pellentesque tellus
et hendrerit consequat. Quisque est nisl, laoreet in orci eu, rhoncus volutpat nunc. Morbi ac massa id quam 
sollicitudin sagittis at in lorem. Phasellus bibendum velit nec tempor ultricies. Quisque quis sem interdum lectus 
venenatis semper ut auctor purus. Duis in lorem nibh. Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
tu niorp tes. elv cen ole ue di cunn muspi
'''

splited_paragpraph = paragraph.split()

count = {}
for word in splited_paragpraph:
    count.setdefault(word,0)
    count[word] += 1
pprint(count)

print(20 * '*')

print('5. Write code that will print out the anagrams (words that use the same letters) from a\
paragraph of text.')
print(splited_paragpraph)

# empty dictionary which holds subsets
# of all anagrams together
dict = {}

# traverse list of strings
for strVal in splited_paragpraph:

    # sorted(iterable) method accepts any
    # iterable and returns list of items
    # in ascending order
    key = ''.join(sorted(strVal))

    # now check if key exist in dictionary
    # or not. If yes then simply append the
    # strVal into the list of it's corresponding
    # key. If not then map empty list onto
    # key and then start appending values
    if key in dict.keys():
        dict[key].append(strVal)
    else:
        dict[key] = []
        dict[key].append(strVal)
print(dict)