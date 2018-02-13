def odd_even():
    odd_even=''
    for num in range(1,2001):
        if num%2==0:
            odd_even='even'
        else:
            odd_even='odd'
        print 'Number is '+str(num)+'. This is an '+odd_even+' number.'
odd_even()

def multiply(num_list,multipy_num):
    for idx in range(0,len(num_list)):
        num_list[idx]=num_list[idx]*multipy_num
    return num_list
print multiply([2,4,10,16],5)

def layered_multiples(arr):
    new_arr=[]
    for num in arr:
        new_sub_arr=[]
        for i in range(0,num):
            new_sub_arr.append(1)
        new_arr.append(new_sub_arr)
    return new_arr
print layered_multiples(multiply([2,5,8],2))