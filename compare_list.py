list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']

same=True
if len(list_one)!=len(list_two):
    print 'The lists are not the same.'
else:
    for i in range(0,len(list_one)):
        if list_one[i]!=list_two[i]:
            print 'The lists are not the same'
            same=False
            break
    if same:
        print 'The lists are the same'
