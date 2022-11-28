name = 'Mateusz'
print(name[0])
print(name[-1])

print(20 * '*')

filename = 'myfile.exe'
print(filename[-3:])
print(filename[0:-4])

print(20 * '*')


def is_paliindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False


print(is_paliindrome("kamilślimak"))


print(20 * '*')

