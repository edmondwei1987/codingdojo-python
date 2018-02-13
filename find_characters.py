word_list = ['hello','world','my','name','is','Anna']
char = 'o'
new_word_list=[]
for word in word_list:
    if word.find(char)>0:
        new_word_list.append(word)
print new_word_list