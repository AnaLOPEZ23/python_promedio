class Employee:
    name: str
    age: int
    salary: float
    
    def __init__(self, name: str, age: int, salary: float):
        self.name = name
        self.age = age
        self.salary = salary
    
    def introduce(self) -> str:
        return f"Hola , Me llamo{self.name}, tengo {self.age}"

employee1 = Employee(" Carla lopez ", 30, 3500.0)
print(employee1.introduce())

