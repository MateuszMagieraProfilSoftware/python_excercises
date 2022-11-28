print('1. Write a function, is_odd, that takes an integer and returns True if the number is odd\
and False if the number is not odd.')

def is_odd(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_odd(2))

print(20* "*")

print('2. Write a function, is_prime, that takes an integer and returns True if the number is\
prime and False if the number is not prime.')


def is_prime(number):
    if number == 1:
        return True
    elif number == 2:
        return True
    elif number > 2:
        for i in range(2,number):
            if number % i == 0:
                return False
            else:
                return True

