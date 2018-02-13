for row in range(0,13):
    string=''
    for col in range(0,13):
        if row==0 and col==0:
            string=string+'X '
        elif row==0:
            string=string+str(col)+' '
        elif col==0:
            string=string+str(row)+' '
        else:
            string=string+str(col*row)+' '
    print string