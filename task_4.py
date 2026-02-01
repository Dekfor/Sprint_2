class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours = None, rest_days = 0, email = None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email
    @classmethod
    def get_hours(self, name, hours = None, rest_days = 0, email = None):
        return cls(name, hours, rest_days, email) 
    
    @classmethod
    def get_email(self, name, hours = None, rest_days = 0, email = None):
        employee = cls(name, hours, rest_days, email)
        if employee.email is not None:      
            return employee.email
        return f"{name}@email.com"
    
    @classmethod
    def set_hourly_payment(cls, new_payment):
         cls.hourly_payment = new_payment

    def salary(self, hour, hourly_payment):
        hours = self.hours if self.hours is not None else (7 - self.rest_days) * 8
        return hours * self.hourly_payment

