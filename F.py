#pylint:disable=E0601
#pylint:disable=E0401
import random
from random import randint
import string


from colorama import Fore, Back, Style
def random_string_generator_variable_size(min_size, max_size, allowed_chars):
    return ''.join(random.choice(allowed_chars) for x in range(randint(min_size, max_size)))

chars = string.ascii_letters + string.punctuation


print(Fore.CYAN+'  your code  =  ')

print(Fore.LIGHTGREEN_EX+random_string_generator_variable_size(6, 24, chars))


print(Fore.LIGHTCYAN_EX+'CR : amirhosin0098')
