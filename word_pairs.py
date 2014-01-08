from random import choice



fruits = [
    'apple',
    'avocado',
    'banana',
    'cherry',
    'coconut',
    'date',
    'fig',
    'grape',
    'kiwi',
    'lemon',
    'lime',
    'mango',
    'melon',
    'nut',
    'olive',
    'orange',
    'peach',
    'pear',
    'plum',
    'star',
]

pets = [
    'dog',
    'sheep',
    'pig',
    'goat',
    'cow',
    'cat',
    'duck',
    'camel',
    'goose',
    'yak',
    'mouse',
    'dove',
    'rat',
    'fox',
    'snail',
    'swan',
    'deer',
    'python',
]

s = choice(fruits) + ' ' + choice(pets)
print s.lower()