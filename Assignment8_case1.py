class AttendanceShortageException(Exception):
    def __init__(self,arg):
        self.msg=arg
class IncomeException(Exception):
    def __init__(self,arg):
        self.msg=arg
class GPAException(Exception):
    def __init__(self,arg):
        self.msg=arg
attendance=int(input("Enter Student Attendance Percentage(1-100)==>"))
income=int(input("Enter Student, parents Income==>"))
cgpa=int(input("Enter Student CGPA(0n 10 Scale)==>"))
if attendance<75:
    raise AttendanceShortageException("Student is having Attendance Shortage")
    print("Student is Thrown")
elif income>500000:
    raise IncomeException("Parents Income is more")
    print("Student is Thrown")
elif cgpa<7:
    raise GPAException("Student having CGPA Shortage")
    print("Student is Thrown")
else:
    print("Student is not Thrown")