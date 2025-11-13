from clsfiles import studentscls

# For Students
ids = int(input("S-ID : "))
name = input("S-Name : ")
result = float(input("S-Result : "))
iqLevel = int(input("S-Iq-Level : "))
s1 = studentscls.Student(ids, name, result, iqLevel)
s1.studentResult()
s1.intiligenceStudent()