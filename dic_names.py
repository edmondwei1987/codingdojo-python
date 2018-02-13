students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

# def call_names(people):
#     for person in people:
#         print person['first_name']+' '+person['last_name']

# call_names(students)

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def call_group_names(people):
    for group in people:
        print group
        for i in range(0,len(people[group])):
            person=people[group][i]
            f_name=person['first_name'].upper()
            l_name=person['last_name'].upper()
            print "{} - {} - {}".format(i+1,f_name+' '+l_name,len(f_name+l_name))

call_group_names(users)
