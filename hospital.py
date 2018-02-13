class Patient(object):
    def __init__(self,id,name,allergies,bed_number='none'):
        self.id=id
        self.name=name
        self.allergies=allergies
        self.bed_number=bed_number


class Hospital(object):
    def __init__(self,name,capacity,patients):
        self.name=name
        self.capacity=capacity
        self.patients=patients
        self.bed_number=0
    def admit(self,patient):
        if len(self.patients)>=self.capacity:
            print 'Hospital is Full!!!'
        else:
            self.bed_number+=1
            patient.bed_number=self.bed_number
            self.patients.append(patient)
        return self
        
    def discharge(self,patient):
        for i in range(0,len(self.patients)):
            if patient.bed_number==self.patients[i].bed_number:
                self.patients[i].bed_number='none'
                del self.patients[i]
                break
        return self
    def display(self):
        for p in self.patients:
            print "{}--{}--{}".format(p.name,p.allergies,p.bed_number)


patient1=Patient('1','edmond','flower')
patient2=Patient('2','ada','grass')

hospital=Hospital('garey medical center',400,[])

hospital.admit(patient1).admit(patient2)
hospital.discharge(patient2).display()
            
