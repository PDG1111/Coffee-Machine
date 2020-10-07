prompt = ">"

class user:
    def __init__(self, name, birthDate, phoneNumber, email):
        self.name = name
        self.birthDate = birthDate
        self.phoneNumber = phoneNumber
        self.email = email

        def studentcard(self, student_id):
            self.student_id = student_id

        def employeecard(self, employee_card):
            self.employee_card = employee_card

machine_digital_system = input("Scan your KEA card(1 for student, 2 for employee):")

if machine_digital_system == "1":
    print("Welcome student")
elif machine_digital_system == "2":
    print("Welcome employee")
else:
    exit()
