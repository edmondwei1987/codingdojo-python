type_list=['magical unicorns',19,'hello',98.98,'world']
sum=0
string=''
list_type=[]
final_type=''
for item in type_list:
    if isinstance(item,int):
        sum=sum+item
        if 'integer' not in list_type:
            list_type.append('integer')
    elif isinstance(item,str):
        string=string+item+' '
        if 'string' not in list_type:
            list_type.append('string')
    elif 'other_type' not in list_type:
            list_type.append('other_type')
if len(list_type)>1:
    final_type='mixed'
else:
    final_type=list_type[0]
print 'The list you entered is of '+ final_type +' type'
if 'integer' in list_type:
    print "Sum: "+str(sum)
if 'string' in list_type:
    print "String: "+string