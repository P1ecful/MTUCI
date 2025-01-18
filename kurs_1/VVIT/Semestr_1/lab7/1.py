class Employee:
    def __init__(self, ID, name):
        self.ID = ID
        self.name = name
        
    def get_info(self):
        return f'ID: {self.ID}, Имя: {self.name}'
        

class Manager(Employee):
    def __init__(self, ID, name, departament):
        Employee.__init__(self, ID, name)
        self.departament = departament
        
    def manage_project(self):
        return self.departament


class Technican(Employee):
    def __init__(self, ID, name, specialization):
        Employee.__init__(self, ID, name)
        self.specialization = specialization
        
    def perform_maintenance(self):
        return self.specialization


class TechManager(Manager, Technican):
    def __init__(self, ID, name, specialization, departament):
        Manager.__init__(self, ID, name, departament)
        Technican.__init__(self, ID, name, specialization)
        
        self.team = []
    
    def add_employee(self, ID, name) -> str:
        self.team.append(Employee(ID, name))
        return f'Подчиненный {name} добавлен'
    
    def team_info(self):
        for member in self.team:
            print(member.get_info())
    
    
emp = Employee(123, "Dima")
man = Manager(234, "Manager", "IT")
tech = Technican(345, "Tecnican", "Developer")
techman = TechManager(111, "TechManager", "IT", "devops")

print(techman.add_employee(emp.ID, emp.name))
print(techman.team_info())