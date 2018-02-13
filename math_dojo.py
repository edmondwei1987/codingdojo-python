class MathDojo(object):
    def __init__(self,result):
        self.result=result
    def add(self,*args):
        for num in args:
            if isinstance(num,int):
                self.result+=num
            elif isinstance(num,list) or isinstance(num,tuple):
                for subnum in num:
                    self.result+=subnum
        return self
    def subtract(self,*args):
        for num in args:
            if isinstance(num,int):
                self.result-=num
            elif isinstance(num,list) or isinstance(num,tuple):
                for subnum in num:
                    self.result-=subnum
        return self

# print MathDojo(0).add(2).add(2,5).subtract(1,1,3,2).result
print MathDojo(0).add([1], 3,4).add((3,5,7,8), [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result
