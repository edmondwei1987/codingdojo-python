class Call(object):
    def __init__(self,id,name,phone,time,reason):
        self.id=id
        self.name=name
        self.phone=phone
        self.time=time
        self.reason=reason
    def display(self):
        for key in self.__dict__:
            print "{} : {}".format(key,self.__dict__[key])


class CallCenter(object):
    def __init__(self,calls):
        self.calls=calls
        self.queue_size=len(calls)
    def add(self,call):
        self.calls.append(call)
    def remove(self):
        self.calls.remove(self.calls[0])
    def remove(self,phone):
        for call in self.calls:
            if call.phone==phone:
                self.calls.remove(call)
    def info(self):
        for call in self.calls:
            # print "{} : {}".format(call.name,call.phone)
            call.display()
    def sort_by_time(self):
        for idx in range(0,len(self.calls)):
            max=self.transfer_time(self.calls[idx].time)
            # print min
            for in_idx in range(0,len(self.calls)):
                if(max<self.transfer_time(self.calls[in_idx].time)):
                    # print outcall,call
                    temp=self.calls[idx]
                    self.calls[idx]=self.calls[in_idx]
                    self.calls[in_idx]=temp

    def transfer_time(self,time):
        time_list=time.split(':')
        return int(time_list[0])*60+int(time_list[1])

my_call=Call('1','edmond','6263776765','10:20','ask for leave permit')
friend_call=Call('2','ada','234434343','5:20','homework')
tony_call=Call('3','tony','4534354354','15:30','ask for money')
call_center=CallCenter([my_call,friend_call,tony_call])
# call_center.info()
# call_center.remove('234434343')
# call_center.info()
# call_center.info()
call_center.sort_by_time()
call_center.info()



