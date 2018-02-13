me={
    'name':'edmond',
    'age':30,
    'birth country':'China',
    'favorite language':'Python'
}

def introduce(person):
    for character in person:
        print "My {} is {}".format(character,person[character])

introduce(me)