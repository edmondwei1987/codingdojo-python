def draw_stars(ls):
    for item in ls:
        string=''
        if isinstance(item,int):
            for i in range(0,item):
                string=string+'*'
        elif isinstance(item,str):
            for i in range(0,len(item)):
                string=string+item[0].lower()
        print string

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars(x)
# draw_stars([4, 6, 1, 3, 5, 7, 25])