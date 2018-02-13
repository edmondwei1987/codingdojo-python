name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]


def make_dict(list1,list2):
    dict={}
    if len(list1)>=len(list2):
        for i in range(0,len(list2)):
            dict[list1[i]]=list2[i]
    else:
        for i in range(0,len(list1)):
            dict[list2[i]]=list1[i]
    return dict

print make_dict(name,favorite_animal)