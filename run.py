from random import choice
from textwrap import dedent

def top():
    poem = '''
    roses are red, violets are {color},
    hastheresamaysteppeddown.com'''
    com_list = ['a problem','bottom','fathom']
    color_value = choice(com_list)
    first_verse = dedent(poem.format(color=color_value)).strip()
    print(first_verse)

def middle():
    color = input('Pick a color: ')
    color_map = {
        'green':'You typed green, you bean!',
        'red':'You entered red, You are bad!',
        'yellow':'You think you are cool but you are mellow',
    }
    try:
        print(color_map[color])
    except:
        print('Wrong colour, piss off!')        

if __name__ == '__main__':
    verse_list = [top, middle]
    verse = choice(verse_list)
    verse()

