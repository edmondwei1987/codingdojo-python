import random
def coin_tosses(times):
    head_count=0
    tail_count=0
    for i in range(0,times):
        head_or_tail=''
        coin=random.random()
        if round(coin)==0:
            head_count=head_count+1
            head_or_tail='head'
        else:
            tail_count=tail_count+1
            head_or_tail='tail'
        print "Attempt #{}: Throwing a coin... It's a {}! ... Got {} head(s) so far and {}tail(s) so far".format(i+1,head_or_tail,head_count,tail_count)

coin_tosses(100)
