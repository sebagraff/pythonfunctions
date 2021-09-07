def suminloop (lista1):
    for num in lista1:
       return sum(lista1)

print(suminloop([10,20,30,40,5,6,7,8]))

class Student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

studen1 = Student("JIM","Business", 3.1 , False)


def numtodigits(numbers):
    result=0
    while numbers > 0:
        result=(numbers/10)
    return result
print(numtodigits(10))