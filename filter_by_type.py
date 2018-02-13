# print type(5) int
# print type([1,2,3]) list
# print type('jfkldsjfl') str
variable=[45,100,455,0,-23,"","Rubber baby buggy bumpers",
"Experience is simply the name we give our mistakes",
"Tell me and I forget. Teach me and I remember. Involve me and I learn.",
[],[4,34,22,68,9,13,3,5,7,9,2,12,45,923],[3,5,7,34,3,2,113,65,8,89],
[1,7,4,21],['name','address','phone number','social security number']]
for var in variable:
    if isinstance(var,int):
        if var>=100:
            print "That's a big number!"
        else:
            print "That's a small number!"
    elif isinstance(var,list):
        if len(var)>=10:
            print 'Big list'
        else:
            print 'Short List'
    elif isinstance(var,str):
        if len(var)>=50:
            print 'Long sentence'
        else:
            print 'Short sentence'
    else:
        print 'unknow type'