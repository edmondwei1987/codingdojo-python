import random
def score_grade(score):
    grade=''
    if score>=60 and score<70:
        grade='D'
    elif score>69 and score<80:
        grade='C'
    elif score>79 and score<90:
        grade='B'
    elif score>89 and score<101:
        grade='A'
    return 'Score:'+str(score)+';Your grade is '+grade

for i in range(0,10):
    num = random.randint(59,100)
    print score_grade(num)
