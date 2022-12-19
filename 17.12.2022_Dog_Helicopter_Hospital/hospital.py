"""Hospital class"""


class Hospital:
    def __init__(self, name, address, phone, website, operating_status):
        self.name = name
        self.address = address
        self.phone_number = phone
        self.website = website
        self.operating_status = operating_status
        self.employees = dict()
        self.medicine = dict()

    def add_employee(self, employee_name, employee_surname, employee_phone):
        if employee_phone not in self.employees.keys():
            self.employees[employee_phone] = employee_name, employee_surname, employee_phone

    def show_employees(self):
        for i in self.employees.keys():
            print(self.employees[i])

    def remove_employees(self, employee_number):
        if employee_number in self.employees.keys():
            self.employees.pop(employee_number)
        else:
            print("Could not find the info.")

    def add_medicine(self, name, quantity):
        if name not in self.medicine.keys():
            self.medicine[name] = quantity
        else:
            self.medicine[name] = self.medicine[name] + quantity

    def show_medicine(self):
        for i in self.medicine.keys():
            print(i, "---->", self.medicine[i])

    def show_hospital_info(self):
        print("------------Hospital info------------")
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Phone number: {self.phone_number}")
        print(f"Website: {self.website}")
        if self.operating_status == 1:
            print("The hospital is operating now.")
        else:
            print("The hospital is not operating now.")


hospital = Hospital("Yerevan number 1", "Ulneci 18", "093181818", "yerevan1.am", 1)
hospital.add_employee("Matt", "Wilson", "043434343")
hospital.show_employees()
hospital.remove_employees("043434343")
hospital.show_employees()
hospital.add_medicine("Paracetamol", 3)
hospital.show_medicine()
hospital.add_medicine("Paracetamol", 3)
hospital.show_medicine()
hospital.show_hospital_info()
