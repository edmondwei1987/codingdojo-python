my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def make_tuple(dict):
    tuple_list=[]
    for key in dict:
        tuple_list.append((key,dict[key]))
    return tuple_list

print make_tuple(my_dict)