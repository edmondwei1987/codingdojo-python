words="It's thanksgiving day. It's my birthday,too!"
index=words.index('day')
print index
print words.replace('day','month',1)


x = [2,54,-2,7,12,98]
print min(x)
print max(x)

x = ["hello",2,54,-2,7,12,98,"world"]
y = [x[0],x[len(x)-1]]
print y


x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print [x[0:len(x)/2]]+x[len(x)/2:len(x)]