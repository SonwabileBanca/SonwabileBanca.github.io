# A dry joke generator
jokes = ['What kind of concert only costs 45 cents?\n\t>A 50 cents concert featuring Nickleback',
        'How can you tell if a vamipre is sick?\n\t>By being in the coffin.',
        'What runs around the yard without moving?\n\tA fence',
        'What do you get for a pampered cow?\n\tSpoilt milk !!LOL!!',
        'Anyone who believes in Telekenesis\n\tRaise my Hand.',
        'My grandfather said my generation rely on too much technology\n\t>So I unplugged his life support(Just kidding)'
       ]
#impor the random function use the len() as index
from random import randint
print(jokes[randint(0, len(jokes) -1)])
