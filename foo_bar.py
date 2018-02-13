for num in range(100,1001):
    output=''
    foo=True
    bar=False
    for i in range(2,num):
        if num%i==0:
            foo=False
        if num==i*i:
            bar=True
            output=output+' Bar'
    if foo:
        output=output+' Foo'
    if foo or bar:
        print str(num)+':'+output
    # if bar:
    #     print str(num)+':'+output
    
        